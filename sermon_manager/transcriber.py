"""Sermon transcription pipeline (faster-whisper) wired into the local DB.

For each sermon lacking a transcript, audio is sourced from the rclone audio
mirror (local_audio_path, when the mirror has run) or the CDN URL, transcribed
with faster-whisper, and stored in `transcriptions` attached to whichever source
owns the sermon. FTS is refreshed afterwards so transcript text is searchable.
"""

import os
import subprocess
import tempfile


def _initial_prompt(sermon):
    """Build a faster-whisper initial prompt from metadata + NIV passage text."""
    from bible_prompt import build_sermon_prompt
    return build_sermon_prompt(sermon)


def _fetch_audio(sermon, dest_path, _echo=print):
    """Write a sermon's audio to dest_path, from rclone mirror or CDN URL."""
    local = (sermon.get('local_audio_path') or '').strip()
    url = (sermon.get('audio_url') or '').strip()

    if local:
        _echo(f"  Reading audio from mirror: {local}")
        with open(dest_path, 'wb') as f:
            subprocess.run(['rclone', 'cat', local], check=True, stdout=f)
        return

    if url:
        _echo(f"  Downloading audio from CDN")
        subprocess.run(
            ['curl', '-L', '-sS', '--fail', '-o', dest_path, url],
            check=True,
        )
        return

    raise ValueError("No audio source (local_audio_path or audio_url) available")


def transcribe_missing(conn, model_name='medium', device='cpu', compute_type='int8',
                       language='en', limit=None, title_filter=None, _echo=print):
    """Transcribe sermons lacking a transcription and store them in the DB.

    Returns a summary dict {total, ok, failed, words}.
    """
    from db import add_transcription, get_pending_transcriptions, refresh_fts

    pending = get_pending_transcriptions(conn)
    if title_filter:
        pending = [s for s in pending if (s.get('title') or '').lower() == title_filter.lower()]
        if not pending:
            _echo(f"No pending sermon with title '{title_filter}'.")
            return {'total': 0, 'ok': 0, 'failed': 0, 'words': 0}
    if limit:
        pending = pending[:limit]

    if not pending:
        _echo("No sermons pending transcription.")
        return {'total': 0, 'ok': 0, 'failed': 0, 'words': 0}

    _echo(f"=== Transcribing {len(pending)} sermon(s) with faster-whisper ({model_name}) ===")

    model = None
    ok = failed = words = 0
    with tempfile.TemporaryDirectory(prefix='sermon_audio_') as tmpdir:
        for i, s in enumerate(pending, 1):
            title = s.get('title') or '?'
            _echo(f"[{i}/{len(pending)}] {title}")
            try:
                tmp_path = os.path.join(tmpdir, f"audio_{i}.mp3")
                _fetch_audio(s, tmp_path, _echo=_echo)

                if model is None:
                    _echo("  Loading faster-whisper model...")
                    from faster_whisper import WhisperModel
                    model = WhisperModel(model_name, device=device, compute_type=compute_type)

                _echo("  Transcribing...")
                segments, _ = model.transcribe(
                    tmp_path, beam_size=5, language=language, initial_prompt=_initial_prompt(s)
                )
                text = "\n".join(seg.text.strip() for seg in segments).strip()

                if s.get('tithely_sermon_id'):
                    add_transcription(conn, text, tithely_sermon_id=s['tithely_sermon_id'])
                elif s.get('wordpress_sermon_id'):
                    add_transcription(conn, text, wordpress_sermon_id=s['wordpress_sermon_id'])
                else:
                    raise ValueError("Sermon has no source id; cannot attach transcription")

                n = len(text.split())
                words += n
                _echo(f"  Stored transcription ({n} words)")
                ok += 1
            except Exception as e:
                _echo(f"  ERROR: {e}")
                failed += 1

    n = refresh_fts(conn)
    summary = {'total': len(pending), 'ok': ok, 'failed': failed, 'words': words}
    _echo(f"=== Transcription Complete: {ok} ok, {failed} failed. FTS refreshed ({n} rows). ===")
    return summary