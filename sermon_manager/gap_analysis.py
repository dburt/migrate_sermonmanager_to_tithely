"""Gap analysis: compare WordPress CSV against Tithely index using audio_file_size as join key."""

import csv
import json


def load_local_sermons(csv_path):
    """Load WordPress sermons from CSV, keyed by audio_file_size."""
    sermons = []
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                row['audio_file_size'] = int(float(row.get('audio_file_size', 0) or 0))
            except (ValueError, TypeError):
                row['audio_file_size'] = 0
            sermons.append(row)
    return sermons


def load_remote_index(json_path):
    """Load Tithely index from JSON."""
    with open(json_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def normalize_field(value):
    """Normalize a field value for comparison."""
    if value is None:
        return ""
    return str(value).strip()


# Fields to compare between WordPress and Tithely
FIELD_MAP = {
    # wordpress_field: tithely_field
    'title': 'title',
    'preacher': 'speaker',
    'sermon_series': 'sermon_series',
    'bible_passage': 'bible_passage',
    'content_text': 'description',
    'audio_url': 'audio_url',
}


def compare_fields(local, remote):
    """Compare mapped fields between a local and remote sermon. Returns dict of diffs."""
    diffs = {}
    for local_key, remote_key in FIELD_MAP.items():
        local_val = normalize_field(local.get(local_key, ''))
        remote_val = normalize_field(remote.get(remote_key, ''))
        if local_val != remote_val:
            diffs[local_key] = {'local': local_val, 'remote': remote_val}
    return diffs


def run_gap_analysis(local_csv_path, remote_index_path):
    """
    Join WordPress sermons with Tithely index on audio_file_size.

    Returns dict with sections:
      matched_correct: list of matched sermons with no field diffs
      matched_with_diffs: list of matched sermons with field diffs
      local_only: in WordPress but not Tithely
      remote_only: on Tithely but not in WordPress
      no_size: audio_file_size is 0 on either side
    """
    local_sermons = load_local_sermons(local_csv_path)
    remote_sermons = load_remote_index(remote_index_path)

    # Build lookup by audio_file_size
    remote_by_size = {}
    remote_no_size = []
    for s in remote_sermons:
        size = int(s.get('audio_file_size', 0) or 0)
        if size == 0:
            remote_no_size.append(s)
        else:
            # Handle duplicates: store as list
            remote_by_size.setdefault(size, []).append(s)

    matched_correct = []
    matched_with_diffs = []
    local_only = []
    local_no_size = []
    matched_remote_sizes = set()

    for local in local_sermons:
        size = local['audio_file_size']
        if size == 0:
            local_no_size.append({
                'source': 'local',
                'title': local.get('title', ''),
                'audio_url': local.get('audio_url', ''),
            })
            continue

        remotes = remote_by_size.get(size)
        if not remotes:
            local_only.append({
                'title': local.get('title', ''),
                'preacher': local.get('preacher', ''),
                'sermon_series': local.get('sermon_series', ''),
                'bible_passage': local.get('bible_passage', ''),
                'content_text': local.get('content_text', ''),
                'audio_url': local.get('audio_url', ''),
                'audio_file_size': size,
                'post_date_gmt': local.get('post_date_gmt', ''),
            })
            continue

        # Match with first remote (should be unique by size)
        remote = remotes[0]
        matched_remote_sizes.add(size)

        diffs = compare_fields(local, remote)
        entry = {
            'audio_file_size': size,
            'local_title': local.get('title', ''),
            'remote_title': remote.get('title', ''),
            'remote_slug': remote.get('slug', ''),
        }
        if diffs:
            entry['diffs'] = diffs
            matched_with_diffs.append(entry)
        else:
            matched_correct.append(entry)

    # Find remote-only (on Tithely but not matched)
    remote_only = []
    for size, remotes in remote_by_size.items():
        if size not in matched_remote_sizes:
            for r in remotes:
                remote_only.append({
                    'slug': r.get('slug', ''),
                    'title': r.get('title', ''),
                    'speaker': r.get('speaker', ''),
                    'audio_file_size': size,
                    'audio_url': r.get('audio_url', ''),
                })

    no_size = local_no_size + [{'source': 'remote', **s} for s in remote_no_size]

    return {
        'matched_correct': matched_correct,
        'matched_with_diffs': matched_with_diffs,
        'local_only': local_only,
        'remote_only': remote_only,
        'no_size': no_size,
        'summary': {
            'total_local': len(local_sermons),
            'total_remote': len(remote_sermons),
            'matched_correct': len(matched_correct),
            'matched_with_diffs': len(matched_with_diffs),
            'local_only': len(local_only),
            'remote_only': len(remote_only),
            'no_size': len(no_size),
        }
    }


def format_summary(report):
    """Format a human-readable summary from a gap analysis report."""
    s = report['summary']
    lines = [
        "=== Gap Analysis Summary ===",
        f"Local (WordPress):     {s['total_local']}",
        f"Remote (Tithely):      {s['total_remote']}",
        "",
        f"Matched (correct):     {s['matched_correct']}",
        f"Matched (with diffs):  {s['matched_with_diffs']}",
        f"Local-only (missing):  {s['local_only']}",
        f"Remote-only (extra):   {s['remote_only']}",
        f"No audio_file_size:    {s['no_size']}",
    ]

    if report['matched_with_diffs']:
        # Count diffs by field
        field_counts = {}
        for entry in report['matched_with_diffs']:
            for field in entry.get('diffs', {}):
                field_counts[field] = field_counts.get(field, 0) + 1
        lines.append("")
        lines.append("--- Diff Breakdown by Field ---")
        for field, count in sorted(field_counts.items(), key=lambda x: -x[1]):
            lines.append(f"  {field}: {count}")

    return "\n".join(lines)


def prepare_updates(report, fields=None):
    """
    Generate update payloads from matched_with_diffs section.

    Args:
        report: gap analysis report dict
        fields: optional list of field names to include (e.g. ['title', 'preacher']).
                If None, includes all differing fields.

    Returns list of {slug, updates: {field: new_value}} dicts.
    """
    updates = []
    for entry in report.get('matched_with_diffs', []):
        slug = entry.get('remote_slug')
        if not slug:
            continue

        payload = {}
        for local_key, diff in entry.get('diffs', {}).items():
            if fields and local_key not in fields:
                continue
            payload[local_key] = diff['local']  # WordPress is source of truth

        if payload:
            updates.append({
                'slug': slug,
                'audio_file_size': entry['audio_file_size'],
                'updates': payload,
            })

    return updates


def prepare_creates(report):
    """
    Generate create payloads from local_only section.

    Returns list of sermon data dicts ready for Tithely creation.
    """
    creates = []
    for entry in report.get('local_only', []):
        creates.append({
            'title': entry.get('title', ''),
            'preacher': entry.get('preacher', ''),
            'sermon_series': entry.get('sermon_series', ''),
            'bible_passage': entry.get('bible_passage', ''),
            'description': entry.get('content_text', ''),
            'audio_url': entry.get('audio_url', ''),
            'audio_file_size': entry.get('audio_file_size', 0),
            'date': entry.get('post_date_gmt', ''),
        })
    return creates
