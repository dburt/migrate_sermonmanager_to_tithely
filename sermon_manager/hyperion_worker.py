"""GPU transcription worker for St Alfred's sermons (runs on Hyperion).

Reads meta.json (written by 'sermon_manager.py transcribe-remote' on the Linux
side) from D:\\stalfreds_transcribe, transcribes audio files that lack a
transcript, and writes them to D:\\stalfreds_transcribe\\transcripts\\<slug>.txt.

Idempotent and resumable: already-transcribed slugs are skipped each run, so the
orchestrator can invoke this repeatedly with small --limit batches.
"""

import argparse
import json
import os
import sys
from pathlib import Path

BASE = Path(r"D:\stalfreds_transcribe")
META = BASE / "meta.json"
OUT_DIR = BASE / "transcripts"
AUDIO_DIR = r"D:\stalfreds_audio"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=10, help="Max sermons per run.")
    ap.add_argument("--model", default=None, help="Overrides model from meta.json.")
    args = ap.parse_args()

    if not META.exists():
        print("meta.json not found - nothing to do")
        return 0

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    meta = json.loads(META.read_text(encoding="utf-8"))
    model_name = args.model or meta.get("model", "medium")
    audio_dir = meta.get("audio_dir", AUDIO_DIR)

    done = {p.stem for p in OUT_DIR.glob("*.txt")}
    jobs = [j for j in meta.get("jobs", []) if j.get("slug") not in done][: args.limit]
    if not jobs:
        print("no pending transcriptions")
        return 0

    print(f"GPU worker: {len(jobs)} jobs, model={model_name}")
    sys.stdout.flush()

    os.environ.setdefault("CUDA_VISIBLE_DEVICES", "0")
    from faster_whisper import WhisperModel

    model = WhisperModel(model_name, device="cuda", compute_type="auto")
    print("model loaded on cuda")
    sys.stdout.flush()

    for i, j in enumerate(jobs, 1):
        slug = j.get("slug")
        if not slug:
            continue
        out = OUT_DIR / (slug + ".txt")
        if out.exists():
            continue
        audio = os.path.join(audio_dir, j.get("audio") or (slug + ".mp3"))
        if not os.path.exists(audio):
            print(f"[{i}/{len(jobs)}] MISSING audio: {audio}")
            sys.stdout.flush()
            continue
        print(f"[{i}/{len(jobs)}] {slug}")
        sys.stdout.flush()
        try:
            prompt = j.get("prompt") or ""
            segs, _ = model.transcribe(
                audio, beam_size=5, language="en",
                initial_prompt=prompt if prompt else None,
            )
            text = " ".join(s.text.strip() for s in segs).strip()
            out.write_text(text, encoding="utf-8")
            print(f"  done ({len(text.split())} words)")
            sys.stdout.flush()
        except Exception as e:
            print(f"  FAILED: {e}")
            sys.stdout.flush()

    print("worker finished")
    return 0


if __name__ == "__main__":
    sys.exit(main())