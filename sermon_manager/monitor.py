"""Progress + ETA monitor for the remote transcription drain.

Reports:
- DB totals and how many transcripts exist already
- overall pending (sermons still needing a transcript)
- how many transcript files have landed on the Hyperion mirror vs the job list
- measured throughput (transcripts/hour) and estimated completion time

A small baseline file (logs/transcribe-baseline.json) anchors 'elapsed' to the
start of the current drain run so the rate is measured on growth, not absolutes.
"""

import json
import os
import subprocess
from datetime import datetime, timedelta, timezone

import db

LOGS_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "logs")
BASELINE_PATH = os.path.join(LOGS_DIR, "transcribe-baseline.json")
REMOTE_TRANSCRIPTS = "hyperion:/D:/stalfreds_transcribe/transcripts"
REMOTE_BASE = "hyperion:/D:/stalfreds_transcribe"


def _run(args, **kw):
    return subprocess.run(args, text=True, capture_output=True, **kw)


def _remote_done_count():
    r = _run(["rclone", "lsf", REMOTE_TRANSCRIPTS])
    if r.returncode != 0:
        return 0
    return sum(1 for ln in r.stdout.splitlines() if ln.strip().endswith(".txt"))


def _remote_job_total():
    r = _run(["rclone", "cat", REMOTE_BASE + "/meta.json"])
    if r.returncode != 0:
        return 0
    try:
        return len(json.loads(r.stdout).get("jobs", []))
    except Exception:
        return 0


def _drain_pid():
    r = _run(["pgrep", "-f", "transcribe-remote"], timeout=10)
    if r.returncode != 0:
        return None
    pids = r.stdout.split()
    return int(pids[0]) if pids else None


def _drain_elapsed(pid):
    r = _run(["ps", "-o", "etimes=", "-p", str(pid)], timeout=10)
    if r.returncode != 0 or not r.stdout.strip():
        return None
    try:
        return int(r.stdout.strip())
    except ValueError:
        return None


def _process_start(pid):
    r = _run(["ps", "-o", "lstart=", "-p", str(pid)])
    if r.returncode != 0 or not r.stdout.strip():
        return None
    try:
        local = datetime.strptime(r.stdout.strip(), "%a %b %d %H:%M:%S %Y")
        return local.replace(tzinfo=datetime.now().astimezone().tzinfo)
    except ValueError:
        return None


def _load_baseline():
    if not os.path.exists(BASELINE_PATH):
        return {}
    with open(BASELINE_PATH, encoding="utf-8") as f:
        return json.load(f)


def _save_baseline(pid, started_at, remote_count, db_count):
    os.makedirs(LOGS_DIR, exist_ok=True)
    with open(BASELINE_PATH, "w", encoding="utf-8") as f:
        json.dump({
            "pid": pid,
            "started_at": started_at.isoformat(),
            "remote_baseline": remote_count,
            "db_baseline": db_count,
        }, f)


def status_report(conn, baseline=None, _echo=None):
    _echo = _echo or (lambda s: None)
    now = datetime.now(timezone.utc)
    base = baseline or _load_baseline()

    total_db = conn.execute("SELECT COUNT(*) c FROM v_sermons").fetchone()["c"]
    db_have = conn.execute("SELECT COUNT(*) c FROM transcriptions").fetchone()["c"]
    pend = len(db.get_pending_transcriptions(conn))
    remote_done = _remote_done_count()
    job_total = _remote_job_total()

    pid = _drain_pid()
    elapsed = _drain_elapsed(pid) if pid else None
    if elapsed is None and base.get("started_at"):
        try:
            elapsed = int((now - datetime.fromisoformat(base["started_at"])).total_seconds())
        except ValueError:
            elapsed = None

    result = {
        "pid": pid,
        "elapsed_s": elapsed,
        "transcripts_db": db_have,
        "pending_db": pend,
        "remote_done": remote_done,
        "job_total": job_total,
        "jobs_remaining": max(0, job_total - remote_done),
        "rate_h": None,
        "eta_seconds": None,
        "finish_at": None,
    }

    if elapsed is not None:
        done_in_run = remote_done - int(base.get("remote_baseline", 0))
        done_in_run = max(0, done_in_run)
        if elapsed > 0 and done_in_run > 0:
            rate = done_in_run / elapsed  # transcripts per second
            result["rate_h"] = round(rate * 3600, 2)
            remaining = result["jobs_remaining"]
            if remaining > 0:
                eta = remaining / rate
                result["eta_seconds"] = int(eta)
                result["finish_at"] = (now + timedelta(seconds=eta)).isoformat(timespec="minutes")

    if elapsed is not None:
        elapsed_str = "%dh%dm" % (elapsed // 3600, (elapsed % 3600) // 60)
    else:
        elapsed_str = "-"
    _echo(
        f"drain pid={result['pid']}, elapsed={elapsed_str}, "
        f"rate={result['rate_h'] or '-'}/hr"
    )
    _echo(f"  transcripts in DB: {result['transcripts_db']} / {total_db} total sermons")
    _echo(f"  pending overall: {result['pending_db']}")
    _echo(
        f"  this run: {result['remote_done']}/{result['job_total']} done, "
        f"{result['jobs_remaining']} remaining"
    )
    if result["finish_at"]:
        _echo(f"  ETA finish: {result['finish_at']} (in ~{result['eta_seconds']//3600}h{(result['eta_seconds']%3600)//60}m)")
    else:
        _echo("  ETA: estimating (need the first few transcripts of this run to settle)")
    return result