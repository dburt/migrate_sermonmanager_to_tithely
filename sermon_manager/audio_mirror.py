"""Audio mirror tooling: download and organize sermon audio files."""

import json
import os
import re
import subprocess
import requests
from pathlib import Path


def sanitize_filename(name):
    """Sanitize a string for use as a filename."""
    name = re.sub(r'[^\w\s\-.]', '', name)
    name = re.sub(r'\s+', '-', name.strip())
    return name.lower()


def download_audio(url, output_dir, filename=None, _echo=print):
    """
    Download a single audio file.

    Args:
        url: URL to download
        output_dir: directory to save to
        filename: optional filename override (default: derived from URL)
        _echo: output function

    Returns dict with {url, path, size, success, error}
    """
    os.makedirs(output_dir, exist_ok=True)

    if not filename:
        filename = url.split('/')[-1].split('?')[0]
        if not filename:
            filename = 'unknown_audio.mp3'

    output_path = os.path.join(output_dir, filename)

    # Skip if already downloaded
    if os.path.exists(output_path):
        existing_size = os.path.getsize(output_path)
        _echo(f"Already exists: {filename} ({existing_size} bytes)")
        return {
            'url': url,
            'path': output_path,
            'size': existing_size,
            'success': True,
            'skipped': True,
        }

    try:
        _echo(f"Downloading: {filename}...")
        response = requests.get(url, stream=True, timeout=60)
        response.raise_for_status()

        total_size = int(response.headers.get('Content-Length', 0))
        downloaded = 0

        with open(output_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
                downloaded += len(chunk)

        _echo(f"Downloaded: {filename} ({downloaded} bytes)")
        return {
            'url': url,
            'path': output_path,
            'size': downloaded,
            'expected_size': total_size,
            'success': True,
            'skipped': False,
        }

    except Exception as e:
        _echo(f"Error downloading {url}: {e}")
        # Clean up partial download
        if os.path.exists(output_path):
            os.remove(output_path)
        return {
            'url': url,
            'path': output_path,
            'size': 0,
            'success': False,
            'error': str(e),
        }


def load_manifest(manifest_path):
    """Load the mirror manifest tracking download progress."""
    if os.path.exists(manifest_path):
        with open(manifest_path, 'r') as f:
            return json.load(f)
    return {'downloads': {}, 'total_size': 0}


def save_manifest(manifest, manifest_path):
    """Save the mirror manifest."""
    with open(manifest_path, 'w') as f:
        json.dump(manifest, f, indent=2)


def mirror_audio(index_path, output_dir, dry_run=False, resume=True, _echo=print):
    """
    Batch download all audio files from an index.

    Args:
        index_path: path to JSON index file (must have audio_url per entry)
        output_dir: directory to save files
        dry_run: if True, just report what would be downloaded
        resume: if True, skip already downloaded files
        _echo: output function

    Returns summary dict.
    """
    with open(index_path, 'r') as f:
        index = json.load(f)

    manifest_path = os.path.join(output_dir, 'mirror_manifest.json')
    manifest = load_manifest(manifest_path) if resume else {'downloads': {}, 'total_size': 0}

    to_download = []
    already_done = 0
    total_estimated_size = 0

    for entry in index:
        url = entry.get('audio_url', '')
        if not url or not url.startswith('http'):
            continue

        size = int(entry.get('audio_file_size', 0) or 0)
        total_estimated_size += size

        if resume and url in manifest['downloads'] and manifest['downloads'][url].get('success'):
            already_done += 1
            continue

        to_download.append(entry)

    if dry_run:
        _echo(f"=== Mirror Dry Run ===")
        _echo(f"Total sermons with audio: {len(to_download) + already_done}")
        _echo(f"Already downloaded: {already_done}")
        _echo(f"To download: {len(to_download)}")
        _echo(f"Estimated total size: {total_estimated_size / (1024**3):.2f} GB")

        # Check URL accessibility for a sample
        sample_size = min(5, len(to_download))
        if sample_size > 0:
            _echo(f"\nChecking accessibility of {sample_size} sample URLs...")
            for entry in to_download[:sample_size]:
                url = entry.get('audio_url', '')
                try:
                    resp = requests.head(url, timeout=10, allow_redirects=True)
                    _echo(f"  {resp.status_code} - {entry.get('title', url)}")
                except Exception as e:
                    _echo(f"  ERROR - {entry.get('title', url)}: {e}")

        return {
            'total': len(to_download) + already_done,
            'already_done': already_done,
            'to_download': len(to_download),
            'estimated_size_gb': total_estimated_size / (1024**3),
        }

    # Actual download
    os.makedirs(output_dir, exist_ok=True)
    succeeded = 0
    failed = 0

    for i, entry in enumerate(to_download, 1):
        url = entry.get('audio_url', '')
        slug = entry.get('slug', '')
        title = entry.get('title', '')

        # Build filename from slug or title
        if slug:
            filename = f"{slug}.mp3"
        elif title:
            filename = f"{sanitize_filename(title)}.mp3"
        else:
            filename = url.split('/')[-1].split('?')[0]

        _echo(f"[{i}/{len(to_download)}] {title or slug}")
        result = download_audio(url, output_dir, filename=filename, _echo=_echo)

        manifest['downloads'][url] = result
        if result['success']:
            succeeded += 1
            manifest['total_size'] += result.get('size', 0)
        else:
            failed += 1

        # Save manifest periodically
        if i % 10 == 0:
            save_manifest(manifest, manifest_path)

    save_manifest(manifest, manifest_path)

    summary = {
        'total': len(to_download),
        'succeeded': succeeded,
        'failed': failed,
        'already_done': already_done,
        'total_size_bytes': manifest['total_size'],
    }
    _echo(f"\n=== Mirror Complete ===")
    _echo(f"Downloaded: {succeeded}, Failed: {failed}, Skipped: {already_done}")
    return summary


# --- rclone (streaming) mirror --------------------------------------------------------

def remote_file_size(rclone_remote):
    """Return size (bytes) of a remote file via rclone, or None if absent/error."""
    try:
        proc = subprocess.run(
            ['rclone', 'size', rclone_remote, '--json'],
            capture_output=True, text=True, timeout=60,
        )
        if proc.returncode == 0:
            import json as _json
            info = _json.loads(proc.stdout)
            return int(info.get('bytes', 0))
    except Exception:
        pass
    return None


def stream_to_rclone(url, rclone_target, expected_size=None, _echo=print):
    """
    Stream a URL into an rclone remote path without touching local disk.

    Skips (returns 'skipped') when the remote file already exists with the
    expected size. Returns 'ok', 'skipped', or raises on failure.
    """
    if expected_size:
        existing = remote_file_size(rclone_target)
        if existing is not None and existing == expected_size:
            _echo(f"  Already on remote: {rclone_target} ({existing} bytes)")
            return 'skipped'

    _echo(f"  Streaming {url} -> {rclone_target} ...")
    response = requests.get(url, stream=True, timeout=60)
    response.raise_for_status()

    proc = subprocess.Popen(
        ['rclone', 'rcat', rclone_target],
        stdin=subprocess.PIPE,
    )
    try:
        for chunk in response.iter_content(chunk_size=1024 * 1024):
            if chunk:
                proc.stdin.write(chunk)
    finally:
        proc.stdin.close()
        response.close()
    proc.wait()

    if proc.returncode != 0:
        raise RuntimeError(f"rclone rcat failed with exit code {proc.returncode} for {rclone_target}")
    return 'ok'


def mirror_audio_db(conn, rclone_remote='hyperion:/D:/stalfreds_audio', dry_run=False, _echo=print):
    """
    Mirror audio for sermons in the DB that lack a local audio path.

    Each file is streamed straight from its CDN URL into the rclone remote
    (no local disk usage). Successful transfers record local_audio_path.
    Returns a summary dict.
    """
    from db import get_pending_audio, record_local_audio

    if rclone_remote.endswith('/'):
        rclone_remote = rclone_remote[:-1]

    pending = get_pending_audio(conn)
    if not pending:
        _echo("No sermon audio pending mirror.")
        return {'total': 0, 'ok': 0, 'skipped': 0, 'failed': 0}

    _echo(f"=== Audio Mirror to {rclone_remote} ===")
    _echo(f"{len(pending)} sermons pending audio.")

    ok_count = skipped_count = failed_count = unavailable_count = 0
    for i, s in enumerate(pending, 1):
        url = s.get('audio_url') or ''
        slug = s.get('slug') or ''
        if not url or not slug:
            _echo(f"[{i}/{len(pending)}] SKIP (no audio_url/slug): {s.get('title', '?')}")
            unavailable_count += 1
            continue

        target = f"{rclone_remote}/{slug}.mp3"
        title = s.get('title') or slug
        _echo(f"[{i}/{len(pending)}] {title}")

        if dry_run:
            _echo(f"  DRY RUN: would stream {url} -> {target}")
            ok_count += 1
            continue

        try:
            status = stream_to_rclone(url, target, expected_size=s.get('audio_file_size') or None, _echo=_echo)
            if status == 'ok':
                record_local_audio(conn, slug, target)
                ok_count += 1
            else:
                skipped_count += 1
        except Exception as e:
            _echo(f"  ERROR: {e}")
            failed_count += 1

    summary = {
        'total': len(pending),
        'ok': ok_count,
        'skipped': skipped_count,
        'failed': failed_count,
        'unavailable': unavailable_count,
    }
    _echo(f"\n=== Audio Mirror Complete ===")
    _echo(f"Streamed: {ok_count}, Already present: {skipped_count}, Failed: {failed_count}, No audio: {unavailable_count}")
    return summary
