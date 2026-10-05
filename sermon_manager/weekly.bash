#!/bin/bash
# Weekly St Alfred's pipeline (cron entry point).
#
# Order matters:
#   1. sync      - pull any new sermons from live Tithely into the DB
#   2. mirror    - stream new sermon audio to the Hyperion mirror (D:)
#   3. transcribe - top up transcriptions for anything new (GPU worker on Hyperion)
#   4. deploy    - re-export static assets (sermons.json, transcripts/*) and rsync to the site
#
# Safe to run any time: every step is idempotent/skippable, and transcribe-remote
# only queues sermons whose audio is already mirrored. Runs at its own pace (a
# large backlog after a long break may keep the transcription step busy for days).
#
# Suggested crontab (weekly, e.g. Sunday 3am):
#   0 3 * * 0  /home/akash/projects/stalfreds_podcast/sermon_manager/weekly.bash
#
# Output goes to logs/weekly-<timestamp>.log; non-zero exit on any failing stage.

set -uo pipefail

cd "$(dirname "$0")/.." || exit 1

# mise-managed toolchain; shims aren't on PATH in cron.
MISE_SHIMS="$HOME/.local/share/mise/shims"
[ -d "$MISE_SHIMS" ] && export PATH="$MISE_SHIMS:$PATH"

PY="uv run python"
TS=$(date +%Y%m%d-%H%M%S)
LOG="logs/weekly-$TS.log"
mkdir -p logs

# Every stage's output is redirected into $LOG below, so cron's own capture
# would otherwise stay empty and failures would be silent.
trap 'echo "weekly pipeline exited rc=$? (full log: $LOG)" >&2' EXIT

{
    echo "=== St Alfred's weekly pipeline started: $(date -u +%Y-%m-%dT%H:%M:%SZ) ==="
    echo "[1/4] sync ..."
    if ! $PY sermon_manager/sermon_manager.py sync; then
        echo "STAGE FAILED: sync"; exit 1
    fi
    echo "[2/4] audio mirror ..."
    if ! $PY sermon_manager/sermon_manager.py mirror-audio-db; then
        echo "STAGE FAILED: mirror-audio-db"; exit 1
    fi
    echo "[3/4] transcribe-remote ..."
    if ! $PY sermon_manager/sermon_manager.py transcribe-remote; then
        echo "STAGE FAILED: transcribe-remote"; exit 1
    fi
    echo "[4/4] export + deploy ..."
    if ! bash sermon-archive/deploy.bash; then
        echo "STAGE FAILED: deploy"; exit 1
    fi
    echo "=== pipeline complete: $(date -u +%Y-%m-%dT%H:%M:%SZ) ==="
} >> "$LOG" 2>&1

exit $?