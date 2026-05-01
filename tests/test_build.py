import pytest
from build import extract_callouts, render_md

def test_extract_single_tip():
    text = "> [!TIP]\n> This is a tip.\n> Second line."
    processed, mapping = extract_callouts(text)
    assert len(mapping) == 1
    key = list(mapping.keys())[0]
    assert key in processed
    type_key, content = mapping[key]
    assert type_key == "TIP"
    assert "This is a tip." in content
    assert "Second line." in content

def test_extract_multiple_callouts():
    text = "> [!TIP]\n> Tip content.\n\nSome text.\n\n> [!WARN]\n> Warning here."
    _, mapping = extract_callouts(text)
    types = [v[0] for v in mapping.values()]
    assert "TIP" in types
    assert "WARN" in types

def test_unknown_callout_type_left_unchanged():
    text = "> [!UNKNOWN]\n> Some text."
    processed, mapping = extract_callouts(text)
    assert len(mapping) == 0
    assert "> [!UNKNOWN]" in processed

def test_render_md_callout_produces_div():
    text = "> [!TIP]\n> Remember this."
    html = render_md(text)
    assert 'class="callout callout-tip"' in html
    assert "💡 Tip" in html
    assert "Remember this." in html

def test_render_md_callout_try():
    html = render_md("> [!TRY]\n> Open your terminal.")
    assert 'callout-try' in html
    assert "⚡ Try It" in html

def test_render_md_callout_warn():
    html = render_md("> [!WARN]\n> Do not delete.")
    assert 'callout-warn' in html
    assert "⚠️ Watch Out" in html

def test_render_md_callout_note():
    html = render_md("> [!NOTE]\n> Field-specific insight.")
    assert 'callout-note' in html
    assert "🔬 Research Note" in html

def test_render_md_preserves_surrounding_content():
    text = "# Heading\n\n> [!TIP]\n> A tip.\n\nNormal paragraph."
    html = render_md(text)
    assert "<h1" in html
    assert "Normal paragraph" in html
    assert "callout-tip" in html
