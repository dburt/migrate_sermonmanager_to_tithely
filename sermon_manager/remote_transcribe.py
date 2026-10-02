"""Orchestrate GPU transcription on Hyperion via ssh + rclone.

Builds a job list (slug -> prompt incl. NIV priming) from the local DB, pushes
meta.json + hyperion_worker.py to hyperion:/D:/stalfreds_transcribe, then loops:
- lists done transcripts on the remote
- runs hyperion_worker.py for a bounded batch (CPU/GPU resumable)
- pulls completed transcripts, imports them into the DB, refreshes FTS
"""

import json
import os
import subprocess
import tempfile
import time
from pathlib import Path

import db
from bible_prompt import build_sermon_prompt

SSH_OPTS = [
    "-i", os.path.expanduser("~/.ssh/id_rsa"),
    "-o", "BatchMode=yes",
    "-o", "StrictHostKeyChecking=accept-new",
    "-o", "ConnectTimeout=15",
]
SSH_TARGET = "dave@100.91.35.72"
REMOTE_BASE = "hyperion:/D:/stalfreds_transcribe"
REMOTE_TRANSCRIPTS = REMOTE_BASE + "/transcripts"
REMOTE_PYTHON = r"C:\Program Files\Python312\python.exe"
AUDIO_DIR = r"D:\stalfreds_audio"
CUDNN_BIN = r"C:\Program Files\Python312\Lib\site-packages\nvidia\cudnn\bin"
CUBLAS_BIN = r"C:\Program Files\Python312\Lib\site-packages\nvidia\cublas\bin"

WORKER_PATH = Path(__file__).with_name("hyperion_worker.py")


def _ssh(command, timeout=3600):
    return subprocess.run(
        ["ssh", *SSH_OPTS, SSH_TARGET, command],
        timeout=timeout, text=True, capture_output=True,
    )


def _worker_command(batch_size):
    path_prefix = ("set \"PATH=%s;%s;%%PATH%%\" && " % (CUDNN_BIN, CUBLAS_BIN))
    return (path_prefix
            + f'"{REMOTE_PYTHON}" D:\\stalfreds_transcribe\\worker.py --limit {batch_size}')


def _rclone(args, timeout=600):
    return subprocess.run(["rclone", *args], timeout=timeout,
                          text=True, capture_output=True)


def _list_remote(echo):
    r = _rclone(["lsf", REMOTE_TRANSCRIPTS])
    if r.returncode != 0:
        echo(f"  rclone lsf failed: {r.stderr.strip()}")
        return set()
    return {ln.strip()[:-4] for ln in r.stdout.splitlines() if ln.strip().endswith(".txt")}


def run_remote_transcribe(conn, limit=None, batch_size=10, model="medium", echo=print):
    pending = db.get_pending_transcriptions(conn)
    # Only queue sermons whose audio has already been mirrored to Hyperion.
    pending = [s for s in pending if s.get("local_audio_path")]
    if not pending:
        echo("No pending transcriptions (with mirrored audio).")
        return 0
    if limit:
        pending = pending[:limit]

    jobs = []
    for s in pending:
        slug = s.get("slug")
        if not slug:
            continue
        try:
            prompt = build_sermon_prompt(s)
        except Exception as e:
            echo(f"  (prompt build failed for {slug}: {e})")
            prompt = ""
        jobs.append({
            "slug": slug,
            "tithely_sermon_id": s.get("tithely_sermon_id"),
            "wordpress_sermon_id": s.get("wordpress_sermon_id"),
            "audio": f"{slug}.mp3",
            "prompt": prompt,
        })
    echo(f"{len(jobs)} jobs queued (model={model}, audio from {AUDIO_DIR})")

    from monitor import save_drain_baseline
    save_drain_baseline(conn)

    with tempfile.TemporaryDirectory() as tmp:
        local_tmp = Path(tmp)
        meta_path = local_tmp / "meta.json"
        meta = {"model": model, "audio_dir": AUDIO_DIR, "jobs": jobs}
        meta_path.write_text(json.dumps(meta, ensure_ascii=False), encoding="utf-8")

        _rclone(["mkdir", REMOTE_TRANSCRIPTS])
        _rclone(["copyto", str(WORKER_PATH), REMOTE_BASE + "/worker.py"])
        _rclone(["copyto", str(meta_path), REMOTE_BASE + "/meta.json"])

        total = len(jobs)
        idle_rounds = 0
        round_no = 0
        while True:
            done = _list_remote(echo)
            remaining = [j for j in jobs if j["slug"] not in done]
            if not remaining:
                echo("All jobs transcribed.")
                break
            round_no += 1
            echo(f"[round {round_no}] {len(done)}/{total} done, {len(remaining)} remaining")
            names = ", ".join(j["slug"] for j in remaining[:batch_size])
            echo(f"  running worker ({len(remaining[:batch_size])}): {names}")
            try:
                r = _ssh(_worker_command(batch_size))
                if r.stdout:
                    echo(r.stdout.rstrip())
                if r.returncode != 0 and r.stderr:
                    echo(r.stderr.rstrip())
            except subprocess.TimeoutExpired:
                echo("  worker ssh timed out (will resume next round)")
            new_done = _list_remote(echo)
            if len(new_done) == len(done):
                idle_rounds += 1
                echo(f"  no progress (idle round {idle_rounds})")
                if idle_rounds >= 3:
                    echo("  stopping: no progress after 3 rounds")
                    break
            else:
                idle_rounds = 0
            time.sleep(2)

        _rclone(["copy", REMOTE_TRANSCRIPTS, str(local_tmp)])
        updated = 0
        for txt in sorted(local_tmp.glob("*.txt")):
            slug = txt.stem
            job = next((j for j in jobs if j["slug"] == slug), None)
            if not job:
                continue
            try:
                db.add_transcription(
                    conn, txt.read_text(encoding="utf-8"),
                    tithely_sermon_id=job["tithely_sermon_id"],
                    wordpress_sermon_id=job["wordpress_sermon_id"],
                )
                updated += 1
            except ValueError as e:
                echo(f"  skip {slug}: {e}")
        if updated:
            db.refresh_fts(conn)
        echo(f"Imported {updated} transcripts.")
        return updated