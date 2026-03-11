"""Offline tests for modules that don't require a browser or network."""

import csv
import json
import os
import shutil
import tempfile

import sys
sys.path.insert(0, os.path.dirname(__file__))

from gap_analysis import (
    run_gap_analysis,
    format_summary,
    prepare_updates,
    prepare_creates,
    normalize_field,
)
from audio_mirror import sanitize_filename, load_manifest, save_manifest


# --- Helpers ---

def make_local_csv(rows):
    f = tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False)
    fields = ['title', 'preacher', 'sermon_series', 'bible_passage',
              'content_text', 'audio_url', 'audio_file_size', 'post_date_gmt']
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()
    for row in rows:
        writer.writerow(row)
    f.close()
    return f.name


def make_remote_json(entries):
    f = tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False)
    json.dump(entries, f)
    f.close()
    return f.name


# --- Gap Analysis Tests ---

def test_gap_analysis_basic():
    local_path = make_local_csv([
        {'title': 'Sermon A', 'preacher': 'John', 'sermon_series': 'Series 1',
         'bible_passage': 'Gen 1:1', 'content_text': 'Desc A',
         'audio_url': 'http://a.mp3', 'audio_file_size': '12345', 'post_date_gmt': '2020-01-01'},
        {'title': 'Sermon B', 'preacher': 'Jane', 'sermon_series': 'Series 2',
         'bible_passage': 'Gen 2:1', 'content_text': 'Desc B',
         'audio_url': 'http://b.mp3', 'audio_file_size': '67890', 'post_date_gmt': '2020-02-01'},
        {'title': 'Sermon C', 'preacher': 'Bob', 'sermon_series': '', 'bible_passage': '',
         'content_text': '', 'audio_url': 'http://c.mp3', 'audio_file_size': '11111',
         'post_date_gmt': '2020-03-01'},
        {'title': 'No Size', 'preacher': 'X', 'sermon_series': '', 'bible_passage': '',
         'content_text': '', 'audio_url': 'http://d.mp3', 'audio_file_size': '0',
         'post_date_gmt': ''},
    ])
    remote_path = make_remote_json([
        {'slug': 'sermon-a', 'title': 'Sermon A', 'speaker': 'John', 'series': 'Series 1',
         'passage': 'Gen 1:1', 'description': 'Desc A', 'audio_url': 'http://a.mp3',
         'audio_file_size': 12345},
        {'slug': 'sermon-b', 'title': 'WRONG TITLE', 'speaker': 'Wrong Speaker',
         'series': 'Series 2', 'passage': 'Gen 2:1', 'description': 'Desc B',
         'audio_url': 'http://b.mp3', 'audio_file_size': 67890},
        {'slug': 'extra-sermon', 'title': 'Extra', 'speaker': 'Nobody', 'series': '',
         'passage': '', 'description': '', 'audio_url': 'http://e.mp3',
         'audio_file_size': 99999},
    ])

    try:
        report = run_gap_analysis(local_path, remote_path)
        s = report['summary']
        assert s['matched_correct'] == 1, f"expected 1 correct, got {s['matched_correct']}"
        assert s['matched_with_diffs'] == 1, f"expected 1 diff, got {s['matched_with_diffs']}"
        assert s['local_only'] == 1, f"expected 1 local-only, got {s['local_only']}"
        assert s['remote_only'] == 1, f"expected 1 remote-only, got {s['remote_only']}"
        assert s['no_size'] == 1, f"expected 1 no-size, got {s['no_size']}"
    finally:
        os.unlink(local_path)
        os.unlink(remote_path)


def test_prepare_updates():
    local_path = make_local_csv([
        {'title': 'Correct Title', 'preacher': 'Jane', 'sermon_series': 'S',
         'bible_passage': '', 'content_text': '', 'audio_url': 'http://b.mp3',
         'audio_file_size': '67890', 'post_date_gmt': ''},
    ])
    remote_path = make_remote_json([
        {'slug': 'sermon-b', 'title': 'WRONG', 'speaker': 'Wrong', 'series': 'S',
         'passage': '', 'description': '', 'audio_url': 'http://b.mp3',
         'audio_file_size': 67890},
    ])

    try:
        report = run_gap_analysis(local_path, remote_path)
        updates = prepare_updates(report)
        assert len(updates) == 1
        assert updates[0]['slug'] == 'sermon-b'
        assert updates[0]['updates']['title'] == 'Correct Title'
        assert updates[0]['updates']['preacher'] == 'Jane'

        # Filter to single field
        updates_title = prepare_updates(report, fields=['title'])
        assert len(updates_title) == 1
        assert list(updates_title[0]['updates'].keys()) == ['title']
    finally:
        os.unlink(local_path)
        os.unlink(remote_path)


def test_prepare_creates():
    local_path = make_local_csv([
        {'title': 'New Sermon', 'preacher': 'Bob', 'sermon_series': '', 'bible_passage': '',
         'content_text': 'A description', 'audio_url': 'http://c.mp3',
         'audio_file_size': '11111', 'post_date_gmt': '2020-03-01'},
    ])
    remote_path = make_remote_json([])

    try:
        report = run_gap_analysis(local_path, remote_path)
        creates = prepare_creates(report)
        assert len(creates) == 1
        assert creates[0]['title'] == 'New Sermon'
        assert creates[0]['description'] == 'A description'
    finally:
        os.unlink(local_path)
        os.unlink(remote_path)


def test_format_summary():
    local_path = make_local_csv([
        {'title': 'A', 'preacher': '', 'sermon_series': '', 'bible_passage': '',
         'content_text': '', 'audio_url': 'http://a.mp3', 'audio_file_size': '100',
         'post_date_gmt': ''},
    ])
    remote_path = make_remote_json([
        {'slug': 'a', 'title': 'A', 'speaker': '', 'series': '', 'passage': '',
         'description': '', 'audio_url': 'http://a.mp3', 'audio_file_size': 100},
    ])

    try:
        report = run_gap_analysis(local_path, remote_path)
        summary = format_summary(report)
        assert 'Matched (correct):     1' in summary
        assert 'Local-only (missing):  0' in summary
    finally:
        os.unlink(local_path)
        os.unlink(remote_path)


def test_normalize_field():
    assert normalize_field(None) == ""
    assert normalize_field("  hello  ") == "hello"
    assert normalize_field(42) == "42"


# --- Audio Mirror Tests ---

def test_sanitize_filename():
    assert sanitize_filename('Sermon Title! (Part 1)') == 'sermon-title-part-1'
    assert sanitize_filename('  spaces  ') == 'spaces'
    assert sanitize_filename('') == ''


def test_manifest_round_trip():
    td = tempfile.mkdtemp()
    try:
        mp = os.path.join(td, 'manifest.json')
        assert load_manifest(mp) == {'downloads': {}, 'total_size': 0}

        m = {'downloads': {'http://x': {'success': True}}, 'total_size': 100}
        save_manifest(m, mp)
        assert load_manifest(mp) == m
    finally:
        shutil.rmtree(td)


# --- Runner ---

if __name__ == '__main__':
    tests = [v for k, v in sorted(globals().items()) if k.startswith('test_')]
    passed = failed = 0
    for test in tests:
        try:
            test()
            print(f"  PASS  {test.__name__}")
            passed += 1
        except Exception as e:
            print(f"  FAIL  {test.__name__}: {e}")
            failed += 1
    print(f"\n{passed} passed, {failed} failed")
    raise SystemExit(1 if failed else 0)
