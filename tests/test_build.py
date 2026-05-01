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

from build import parse_quiz

SAMPLE_QUIZ = """## Q1

What does CC stand for?

- [ ] Cloud Computing
- [x] Claude Code
- [ ] Code Compiler
- [ ] Custom CLI

> CC always refers to Claude Code in this tutorial.

---

## Think

Describe one way CC is better than copy-pasting from Claude.ai.

<answer>
CC can read your files directly — no copy-pasting needed.
</answer>
"""

def test_parse_quiz_finds_mcq():
    questions = parse_quiz(SAMPLE_QUIZ)
    mcqs = [q for q in questions if q["type"] == "mcq"]
    assert len(mcqs) == 1

def test_parse_quiz_mcq_fields():
    questions = parse_quiz(SAMPLE_QUIZ)
    mcq = [q for q in questions if q["type"] == "mcq"][0]
    assert "What does CC stand for?" in mcq["question"]
    assert len(mcq["options"]) == 4
    correct = [o for o in mcq["options"] if o["correct"]]
    assert len(correct) == 1
    assert "Claude Code" in correct[0]["text"]
    assert "CC always refers" in mcq["explanation"]

def test_parse_quiz_finds_thinking():
    questions = parse_quiz(SAMPLE_QUIZ)
    thinking = [q for q in questions if q["type"] == "think"]
    assert len(thinking) == 1

def test_parse_quiz_thinking_fields():
    questions = parse_quiz(SAMPLE_QUIZ)
    think = [q for q in questions if q["type"] == "think"][0]
    assert "Describe one way" in think["question"]
    assert "read your files directly" in think["answer"]
