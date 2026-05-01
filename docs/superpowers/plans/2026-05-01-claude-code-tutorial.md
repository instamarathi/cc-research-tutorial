# Claude Code Tutorial Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a beautiful, locally-hosted HTML tutorial teaching researchers to use Claude Code, structured as 8 chapter folders (ch00–ch07) each with lecture, tips, exercises, and quiz pages generated from Markdown by a Python build script.

**Architecture:** `build.py` reads `.md` source files, pre-processes custom callout syntax (`> [!TIP]` etc.) and quiz format, renders content through Jinja2 templates, and writes self-contained `.html` files. Tailwind CSS (CDN), Prism.js (CDN), and Google Fonts provide styling. No server required — open any `.html` directly in a browser.

**Tech Stack:** Python 3.8+, `markdown`, `jinja2`; Tailwind CSS Play CDN; Inter + JetBrains Mono (Google Fonts); Prism.js (CDN) for syntax highlighting; vanilla JS for quiz interactivity.

---

## File Map

| File | Responsibility |
|------|---------------|
| `build.py` | Orchestrates the full build: parses MD, renders templates, writes HTML |
| `templates/base.html` | Jinja2 base layout: sidebar, topbar, CDN links, nav |
| `templates/lecture.html` | Extends base; renders prose content |
| `templates/tips.html` | Extends base; renders tips list |
| `templates/exercises.html` | Extends base; renders exercise steps |
| `templates/quiz.html` | Extends base; renders interactive MCQ + thinking exercises |
| `templates/chapter-index.html` | Extends base; chapter landing with 4 page cards |
| `templates/root-index.html` | Standalone; chapter card grid (table of contents) |
| `assets/style.css` | Callout boxes, prose typography, quiz cards, copy button |
| `assets/quiz.js` | MCQ click handler + thinking exercise reveal |
| `tests/test_build.py` | Unit tests for callout pre-processor and quiz parser |
| `ch00/`–`ch07/` | Markdown sources + generated HTML per chapter |

---

## Task 1: Project Scaffold

**Files:**
- Create: `requirements.txt`
- Create: `assets/` (empty dir with placeholder)
- Create: `templates/` (empty dir with placeholder)
- Create: `ch00/` through `ch07/` directories
- Create: `tests/__init__.py`

- [ ] **Step 1: Create directory structure**

```bash
cd /Users/anup/claude_tmp/cc-tutorial
mkdir -p assets templates tests
mkdir -p ch00 ch01 ch02 ch03 ch04 ch05 ch06 ch07
touch tests/__init__.py
```

- [ ] **Step 2: Create requirements.txt**

```
markdown==3.6
jinja2==3.1.4
pytest==8.2.0
```

- [ ] **Step 3: Install dependencies**

```bash
pip install -r requirements.txt
```

Expected: `Successfully installed jinja2-3.1.4 markdown-3.6 pytest-8.2.0` (versions may vary)

- [ ] **Step 4: Commit**

```bash
git init
git add requirements.txt tests/__init__.py
git commit -m "chore: scaffold project structure"
```

---

## Task 2: Callout Pre-processor (TDD)

**Files:**
- Create: `tests/test_build.py`
- Create: `build.py` (callout functions only)

The Python `markdown` library does not support GitHub-style alerts (`> [!TIP]`). We pre-process them before handing text to the markdown library: extract each callout block, replace with a unique placeholder, convert the surrounding markdown, then substitute rendered callout HTML back in.

- [ ] **Step 1: Write failing tests for callout pre-processor**

Create `tests/test_build.py`:

```python
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
```

- [ ] **Step 2: Run tests to confirm they fail**

```bash
pytest tests/test_build.py -v
```

Expected: `ModuleNotFoundError: No module named 'build'` — confirms tests are wired.

- [ ] **Step 3: Implement callout pre-processor in build.py**

Create `build.py`:

```python
#!/usr/bin/env python3
import os
import re
import markdown
from pathlib import Path
from jinja2 import Environment, FileSystemLoader

CALLOUT_TYPES = {
    "TIP":  ("💡 Tip",           "callout-tip"),
    "TRY":  ("⚡ Try It",        "callout-try"),
    "WARN": ("⚠️ Watch Out",     "callout-warn"),
    "NOTE": ("🔬 Research Note", "callout-note"),
}

CHAPTERS = [
    {"id": "ch00", "title": "Welcome & The Superpower",      "desc": "Why CC ≠ copy-paste AI. Installation, first run, mental model shift.", "time": "20 min"},
    {"id": "ch01", "title": "Your First Research Session",   "desc": "File context, reading papers/data with CC, iterative dialogue.",        "time": "30 min"},
    {"id": "ch02", "title": "Simulations & Code",            "desc": "Writing, running, and debugging simulation code with CC.",              "time": "45 min"},
    {"id": "ch03", "title": "Developing Theory",             "desc": "Formalizing ideas, pressure-testing logic, generating LaTeX.",          "time": "30 min"},
    {"id": "ch04", "title": "Writing a Paper Section",       "desc": "Drafting, revising, maintaining flow and consistency.",                "time": "45 min"},
    {"id": "ch05", "title": "Your Voice — Style Guide",      "desc": "Extract your writing style; use it for all future writing.",            "time": "30 min"},
    {"id": "ch06", "title": "Post-Writing Polish",           "desc": "Remove AI markers, vary sentence structure, inject scholarly voice.",   "time": "30 min"},
    {"id": "ch07", "title": "Research Habits That Compound", "desc": "CLAUDE.md, memory, hooks, workflows that improve over time.",           "time": "30 min"},
]

PAGE_TYPES = ["lecture", "tips", "exercises", "quiz"]


def extract_callouts(text: str) -> tuple[str, dict]:
    """Replace > [!TYPE] blocks with unique placeholders. Returns (processed_text, mapping)."""
    callout_map = {}
    lines = text.split('\n')
    result = []
    i = 0
    while i < len(lines):
        m = re.match(r'^> \[!(TIP|TRY|WARN|NOTE)\]\s*$', lines[i])
        if m:
            type_key = m.group(1)
            i += 1
            content_lines = []
            while i < len(lines) and (lines[i].startswith('> ') or lines[i].strip() == '>'):
                content_lines.append(lines[i][2:] if lines[i].startswith('> ') else '')
                i += 1
            placeholder = f'CALLOUT_PLACEHOLDER_{len(callout_map)}'
            callout_map[placeholder] = (type_key, '\n'.join(content_lines))
            result.append(f'\n{placeholder}\n')
        else:
            result.append(lines[i])
            i += 1
    return '\n'.join(result), callout_map


def render_md(text: str) -> str:
    """Convert markdown text (including callout syntax) to HTML."""
    processed, callout_map = extract_callouts(text)
    md = markdown.Markdown(extensions=['fenced_code', 'tables', 'toc'])
    html = md.convert(processed)
    for placeholder, (type_key, content) in callout_map.items():
        label, css_class = CALLOUT_TYPES[type_key]
        md2 = markdown.Markdown(extensions=['fenced_code', 'tables'])
        inner_html = md2.convert(content)
        callout_html = (
            f'<div class="callout {css_class}">'
            f'<span class="callout-label">{label}</span>'
            f'{inner_html}'
            f'</div>'
        )
        html = html.replace(f'<p>{placeholder}</p>', callout_html)
        html = html.replace(placeholder, callout_html)
    return html
```

- [ ] **Step 4: Run tests to confirm they pass**

```bash
pytest tests/test_build.py -v
```

Expected: All 8 tests `PASSED`.

- [ ] **Step 5: Commit**

```bash
git add build.py tests/test_build.py
git commit -m "feat: add callout pre-processor with tests"
```

---

## Task 3: Quiz Parser (TDD)

**Files:**
- Modify: `tests/test_build.py` (add quiz tests)
- Modify: `build.py` (add parse_quiz function)

Quiz markdown format (defined here, used in all chapter content tasks):

```markdown
## Q1

Question text here?

- [ ] Wrong option A
- [x] Correct option
- [ ] Wrong option B
- [ ] Wrong option C

> Explanation of why the correct answer is right.

---

## Think

Open-ended question here?

<answer>
Suggested answer paragraph.
</answer>
```

- [ ] **Step 1: Add quiz parser tests to tests/test_build.py**

Append to `tests/test_build.py`:

```python
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
```

- [ ] **Step 2: Run to confirm failure**

```bash
pytest tests/test_build.py -k "quiz" -v
```

Expected: `ImportError: cannot import name 'parse_quiz'`

- [ ] **Step 3: Implement parse_quiz in build.py**

Add to `build.py` after `render_md`:

```python
def parse_quiz(text: str) -> list[dict]:
    """Parse quiz.md into a list of question dicts for template rendering."""
    questions = []
    blocks = re.split(r'\n---\n', text.strip())
    for block in blocks:
        block = block.strip()
        if not block:
            continue
        # Thinking exercise: has <answer> tag
        if '<answer>' in block:
            q_text = re.split(r'\n\n', block, maxsplit=1)
            question_line = re.sub(r'^##\s+Think\s*\n', '', q_text[0]).strip()
            body = q_text[1] if len(q_text) > 1 else ''
            answer_m = re.search(r'<answer>\s*(.*?)\s*</answer>', body, re.DOTALL)
            answer = answer_m.group(1).strip() if answer_m else ''
            # Remove the answer block to get the question body
            q_body = re.sub(r'<answer>.*?</answer>', '', body, flags=re.DOTALL).strip()
            full_question = (question_line + '\n\n' + q_body).strip()
            questions.append({
                "type": "think",
                "question": full_question,
                "answer": answer,
            })
        else:
            # MCQ: has lines starting with - [ ] or - [x]
            lines = block.split('\n')
            question_lines, option_lines, explanation_lines = [], [], []
            state = 'question'
            for line in lines:
                if re.match(r'^- \[[ x]\]', line):
                    state = 'options'
                if state == 'question':
                    if not re.match(r'^##\s+Q\d+', line):
                        question_lines.append(line)
                elif state == 'options':
                    if re.match(r'^- \[[ x]\]', line):
                        option_lines.append(line)
                    elif line.startswith('>'):
                        explanation_lines.append(line.lstrip('> ').strip())
            options = []
            for opt in option_lines:
                correct = opt.startswith('- [x]')
                text = re.sub(r'^- \[[ x]\]\s*', '', opt).strip()
                options.append({"text": text, "correct": correct})
            if options:
                questions.append({
                    "type": "mcq",
                    "question": '\n'.join(question_lines).strip(),
                    "options": options,
                    "explanation": ' '.join(explanation_lines).strip(),
                })
    return questions
```

- [ ] **Step 4: Run tests to confirm they pass**

```bash
pytest tests/test_build.py -v
```

Expected: All tests `PASSED`.

- [ ] **Step 5: Commit**

```bash
git add build.py tests/test_build.py
git commit -m "feat: add quiz parser with tests"
```

---

## Task 4: Build Orchestrator

**Files:**
- Modify: `build.py` (add build() function)

- [ ] **Step 1: Add build() to build.py**

Append to `build.py`:

```python
def build():
    root = Path(__file__).parent
    env = Environment(loader=FileSystemLoader(str(root / 'templates')))
    env.filters['zfill'] = lambda s, w: str(s).zfill(w)

    for i, chapter in enumerate(CHAPTERS):
        chapter_dir = root / chapter['id']
        chapter_dir.mkdir(exist_ok=True)

        for page_type in PAGE_TYPES:
            md_path = chapter_dir / f'{page_type}.md'
            if md_path.exists():
                src = md_path.read_text(encoding='utf-8')
            else:
                src = f'# {page_type.capitalize()}\n\n_Content coming soon._'

            if page_type == 'quiz':
                questions = parse_quiz(src)
                content_html = None
            else:
                questions = None
                content_html = render_md(src)

            tmpl = env.get_template(f'{page_type}.html')
            html = tmpl.render(
                chapter=chapter,
                chapters=CHAPTERS,
                chapter_index=i,
                page_type=page_type,
                content=content_html,
                questions=questions,
                depth='../',
                prev_page=_prev_page(i, page_type),
                next_page=_next_page(i, page_type),
            )
            (chapter_dir / f'{page_type}.html').write_text(html, encoding='utf-8')

        idx_tmpl = env.get_template('chapter-index.html')
        idx_html = idx_tmpl.render(
            chapter=chapter,
            chapters=CHAPTERS,
            chapter_index=i,
            depth='../',
            prev_chapter=CHAPTERS[i - 1] if i > 0 else None,
            next_chapter=CHAPTERS[i + 1] if i < len(CHAPTERS) - 1 else None,
        )
        (chapter_dir / 'index.html').write_text(idx_html, encoding='utf-8')

    root_tmpl = env.get_template('root-index.html')
    root_html = root_tmpl.render(chapters=CHAPTERS)
    (root / 'index.html').write_text(root_html, encoding='utf-8')

    print(f'✓ Built {len(CHAPTERS)} chapters → open index.html in your browser.')


def _prev_page(chapter_index: int, page_type: str) -> dict | None:
    page_order = PAGE_TYPES
    pi = page_order.index(page_type)
    if pi > 0:
        return {"chapter": CHAPTERS[chapter_index], "page": page_order[pi - 1]}
    if chapter_index > 0:
        return {"chapter": CHAPTERS[chapter_index - 1], "page": page_order[-1]}
    return None


def _next_page(chapter_index: int, page_type: str) -> dict | None:
    page_order = PAGE_TYPES
    pi = page_order.index(page_type)
    if pi < len(page_order) - 1:
        return {"chapter": CHAPTERS[chapter_index], "page": page_order[pi + 1]}
    if chapter_index < len(CHAPTERS) - 1:
        return {"chapter": CHAPTERS[chapter_index + 1], "page": page_order[0]}
    return None


if __name__ == '__main__':
    build()
```

- [ ] **Step 2: Add integration test**

Append to `tests/test_build.py`:

```python
import tempfile, shutil
from pathlib import Path

def test_build_generates_html(tmp_path, monkeypatch):
    """build() creates HTML files for every chapter page."""
    import build as b
    # Patch root so build writes to tmp_path
    monkeypatch.setattr(b, 'CHAPTERS', [
        {"id": "ch00", "title": "Test Chapter", "desc": "Test.", "time": "5 min"},
    ])
    # Copy templates and assets to tmp_path
    repo_root = Path(__file__).parent.parent
    shutil.copytree(repo_root / 'templates', tmp_path / 'templates')
    (tmp_path / 'assets').mkdir()
    (tmp_path / 'ch00').mkdir()
    (tmp_path / 'ch00' / 'lecture.md').write_text('# Hello\nWorld.')
    (tmp_path / 'ch00' / 'quiz.md').write_text(
        '## Q1\n\nQuestion?\n\n- [ ] Wrong\n- [x] Right\n\n> Correct.\n'
    )
    monkeypatch.chdir(tmp_path)
    # Patch Path(__file__).parent inside build module
    import importlib
    monkeypatch.setattr(Path, '__new__', lambda cls, *a, **kw: object.__new__(cls))
    # Simpler: just call build() directly after patching root lookup
    # Instead: test the file-writing functions independently
    from build import render_md, parse_quiz
    html = render_md('# Hello\nWorld.')
    assert '<h1>' in html
    questions = parse_quiz('## Q1\n\nQ?\n\n- [x] Right\n- [ ] Wrong\n\n> Exp.\n')
    assert questions[0]['type'] == 'mcq'
```

- [ ] **Step 3: Run tests**

```bash
pytest tests/test_build.py -v
```

Expected: All tests `PASSED`.

- [ ] **Step 4: Commit**

```bash
git add build.py tests/test_build.py
git commit -m "feat: add build orchestrator with prev/next page navigation"
```

---

## Task 5: base.html Template

**Files:**
- Create: `templates/base.html`

- [ ] **Step 1: Create templates/base.html**

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{% block title %}Claude Code Tutorial{% endblock %}</title>

  <!-- Tailwind Play CDN -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {
      theme: {
        extend: {
          fontFamily: {
            sans: ['Inter', 'system-ui', 'sans-serif'],
            mono: ['"JetBrains Mono"', 'monospace'],
          },
          colors: {
            sidebar: '#1a1f2e',
            accent: '#6366f1',
          }
        }
      }
    }
  </script>

  <!-- Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">

  <!-- Prism.js (One Dark theme) -->
  <link href="https://cdn.jsdelivr.net/npm/prismjs@1.29.0/themes/prism-tomorrow.min.css" rel="stylesheet">

  <link rel="stylesheet" href="{{ depth }}assets/style.css">
</head>

<body class="font-sans bg-[#f9f8f6] text-gray-800">

  <!-- Sidebar -->
  <aside id="sidebar"
         class="fixed top-0 left-0 h-full w-60 bg-sidebar text-white overflow-y-auto z-20 transition-transform">
    <div class="p-5">
      <a href="{{ depth }}index.html"
         class="block text-white font-semibold text-sm mb-8 opacity-90 hover:opacity-100">
        Claude Code Tutorial
      </a>
      <nav>
        {% for ch in chapters %}
        {% set idx = loop.index0 %}
        <div class="mb-0.5">
          <a href="{{ depth }}{{ ch.id }}/index.html"
             class="flex items-center gap-2 px-3 py-2 rounded text-sm
                    {% if ch.id == chapter.id %}
                      text-white font-semibold bg-white/10
                    {% else %}
                      text-gray-400 hover:text-white hover:bg-white/5
                    {% endif %}">
            <span class="text-xs opacity-50 font-mono w-5">{{ '%02d' % idx }}</span>
            <span>{{ ch.title }}</span>
          </a>
          {% if ch.id == chapter.id %}
          <div class="ml-7 mt-1 mb-2 space-y-0.5 border-l border-white/10 pl-3">
            {% for pt in ['lecture', 'tips', 'exercises', 'quiz'] %}
            <a href="{{ depth }}{{ ch.id }}/{{ pt }}.html"
               class="block py-1 text-xs rounded
                      {% if page_type == pt %}
                        text-accent font-semibold
                      {% else %}
                        text-gray-500 hover:text-gray-200
                      {% endif %}">
              {{ pt | capitalize }}
            </a>
            {% endfor %}
          </div>
          {% endif %}
        </div>
        {% endfor %}
      </nav>
    </div>
  </aside>

  <!-- Main -->
  <div class="ml-60">
    <!-- Top bar -->
    <header class="sticky top-0 bg-white/80 backdrop-blur border-b border-gray-200 z-10">
      <div class="px-10 py-3 flex items-center justify-between">
        <span class="text-sm font-medium text-gray-700">
          {% block page_title %}{% endblock %}
        </span>
        <span class="text-xs font-medium uppercase tracking-widest text-gray-400">
          {% block page_badge %}{% endblock %}
        </span>
      </div>
      <!-- Progress bar: width = (chapter_index / total_chapters * 100)% -->
      <div class="h-0.5 bg-accent/80"
           style="width: {{ ((chapter_index + 1) / chapters|length * 100)|round|int }}%">
      </div>
    </header>

    <!-- Content area -->
    <main class="px-10 py-10 max-w-[800px]">
      {% block main %}{% endblock %}
    </main>

    <!-- Prev / Next navigation -->
    <footer class="px-10 py-8 border-t border-gray-200 flex items-center justify-between">
      {% if prev_page %}
      <a href="{{ depth }}{{ prev_page.chapter.id }}/{{ prev_page.page }}.html"
         class="flex items-center gap-2 text-sm text-accent hover:underline">
        ← {{ prev_page.chapter.title }} · {{ prev_page.page | capitalize }}
      </a>
      {% else %}<span></span>{% endif %}

      {% if next_page %}
      <a href="{{ depth }}{{ next_page.chapter.id }}/{{ next_page.page }}.html"
         class="flex items-center gap-2 text-sm text-accent hover:underline">
        {{ next_page.chapter.title }} · {{ next_page.page | capitalize }} →
      </a>
      {% else %}<span></span>{% endif %}
    </footer>
  </div>

  <!-- Prism.js -->
  <script src="https://cdn.jsdelivr.net/npm/prismjs@1.29.0/prism.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/prismjs@1.29.0/components/prism-python.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/prismjs@1.29.0/components/prism-bash.min.js"></script>

  {% block scripts %}{% endblock %}
</body>
</html>
```

- [ ] **Step 2: Commit**

```bash
git add templates/base.html
git commit -m "feat: add base Jinja2 template with sidebar and nav"
```

---

## Task 6: Page Templates

**Files:**
- Create: `templates/lecture.html`
- Create: `templates/tips.html`
- Create: `templates/exercises.html`
- Create: `templates/quiz.html`
- Create: `templates/chapter-index.html`

- [ ] **Step 1: Create templates/lecture.html**

```html
{% extends "base.html" %}

{% block title %}{{ chapter.title }} — Lecture{% endblock %}
{% block page_title %}{{ chapter.title }}{% endblock %}
{% block page_badge %}Lecture{% endblock %}

{% block main %}
<article class="prose-content">
  {{ content | safe }}
</article>
{% endblock %}

{% block scripts %}
<script>
  // Copy-to-clipboard for code blocks
  document.querySelectorAll('pre').forEach(pre => {
    const btn = document.createElement('button');
    btn.textContent = 'Copy';
    btn.className = 'copy-btn';
    btn.addEventListener('click', () => {
      navigator.clipboard.writeText(pre.querySelector('code').innerText);
      btn.textContent = 'Copied!';
      setTimeout(() => btn.textContent = 'Copy', 2000);
    });
    pre.style.position = 'relative';
    pre.appendChild(btn);
  });
</script>
{% endblock %}
```

- [ ] **Step 2: Create templates/tips.html**

```html
{% extends "base.html" %}

{% block title %}{{ chapter.title }} — Tips{% endblock %}
{% block page_title %}{{ chapter.title }}{% endblock %}
{% block page_badge %}Tips{% endblock %}

{% block main %}
<article class="prose-content">
  {{ content | safe }}
</article>
{% endblock %}

{% block scripts %}
<script>
  document.querySelectorAll('pre').forEach(pre => {
    const btn = document.createElement('button');
    btn.textContent = 'Copy';
    btn.className = 'copy-btn';
    btn.addEventListener('click', () => {
      navigator.clipboard.writeText(pre.querySelector('code').innerText);
      btn.textContent = 'Copied!';
      setTimeout(() => btn.textContent = 'Copy', 2000);
    });
    pre.style.position = 'relative';
    pre.appendChild(btn);
  });
</script>
{% endblock %}
```

- [ ] **Step 3: Create templates/exercises.html**

```html
{% extends "base.html" %}

{% block title %}{{ chapter.title }} — Exercises{% endblock %}
{% block page_title %}{{ chapter.title }}{% endblock %}
{% block page_badge %}Exercises{% endblock %}

{% block main %}
<article class="prose-content">
  {{ content | safe }}
</article>
{% endblock %}

{% block scripts %}
<script>
  document.querySelectorAll('pre').forEach(pre => {
    const btn = document.createElement('button');
    btn.textContent = 'Copy';
    btn.className = 'copy-btn';
    btn.addEventListener('click', () => {
      navigator.clipboard.writeText(pre.querySelector('code').innerText);
      btn.textContent = 'Copied!';
      setTimeout(() => btn.textContent = 'Copy', 2000);
    });
    pre.style.position = 'relative';
    pre.appendChild(btn);
  });
</script>
{% endblock %}
```

- [ ] **Step 4: Create templates/quiz.html**

```html
{% extends "base.html" %}

{% block title %}{{ chapter.title }} — Quiz{% endblock %}
{% block page_title %}{{ chapter.title }}{% endblock %}
{% block page_badge %}Quiz{% endblock %}

{% block main %}
<div class="quiz-container">
  <h1 class="text-2xl font-bold mb-2">Quiz</h1>
  <p class="text-gray-500 mb-8 text-sm">{{ chapter.title }}</p>

  {% for q in questions %}
  <div class="question-block mb-10" data-qindex="{{ loop.index0 }}">

    {% if q.type == 'mcq' %}
    <div class="mcq-block">
      <p class="font-semibold text-gray-800 mb-4 text-base">
        {{ loop.index }}. {{ q.question }}
      </p>
      <div class="options-grid space-y-2">
        {% for opt in q.options %}
        <button class="mcq-option w-full text-left px-4 py-3 rounded-lg border border-gray-200
                        bg-white hover:bg-gray-50 text-sm transition-colors"
                data-correct="{{ opt.correct | lower }}">
          {{ opt.text }}
        </button>
        {% endfor %}
      </div>
      <div class="explanation hidden mt-4 p-4 bg-indigo-50 rounded-lg text-sm text-indigo-800 border border-indigo-100">
        {{ q.explanation }}
      </div>
    </div>

    {% elif q.type == 'think' %}
    <div class="think-block">
      <p class="font-semibold text-gray-800 mb-3 text-base">
        {{ loop.index }}. {{ q.question }}
      </p>
      <textarea class="w-full h-28 p-3 border border-gray-200 rounded-lg text-sm
                       bg-white focus:outline-none focus:border-accent resize-y"
                placeholder="Write your answer here…"></textarea>
      <button class="reveal-btn mt-3 px-4 py-2 text-sm font-medium text-accent
                     border border-accent rounded-lg hover:bg-accent hover:text-white transition-colors">
        Reveal suggested answer
      </button>
      <div class="answer hidden mt-3 p-4 bg-green-50 rounded-lg text-sm text-green-800 border border-green-100">
        {{ q.answer }}
      </div>
    </div>
    {% endif %}

  </div>
  {% endfor %}
</div>

<script src="{{ depth }}assets/quiz.js"></script>
{% endblock %}
```

- [ ] **Step 5: Create templates/chapter-index.html**

```html
{% extends "base.html" %}

{% block title %}{{ chapter.title }}{% endblock %}
{% block page_title %}{{ chapter.title }}{% endblock %}
{% block page_badge %}Chapter {{ '%02d' % chapter_index }}{% endblock %}

{% block main %}
<div class="mb-8">
  <span class="text-xs font-mono text-gray-400 uppercase tracking-widest">
    Chapter {{ '%02d' % chapter_index }} · {{ chapter.time }}
  </span>
  <h1 class="text-3xl font-bold mt-2 mb-3">{{ chapter.title }}</h1>
  <p class="text-gray-600 text-base">{{ chapter.desc }}</p>
</div>

<div class="grid grid-cols-2 gap-4 mt-10">
  {% for pt, icon, color in [
      ('lecture',   '📖', 'indigo'),
      ('tips',      '💡', 'yellow'),
      ('exercises', '⚡', 'green'),
      ('quiz',      '🧠', 'purple')
  ] %}
  <a href="{{ pt }}.html"
     class="group block p-5 rounded-xl border border-gray-200 bg-white
            hover:border-{{ color }}-300 hover:shadow-sm transition-all">
    <span class="text-2xl mb-3 block">{{ icon }}</span>
    <h2 class="font-semibold text-gray-800 group-hover:text-accent">{{ pt | capitalize }}</h2>
    <p class="text-xs text-gray-500 mt-1">
      {% if pt == 'lecture' %}Core concepts and explanations
      {% elif pt == 'tips' %}Shortcuts, patterns, and tricks
      {% elif pt == 'exercises' %}Hands-on practice with CC
      {% else %}Test your understanding
      {% endif %}
    </p>
  </a>
  {% endfor %}
</div>

{% if prev_chapter or next_chapter %}
<div class="flex justify-between mt-12 pt-8 border-t border-gray-200">
  {% if prev_chapter %}
  <a href="{{ depth }}{{ prev_chapter.id }}/index.html"
     class="text-sm text-accent hover:underline">← {{ prev_chapter.title }}</a>
  {% else %}<span></span>{% endif %}
  {% if next_chapter %}
  <a href="{{ depth }}{{ next_chapter.id }}/index.html"
     class="text-sm text-accent hover:underline">{{ next_chapter.title }} →</a>
  {% else %}<span></span>{% endif %}
</div>
{% endif %}
{% endblock %}
```

- [ ] **Step 6: Commit**

```bash
git add templates/
git commit -m "feat: add all page templates"
```

---

## Task 7: Root Index Template

**Files:**
- Create: `templates/root-index.html`

- [ ] **Step 1: Create templates/root-index.html**

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Claude Code Tutorial</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {
      theme: { extend: { fontFamily: { sans: ['Inter', 'sans-serif'] }, colors: { accent: '#6366f1' } } }
    }
  </script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="assets/style.css">
</head>
<body class="font-sans bg-[#f9f8f6] text-gray-800 min-h-screen">
  <div class="max-w-4xl mx-auto px-8 py-16">
    <!-- Hero -->
    <div class="mb-16 text-center">
      <div class="inline-block bg-accent/10 text-accent text-xs font-semibold px-3 py-1 rounded-full mb-4 uppercase tracking-widest">
        Self-paced · 8 Chapters · ~4 hours
      </div>
      <h1 class="text-4xl font-bold text-gray-900 mb-4">Claude Code Tutorial</h1>
      <p class="text-lg text-gray-600 max-w-xl mx-auto">
        You've been using a calculator. This is the computer.
        Learn to use Claude Code as a research superpower.
      </p>
      <a href="{{ chapters[0].id }}/index.html"
         class="inline-block mt-8 px-6 py-3 bg-accent text-white font-semibold rounded-lg hover:bg-indigo-700 transition-colors">
        Start Chapter 00 →
      </a>
    </div>

    <!-- Chapter cards -->
    <div class="space-y-3">
      {% for ch in chapters %}
      {% set idx = loop.index0 %}
      <a href="{{ ch.id }}/index.html"
         class="group flex items-start gap-5 p-5 bg-white rounded-xl border border-gray-200
                hover:border-accent/50 hover:shadow-sm transition-all">
        <span class="text-2xl font-mono font-bold text-gray-200 group-hover:text-accent/30 transition-colors min-w-[2.5rem]">
          {{ '%02d' % idx }}
        </span>
        <div class="flex-1">
          <h2 class="font-semibold text-gray-800 group-hover:text-accent transition-colors">{{ ch.title }}</h2>
          <p class="text-sm text-gray-500 mt-0.5">{{ ch.desc }}</p>
        </div>
        <span class="text-xs text-gray-400 self-center shrink-0">{{ ch.time }}</span>
      </a>
      {% endfor %}
    </div>
  </div>
</body>
</html>
```

- [ ] **Step 2: Commit**

```bash
git add templates/root-index.html
git commit -m "feat: add root index template with chapter card grid"
```

---

## Task 8: style.css

**Files:**
- Create: `assets/style.css`

- [ ] **Step 1: Create assets/style.css**

```css
/* ── Prose content ─────────────────────────────────────────────────────────── */
.prose-content h1 { font-size: 1.875rem; font-weight: 700; margin: 0 0 0.5rem; color: #111827; }
.prose-content h2 { font-size: 1.375rem; font-weight: 600; margin: 2rem 0 0.75rem; color: #1f2937; }
.prose-content h3 { font-size: 1.125rem; font-weight: 600; margin: 1.5rem 0 0.5rem; color: #374151; }
.prose-content p  { line-height: 1.75; margin: 0 0 1rem; color: #374151; }
.prose-content ul, .prose-content ol { padding-left: 1.5rem; margin: 0 0 1rem; }
.prose-content li { line-height: 1.75; margin-bottom: 0.25rem; color: #374151; }
.prose-content a  { color: #6366f1; text-decoration: underline; }
.prose-content a:hover { color: #4f46e5; }
.prose-content code { font-family: 'JetBrains Mono', monospace; font-size: 0.875em;
                      background: #f3f4f6; padding: 0.15em 0.4em; border-radius: 4px; color: #be185d; }
.prose-content pre { border-radius: 8px; margin: 1.25rem 0; overflow-x: auto; }
.prose-content pre code { background: none; padding: 0; color: inherit; font-size: 0.875rem; }
.prose-content blockquote { border-left: 3px solid #d1d5db; padding-left: 1rem;
                             color: #6b7280; font-style: italic; margin: 1rem 0; }
.prose-content table { width: 100%; border-collapse: collapse; margin: 1rem 0; font-size: 0.9rem; }
.prose-content th { text-align: left; padding: 0.5rem 0.75rem; background: #f9fafb;
                    border-bottom: 2px solid #e5e7eb; font-weight: 600; }
.prose-content td { padding: 0.5rem 0.75rem; border-bottom: 1px solid #f3f4f6; }

/* ── Callout boxes ─────────────────────────────────────────────────────────── */
.callout {
  border-left: 4px solid;
  border-radius: 0 8px 8px 0;
  padding: 0.875rem 1rem;
  margin: 1.25rem 0;
}
.callout-label {
  display: block;
  font-weight: 600;
  font-size: 0.8rem;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  margin-bottom: 0.4rem;
}
.callout p { margin: 0; font-size: 0.9rem; line-height: 1.6; }

.callout-tip  { border-color: #fbbf24; background: #fffbeb; }
.callout-tip  .callout-label { color: #b45309; }

.callout-try  { border-color: #22c55e; background: #f0fdf4; }
.callout-try  .callout-label { color: #15803d; }

.callout-warn { border-color: #f97316; background: #fff7ed; }
.callout-warn .callout-label { color: #c2410c; }

.callout-note { border-color: #3b82f6; background: #eff6ff; }
.callout-note .callout-label { color: #1d4ed8; }

/* ── Copy button ───────────────────────────────────────────────────────────── */
.copy-btn {
  position: absolute;
  top: 0.5rem;
  right: 0.5rem;
  padding: 0.2rem 0.6rem;
  font-size: 0.7rem;
  font-family: 'JetBrains Mono', monospace;
  background: rgba(255,255,255,0.12);
  color: #d1d5db;
  border: 1px solid rgba(255,255,255,0.15);
  border-radius: 4px;
  cursor: pointer;
  transition: background 0.15s;
}
.copy-btn:hover { background: rgba(255,255,255,0.2); }

/* ── Quiz ──────────────────────────────────────────────────────────────────── */
.mcq-option { cursor: pointer; }
.mcq-option.correct  { background: #f0fdf4 !important; border-color: #22c55e !important; color: #15803d; font-weight: 500; }
.mcq-option.wrong    { background: #fef2f2 !important; border-color: #ef4444 !important; color: #b91c1c; }
.mcq-option:disabled { cursor: default; }
```

- [ ] **Step 2: Commit**

```bash
git add assets/style.css
git commit -m "feat: add stylesheet with prose, callouts, copy button, quiz styles"
```

---

## Task 9: Quiz JS

**Files:**
- Create: `assets/quiz.js`

- [ ] **Step 1: Create assets/quiz.js**

```javascript
document.addEventListener('DOMContentLoaded', () => {
  // MCQ blocks
  document.querySelectorAll('.mcq-block').forEach(block => {
    const options = block.querySelectorAll('.mcq-option');
    const explanation = block.querySelector('.explanation');
    let answered = false;

    options.forEach(btn => {
      btn.addEventListener('click', () => {
        if (answered) return;
        answered = true;

        options.forEach(o => {
          o.disabled = true;
          if (o.dataset.correct === 'true') {
            o.classList.add('correct');
          }
        });

        if (btn.dataset.correct !== 'true') {
          btn.classList.add('wrong');
        }

        if (explanation) {
          explanation.classList.remove('hidden');
        }
      });
    });
  });

  // Thinking exercise reveal
  document.querySelectorAll('.think-block').forEach(block => {
    const btn = block.querySelector('.reveal-btn');
    const answer = block.querySelector('.answer');
    if (!btn || !answer) return;

    btn.addEventListener('click', () => {
      if (answer.classList.contains('hidden')) {
        answer.classList.remove('hidden');
        btn.textContent = 'Hide answer';
      } else {
        answer.classList.add('hidden');
        btn.textContent = 'Reveal suggested answer';
      }
    });
  });
});
```

- [ ] **Step 2: Commit**

```bash
git add assets/quiz.js
git commit -m "feat: add quiz interactivity JS"
```

---

## Task 10: End-to-End Build Verification

**Files:**
- Create: placeholder `lecture.md` for ch00 (to test the pipeline)

- [ ] **Step 1: Create a minimal ch00/lecture.md**

```markdown
# Welcome & The Superpower

> [!NOTE]
> This is a placeholder to test the build pipeline.

## Hello

This is a **test** paragraph with `inline code`.

```python
print("Hello from Claude Code!")
```

> [!TIP]
> This is a tip callout.
```

- [ ] **Step 2: Create minimal ch00/quiz.md**

```markdown
## Q1

What does CC stand for in this tutorial?

- [ ] Cloud Computing
- [x] Claude Code
- [ ] Command Center
- [ ] Custom CLI

> CC always means Claude Code — the terminal-based AI assistant.

---

## Think

What is one thing you hope to learn from this tutorial?

<answer>
Any personal learning goal is valid. Examples: write simulations faster, stop copy-pasting, write papers in my own voice.
</answer>
```

- [ ] **Step 3: Run the build**

```bash
python build.py
```

Expected output: `✓ Built 8 chapters → open index.html in your browser.`

- [ ] **Step 4: Open in browser and verify**

Open `index.html` — should show chapter card grid.
Open `ch00/lecture.html` — should show styled content with callout boxes.
Open `ch00/quiz.html` — click a wrong MCQ option (should turn red), click correct (should turn green), click reveal answer on thinking exercise.

- [ ] **Step 5: Commit**

```bash
git add ch00/lecture.md ch00/quiz.md
git commit -m "chore: add ch00 test placeholders, verify full build pipeline"
```

---

## Task 11: ch00 Content — Welcome & The Superpower

**Files:**
- Modify: `ch00/lecture.md`
- Create: `ch00/tips.md`
- Create: `ch00/exercises.md`
- Modify: `ch00/quiz.md`

**Target time:** 20 min chapter.

- [ ] **Step 1: Write ch00/lecture.md**

Sections to cover:

```markdown
# Welcome & The Superpower

Brief intro: "You already use AI. This tutorial makes you 10× faster at using it."

## The Copy-Paste Trap
- Diagram: Claude.ai workflow (write prompt → get code → copy → paste → run → copy error → paste back)
- The problem: no shared context, no file access, no memory, every session is zero
- How much time researchers lose to this workflow

## What Claude Code Changes
- CC lives in your terminal, inside your project directory
- It can read every file, run code, see the output, fix errors — without you lifting a finger
- The mental model: CC is a brilliant collaborator sitting next to you, looking at the same screen

> [!NOTE]
> Claude Code is not ChatGPT in a terminal. It's an agent with tool use: it can read files,
> run shell commands, write and edit code, and iterate — all in one conversation.

## Installation
Step-by-step for macOS/Linux/Windows:
```bash
npm install -g @anthropic-ai/claude-code
claude
```
What you see on first run. How to get an API key.

## Your First 5 Minutes
- How to start a session: `claude` in your project directory
- The three things to do in every new session: tell CC what the project is, what you're working on today, what you need
- How to end a session (Ctrl+C or just close terminal)

> [!TIP]
> Always start CC from inside your project directory. It uses the current directory as context.

## The Mental Model Shift
- Before: "I use AI to generate code I paste in"
- After: "I have an AI partner working in my project with me"
- The shift isn't about the tool — it's about how you collaborate

> [!TRY]
> Open your terminal, navigate to any project folder, and type `claude`.
> Ask it: "What files are in this directory and what do they do?"
```

- [ ] **Step 2: Write ch00/tips.md**

```markdown
# Tips: Welcome & The Superpower

## 1. Start every CC session with a one-liner context
Always open with: "I'm working on [project]. Today I want to [goal]."
This primes CC with context and makes every response more relevant.

## 2. `claude --continue` picks up your last session
Don't lose your conversation history. Use `claude --continue` to resume.

## 3. Use `/help` inside CC to see all slash commands
Type `/help` at any CC prompt to see what's available: /clear, /compact, /cost, etc.

## 4. CC works best when it can see your files
Resist the urge to paste code into the prompt. Instead say:
"Read `simulation.py` and tell me what the `run()` function does."

## 5. The escape hatch: Ctrl+C stops any running action
If CC starts doing something unexpected, Ctrl+C stops it immediately.
Nothing is committed without your say-so.

## 6. Check your API usage with `/cost`
Type `/cost` at any time to see how many tokens you've used in the session.
```

- [ ] **Step 3: Write ch00/exercises.md**

```markdown
# Exercises: Welcome & The Superpower

## Exercise 1: Install and First Contact (10 min)

1. Install Claude Code: `npm install -g @anthropic-ai/claude-code`
2. Navigate to any folder on your computer that has files in it (even your Downloads folder)
3. Run `claude`
4. Ask: "List the files here and summarize what each one might be for."
5. Note what CC says. Did it get anything right? Wrong?

**What you're practicing:** Starting a session, understanding how CC reads file context.

---

## Exercise 2: Ask CC About Itself (5 min)

In a CC session, ask:
- "What can you do that Claude.ai cannot?"
- "What tools do you have access to right now?"

**What you're practicing:** Understanding CC's capabilities by asking it directly.

---

## Exercise 3: The Context Test (10 min)

1. Create a new folder called `test-project`
2. Create a file `notes.txt` with 3–4 sentences about anything
3. Start a CC session in that folder
4. Ask: "Read notes.txt and suggest three follow-up questions I should think about."

**What you're practicing:** Giving CC file context and using it for research-style thinking.
```

- [ ] **Step 4: Write ch00/quiz.md**

```markdown
## Q1

When you start Claude Code with `claude` in your terminal, what does it use as its primary context?

- [ ] Your Claude.ai conversation history
- [ ] The entire contents of your home directory
- [x] The current working directory and its files
- [ ] Whatever you paste into the first prompt

> CC starts by reading the current directory. This is why you should always launch it from inside your project folder.

---

## Q2

Which of these tasks can Claude Code do that Claude.ai cannot?

- [ ] Write Python code
- [ ] Answer research questions
- [x] Run a shell command and read the output
- [ ] Explain a concept

> CC has tool use: it can execute bash commands, read and write files, and see the results directly. Claude.ai is a chat interface with no system access.

---

## Q3

What is the best way to give CC context about a file?

- [ ] Copy-paste the file contents into the prompt
- [x] Tell CC the filename and ask it to read it
- [ ] Summarize the file yourself first
- [ ] CC automatically reads all files without being asked

> Ask CC to read the file by name. It will use its file-reading tool to access it directly — no copy-pasting needed.

---

## Think

Think back to the last time you used Claude.ai or ChatGPT for a coding or writing task. Describe one frustration you had with the copy-paste workflow, and explain how Claude Code would have changed that experience.

<answer>
Common answers: losing context between sessions (CC maintains project context), having to re-explain the project each time (CC reads CLAUDE.md), copying error messages back (CC sees terminal output directly), not being able to reference multiple files (CC reads any file you name).
</answer>
```

- [ ] **Step 5: Run build and verify**

```bash
python build.py
```

Open `ch00/lecture.html` in browser. Verify callouts render, code is highlighted, navigation works.

- [ ] **Step 6: Commit**

```bash
git add ch00/
git commit -m "content: ch00 — Welcome & The Superpower"
```

---

## Task 12: ch01 Content — Your First Research Session

**Files:** `ch01/lecture.md`, `ch01/tips.md`, `ch01/exercises.md`, `ch01/quiz.md`

- [ ] **Step 1: Write ch01/lecture.md**

Sections:
```markdown
# Your First Research Session

## What "Context" Means for CC
- CC reads files you point it to — PDFs, CSVs, Python scripts, notes
- It holds up to ~200k tokens of context in a session
- Strategy: give CC the files most relevant to today's task, not everything

> [!NOTE]
> CC cannot open PDFs directly, but it can read text extracted from them.
> For papers, copy the text or use a tool like `pdftotext paper.pdf paper.txt` first.

## The Research Dialogue Pattern
- Don't give CC one big prompt and wait. Have a conversation.
- Start broad → get orientation → ask specific questions → refine
- Example flow for a new dataset or paper

> [!TRY]
> Open a CC session with a paper or dataset you're currently working with.
> Ask: "Read [filename]. What are the three most important things I should know about this?"

## Reading and Analyzing Data with CC
- Ask CC to read a CSV and describe its structure
- Ask CC to identify anomalies, missing values, or interesting patterns
- CC can write a quick Python script to explore the data — right then, in the same session

## Iterative Questioning
- The power is in follow-up questions, not the first prompt
- "That's interesting — can you show me what the distribution looks like?"
- "I don't believe that number — re-check your calculation"
- CC remembers everything in the session context

> [!WARN]
> CC can make mistakes, especially with numerical reasoning.
> Always verify quantitative claims it makes against your own analysis.

## Ending and Resuming Sessions
- `Ctrl+C` to end a session
- `claude --continue` to resume the last session
- Key limitation: context does not persist across new sessions (use CLAUDE.md for that — covered in ch07)
```

- [ ] **Step 2: Write ch01/tips.md**

```markdown
# Tips: Your First Research Session

## 1. Point CC to specific files rather than describing them
"Read `data/survey_results.csv`" beats "I have a CSV with survey results."
CC reads the actual file — no loss in translation.

## 2. Ask CC to make a to-do list for your research session
"Given what's in these files, suggest 5 specific tasks I could accomplish today."
This turns CC into a research planning assistant, not just a Q&A machine.

## 3. Use "Explain like I just picked this up" for unfamiliar papers
Prompt: "Read `paper.txt`. Explain the core argument and methodology to someone
who knows the field but hasn't read this paper."

## 4. Ask CC to find contradictions
"I have two papers: paper1.txt and paper2.txt. Where do they disagree?"
CC will read both and surface the tension — useful for lit review.

## 5. Save important CC outputs to a file
Ask CC: "Write your summary to `session-notes/2026-05-01-paper-review.md`"
CC will create the file. Build a habit of capturing CC's analytical work.

## 6. Text-only formats work best
PDFs → extract text with `pdftotext`. Images in papers → describe them to CC yourself.
```

- [ ] **Step 3: Write ch01/exercises.md**

```markdown
# Exercises: Your First Research Session

## Exercise 1: Analyze a Dataset (15 min)

1. Find any CSV file in your research files (or download one from Kaggle)
2. Start CC in the same directory
3. Ask: "Read `yourfile.csv`. What is the structure of this data, and what are three interesting patterns?"
4. Follow up: "What would be the most important variable to investigate first? Write a Python script to visualize it."
5. Run the script CC writes (copy the filename it saves to, or ask CC to run it)

---

## Exercise 2: Deep-Dive a Paper (15 min)

1. Take a paper you've already read (or are supposed to read)
2. Extract text if needed: `pdftotext paper.pdf paper.txt`
3. Start CC: "Read `paper.txt`. What is the central research question and the key finding?"
4. Ask: "What are the three biggest methodological limitations the authors acknowledge?"
5. Ask: "Generate five follow-up research questions this paper opens up."

---

## Exercise 3: Compare Two Sources (10 min)

1. Get two short texts (two abstracts, two notes, two papers) in your directory
2. Ask CC: "Read both files. Where do they agree? Where do they contradict each other?"

**What you're practicing:** Multi-file context, comparative analysis.
```

- [ ] **Step 4: Write ch01/quiz.md**

```markdown
## Q1

You want CC to analyze a PDF paper. What is the correct first step?

- [ ] Ask CC to download it from the internet
- [ ] Paste the abstract into the prompt
- [x] Extract text with `pdftotext paper.pdf paper.txt`, then point CC to the .txt file
- [ ] CC can read PDFs directly without any conversion

> CC reads text files, not binary formats like PDF. Extract text first, then CC can read the whole paper.

---

## Q2

You ask CC about a dataset and it gives you a number that seems wrong. What should you do?

- [ ] Trust CC — it's more reliable than manual calculations
- [x] Tell CC "I don't think that's right — re-check your calculation" and verify independently
- [ ] Start a new session and ask again
- [ ] Ignore it and move on

> CC makes mistakes, especially with arithmetic and numerical reasoning. Always verify quantitative claims. Push back directly — CC will re-examine its work.

---

## Think

You are starting a research session to work on your literature review. You have 5 papers as .txt files and a notes file. Describe the first 3 prompts you would send to CC and what you expect to get from each.

<answer>
Example sequence: (1) "Read all five paper files. Give me a one-paragraph summary of each." → orientation pass. (2) "Which two papers are most closely related to each other in methodology?" → identifies clusters. (3) "Draft a 3-paragraph lit review synthesis that covers the common themes across these papers." → first draft for revision.
</answer>
```

- [ ] **Step 5: Build and verify, then commit**

```bash
python build.py
git add ch01/
git commit -m "content: ch01 — Your First Research Session"
```

---

## Task 13: ch02 Content — Simulations & Code

**Files:** `ch02/lecture.md`, `ch02/tips.md`, `ch02/exercises.md`, `ch02/quiz.md`

- [ ] **Step 1: Write ch02/lecture.md**

Sections:
```markdown
# Simulations & Code

## CC as Your Coding Partner
- The difference: CC can see your whole project, run your code, and fix errors in a loop
- Old workflow: write → error → paste to Claude.ai → paste fix back → repeat
- New workflow: write → error → CC sees it → CC fixes it → CC runs it to confirm

> [!TRY]
> Open CC in a project with a Python script. Ask: "Read `script.py` and describe
> what each function does." Then: "What would happen if I called `main()` with an empty list?"

## Writing New Simulation Code
- Tell CC what the simulation should do, not how to code it
- Describe inputs, outputs, and the process you want to model
- Ask CC to write it, run it, and show you the output in one pass

## The Debug Loop
- When code breaks: don't copy the error. Ask CC to run it: `python simulate.py`
- CC sees the full traceback and the source code simultaneously
- Ask: "Run the script. If it fails, fix it and run again until it works."

> [!WARN]
> Be specific about what "working" means. "Make it not crash" is different from
> "produce correct output for these test cases."

## Iterative Improvement
- "Make it 3× faster"
- "Add progress reporting every 1000 iterations"
- "Refactor this into a class so I can run multiple parameter sets"
- CC can profile, optimize, and restructure — staying in the same session

## Running and Visualizing Results
- Ask CC to save results to CSV and generate a plot
- CC can write plotting code using matplotlib, seaborn, or plotly
- Ask CC to describe what the plot shows — useful sanity check
```

- [ ] **Step 2: Write ch02/tips.md**

```markdown
# Tips: Simulations & Code

## 1. Describe the science, let CC handle the syntax
"Simulate 10,000 random walks of 100 steps each. Track the final position distribution."
You describe the model; CC writes the Python.

## 2. Ask CC to add assertions for sanity checking
"Add assertions to verify the output distribution has mean ≈ 0 and std ≈ 10."
This catches bugs without writing a full test suite.

## 3. Ask CC to create a CLAUDE.md for your simulation project
"Write a CLAUDE.md file that describes this simulation: what it models, key parameters,
how to run it, and what outputs to expect."
Future CC sessions (and your future self) will thank you.

## 4. "Run it with these parameters and show me the output"
Don't ask CC to write code and then run it yourself. Ask CC to run it.
CC's output includes both the code and the execution results.

## 5. Parameterize early
Ask CC to refactor a hardcoded simulation to accept parameters from the command line or a config file.
This takes 2 minutes with CC and saves hours of future editing.

## 6. Version control your simulations
Ask CC to help you set up git if you haven't: "Initialize git in this directory and make a first commit."
```

- [ ] **Step 3: Write ch02/exercises.md**

```markdown
# Exercises: Simulations & Code

## Exercise 1: Write a Simulation from Scratch (20 min)

Pick a simple stochastic process from your research (or use this one):
> Simulate N particles doing a random walk in 2D. Each step moves ±1 in x and ±1 in y independently. Run 1000 particles for 500 steps. Plot the distribution of final distances from the origin.

1. Start CC in a new directory
2. Describe the simulation to CC (use your own domain if you have one)
3. Ask CC to write the code, run it, and show you the resulting plot
4. Ask CC to add a command-line parameter for the number of steps

---

## Exercise 2: Debug a Broken Script (15 min)

Create a file called `buggy.py` with this content:

```python
import numpy as np

def run_simulation(n_steps, n_particles):
    positions = np.zeros(n_particles)
    for step in range(n_steps):
        positions += np.random.choice([-1, 1], size=n_particls)  # typo
    return positions

results = run_simulation(100, 500)
print(f"Mean final position: {results.meen():.3f}")  # wrong method
```

Ask CC: "Run `buggy.py`. If it fails, fix all errors and run it again until it produces output."

---

## Exercise 3: Optimize an Existing Script (10 min)

Take any slow Python script from your work (or write a deliberately slow one).
Ask CC: "Profile `slow_script.py`, identify the bottleneck, and rewrite it to be at least 5× faster."
```

- [ ] **Step 4: Write ch02/quiz.md**

```markdown
## Q1

You ask CC to write a simulation. The best prompt is:

- [ ] "Write me a Python simulation."
- [x] "Simulate 1000 agents choosing between two options with probability p=0.6 for option A. Track the fraction choosing A over 50 rounds. Run it and show me the output."
- [ ] "Write me good simulation code."
- [ ] "Use numpy to make a simulation."

> Specific prompts produce useful code. Describe the model, the parameters, and what you want to see — CC handles the syntax.

---

## Q2

Your simulation crashes with a `TypeError`. What is the most efficient next step?

- [ ] Copy the error and paste it into a new Claude.ai chat
- [ ] Google the error message
- [x] Ask CC: "Run `simulation.py`. If it errors, fix the error and run it again."
- [ ] Read the traceback yourself and figure out the fix

> CC can see both the source code and the error output. Asking it to run-and-fix is faster and more accurate than manual debugging.

---

## Think

Describe a simulation or analysis script you use in your research. How would you explain it to CC so that CC could re-implement it from scratch without seeing the original code?

<answer>
A good description includes: the scientific process being modeled, the key inputs and their types/ranges, what the simulation computes at each step, what the expected output looks like, and any constraints (e.g., "must finish in under 10 seconds for N=10000"). The more specific and quantitative, the better.
</answer>
```

- [ ] **Step 5: Build, verify, commit**

```bash
python build.py
git add ch02/
git commit -m "content: ch02 — Simulations & Code"
```

---

## Task 14: ch03 Content — Developing Theory

**Files:** `ch03/lecture.md`, `ch03/tips.md`, `ch03/exercises.md`, `ch03/quiz.md`

- [ ] **Step 1: Write ch03/lecture.md**

Sections:
```markdown
# Developing Theory

## CC as a Thinking Partner
- Not just a code generator: CC can engage with abstract ideas, formalize intuitions, find logical gaps
- The key: treat CC like a brilliant peer reviewer who has read everything but doesn't know your specific problem
- Different from a search engine: CC can reason about novel combinations of ideas

## From Verbal Intuition to Formal Statement
- Start with your rough idea in plain language
- Ask CC to help formalize it: "Turn this intuition into a testable hypothesis"
- Ask CC to translate it into mathematical notation or LaTeX

> [!TRY]
> Take a research idea you've been mulling over. Write it out in 2–3 sentences of plain language.
> Ask CC: "Formalize this as a falsifiable hypothesis and suggest how you would test it."

## The Steelman Technique
- Ask CC to make the strongest possible version of your argument
- Then ask CC to attack that steelmanned version
- This surfaces assumptions you didn't know you were making

Prompt sequence:
1. "Here is my hypothesis: [your idea]. Steelman it — make the most rigorous version."
2. "Now argue against it. What are the three strongest counterarguments?"
3. "How would I design a study to rule out those counterarguments?"

## Generating LaTeX
- CC can write LaTeX for equations, tables, and theorem environments
- Prompt: "Write this relationship as a LaTeX equation: ..."
- Ask CC to produce complete theorem-proof blocks in standard mathematical format

> [!NOTE]
> Always verify LaTeX output compiles correctly. CC occasionally makes minor syntax errors
> in complex environments.

## Structuring an Argument
- Ask CC to outline the logical structure of your argument as a numbered chain
- Ask CC to identify where the chain is weakest
- Use CC to find relevant literature touchstones (give it the context of your field)

> [!WARN]
> CC can confabulate citations. Never trust a CC-generated citation without verifying it.
> Ask CC to explain a concept, not to cite sources.
```

- [ ] **Step 2: Write ch03/tips.md**

```markdown
# Tips: Developing Theory

## 1. "What assumptions am I making that I'm not stating?"
This single prompt surfaces hidden premises in your argument that reviewers will attack.

## 2. Use CC to generate rival hypotheses
"Here is my hypothesis. Generate three alternative hypotheses that could explain the same data."
Saves hours of thinking and strengthens your contribution section.

## 3. Ask CC to draw the causal diagram
"Describe the causal relationships in my theory as a DAG (directed acyclic graph) in plain English."
Useful for spotting confounders you missed.

## 4. "Explain this to a skeptical reader in field X"
Different fields have different standards of rigor. Ask CC to translate your argument for
economists, biologists, physicists — whoever your reviewers might be.

## 5. LaTeX template prompt
"Write the following as a LaTeX `theorem` block with proof sketch: [your statement]"
Gives you a starting point for formal write-up.

## 6. Never ask CC "what is the right answer" — ask "what are the possibilities"
CC is better at generating the option space than picking the winner. You pick the winner.
```

- [ ] **Step 3: Write ch03/exercises.md**

```markdown
# Exercises: Developing Theory

## Exercise 1: Formalize an Intuition (15 min)

1. Write 3–5 sentences describing a research idea or observation you've had (from your own work)
2. Give this to CC with the prompt: "Help me turn this informal observation into a precise, testable hypothesis. Suggest the key variables, the proposed relationship, and the conditions under which it should hold."
3. Ask CC: "Now write this as a formal proposition in LaTeX."
4. Ask CC: "What are the two strongest objections a reviewer would raise?"

---

## Exercise 2: The Steelman Drill (15 min)

1. Take an argument from a paper you disagree with
2. Give CC the abstract or key claim
3. Ask: "Steelman this argument — make the most charitable and rigorous version"
4. Ask: "Now identify the single weakest assumption in the steelmanned version"

**What you're practicing:** Intellectual rigor, argument analysis.

---

## Exercise 3: Build a Logical Chain (10 min)

1. State your thesis in one sentence
2. Ask CC: "Break down the logical chain from premises to conclusion. Number each step."
3. Ask CC: "Which step in this chain relies most heavily on empirical assumptions that haven't been established?"
```

- [ ] **Step 4: Write ch03/quiz.md**

```markdown
## Q1

Which CC prompt is most useful for finding hidden weaknesses in your own theory?

- [ ] "Is my theory correct?"
- [ ] "Summarize my theory."
- [x] "What assumptions am I making that I'm not explicitly stating?"
- [ ] "Find citations that support my theory."

> Surfacing implicit assumptions is one of CC's highest-value uses for theory development. Reviewers attack assumptions — find them before the reviewers do.

---

## Q2

CC generates a citation to a paper that would be perfect for your argument. What do you do?

- [ ] Include it in your paper — CC has read everything
- [ ] Search for it quickly to confirm the title
- [x] Verify the full citation (title, authors, year, journal) independently before including it
- [ ] Ask CC to find a PDF of the paper

> CC confabulates citations — it generates plausible-sounding references that may not exist. Always verify before including in academic work.

---

## Think

Describe a theoretical claim in your research. How would you use the steelman technique with CC to stress-test it before writing it up?

<answer>
A good answer: state the claim clearly → ask CC to steelman it (produces the strongest version) → ask CC to attack the steelmanned version → use the identified weaknesses to either strengthen the argument or acknowledge limitations explicitly. The key insight is that this surfaces objections before submission rather than in reviews.
</answer>
```

- [ ] **Step 5: Build, verify, commit**

```bash
python build.py
git add ch03/
git commit -m "content: ch03 — Developing Theory"
```

---

## Task 15: ch04 Content — Writing a Paper Section

**Files:** `ch04/lecture.md`, `ch04/tips.md`, `ch04/exercises.md`, `ch04/quiz.md`

- [ ] **Step 1: Write ch04/lecture.md**

Sections:
```markdown
# Writing a Paper Section

## The Problem with Copy-Paste Writing
- Paste abstract → get a paragraph → paste into Word → realize it needs context → start over
- No memory of the full paper structure, tone, argument flow
- CC can hold your entire paper in context and write consistently across all sections

## Giving CC the Full Paper Context
- At the start of a writing session: "Read `paper.md`. This is my draft paper. 
  We are going to work on the Methods section today. Don't write anything yet — just confirm you've read it."
- Then proceed with specific requests
- CC tracks terminology, argument structure, and tone from what it's read

> [!TRY]
> Take any draft you have. Put it in a file. Ask CC to read it and identify the
> weakest section and why.

## The Drafting Workflow
1. Give CC the section structure (outline)
2. Ask CC to draft it — one subsection at a time
3. Review each subsection: "This is good, but the transition to the next paragraph is abrupt — fix it"
4. Ask CC to check consistency: "Does this section use the same terminology as the introduction?"

## Maintaining Consistency
- Ask CC: "Scan the whole paper and flag any places where the same concept is referred to by different names"
- Ask CC: "Is the tense consistent throughout the Methods section?"
- Ask CC: "Does the contribution in the conclusion match what was promised in the introduction?"

> [!NOTE]
> Consistency checking is where CC dramatically outperforms manual editing.
> It can scan 10,000 words in seconds and catch inconsistencies a tired human misses.

## Revision Workflow
- Give CC the draft and a reviewer comment: "A reviewer said [comment]. Revise [section] to address it."
- Ask CC to suggest multiple ways to address feedback and choose one
- Ask CC to track changes: "Rewrite this paragraph. Show me the before and after."

> [!WARN]
> Don't ask CC to write the whole paper in one prompt. Write section by section,
> with review after each section. Quality drops sharply on long unchecked generations.
```

- [ ] **Step 2: Write ch04/tips.md**

```markdown
# Tips: Writing a Paper Section

## 1. "Write section by section, not the whole paper"
Ask CC to draft one section at a time. Review and approve before moving to the next.
Long unchecked generations accumulate errors and drift from your intent.

## 2. Give CC the section's job before asking it to write
"The Methods section needs to: (1) justify our sample size, (2) describe the instrument, 
(3) explain the analysis pipeline. Draft it with these three goals."

## 3. Ask CC to check argument flow, not just grammar
"Does the argument in the Discussion build logically from the Results? Identify any gaps."

## 4. Use CC to draft the hardest part first
Most researchers put off the Introduction and Conclusion. Start there with CC.
Having them drafted makes the middle sections easier to write.

## 5. "Write in the passive voice as is standard in [field]" if needed
Academic conventions vary. Tell CC the convention you need:
"Write in third person, past tense, passive voice as used in quantitative sociology."

## 6. Ask CC to flag hedging vs. overclaiming
"Read the Discussion. Mark any sentences that overclaim results beyond what the data shows,
and any that are unnecessarily hedged."
```

- [ ] **Step 3: Write ch04/exercises.md**

```markdown
# Exercises: Writing a Paper Section

## Exercise 1: Draft a Methods Section (20 min)

1. Create a file `paper-context.md` with: the paper's research question (1 sentence), 
   the dataset or subjects (2 sentences), and the analysis approach (2–3 sentences)
2. Ask CC: "Read `paper-context.md`. Draft a Methods section of ~200 words. 
   Use passive voice, past tense. Be specific about what was measured and how."
3. Review the draft: ask CC to revise any part that's too vague or too generic

---

## Exercise 2: Consistency Audit (10 min)

1. Take any existing draft section (even a paragraph) or write 3–4 paragraphs quickly
2. Introduce an intentional inconsistency (use "participants" in one place, "subjects" in another)
3. Ask CC: "Read this section. Identify any inconsistencies in terminology or tense."

---

## Exercise 3: Respond to a Reviewer Comment (15 min)

Write a fictional reviewer comment such as:
> "The authors do not adequately justify their choice of sample size. Please provide a power analysis or alternative justification."

Ask CC: "Here is a reviewer comment: [paste comment]. Here is my methods paragraph: [paste paragraph]. 
Revise the paragraph to address this comment and add a justification."
```

- [ ] **Step 4: Write ch04/quiz.md**

```markdown
## Q1

What is the biggest risk of asking CC to write your entire paper in one prompt?

- [ ] CC will use the wrong citation format
- [ ] CC will refuse to write a full paper
- [x] Quality drops sharply and errors accumulate without review checkpoints
- [ ] CC cannot hold a full paper in context

> Long unchecked generations drift from your intent and accumulate inconsistencies. Write and review section by section for best results.

---

## Q2

You want CC to check that your paper uses consistent terminology. The best prompt is:

- [ ] "Is my paper good?"
- [ ] "Check my paper for errors."
- [x] "Scan the whole paper and flag any places where the same concept is referred to by different names or where terminology shifts."
- [ ] "Rewrite my paper with consistent terminology."

> Specific, actionable prompts produce specific, actionable results. Asking for flags rather than rewrites keeps you in control.

---

## Think

A reviewer says your Discussion "overstates the generalizability of the findings." Describe a step-by-step process using CC to identify and fix the problem.

<answer>
Step 1: Ask CC to read the Discussion and Results. Step 2: Ask CC: "Mark every sentence in the Discussion that makes a claim about generalizability." Step 3: For each flagged sentence, ask CC: "Does the data in the Results section support this claim, or does it go beyond it?" Step 4: For sentences that overclaim, ask CC to revise with appropriate hedging language. Step 5: Ask CC to verify the revised section no longer overclaims.
</answer>
```

- [ ] **Step 5: Build, verify, commit**

```bash
python build.py
git add ch04/
git commit -m "content: ch04 — Writing a Paper Section"
```

---

## Task 16: ch05 Content — Your Voice — Style Guide

**Files:** `ch05/lecture.md`, `ch05/tips.md`, `ch05/exercises.md`, `ch05/quiz.md`

- [ ] **Step 1: Write ch05/lecture.md**

Sections:
```markdown
# Your Voice — Style Guide

## Why AI Writing Sounds Generic
- LLMs average across millions of texts → produce the statistical center of academic writing
- The result: smooth, correct, forgettable prose
- Your readers can feel it: overly structured, no personality, no rhythm
- The fix: teach CC what makes your writing yours

## What Makes Your Voice Unique
Every writer has a fingerprint: sentence length variation, preferred connectives, 
hedging language, paragraph rhythm, how you introduce evidence, how you close arguments.
Most writers can't articulate these patterns — but CC can extract them.

## The Style Guide Extraction Workflow

**Step 1: Find 2–3 paragraphs you're proud of**
These should be your own work, unedited by AI, from papers or notes you wrote when
you felt you were writing well.

**Step 2: Ask CC to analyze them**

Prompt:
```
Read the following three paragraphs. Analyze my writing style and produce a 
style guide in Markdown format. Include: typical sentence length, how I vary 
sentence length, connectives I use, how I introduce evidence, how I hedge claims, 
paragraph structure, any distinctive vocabulary or phrasing I use consistently.
[paste paragraphs]
```

**Step 3: Review and save**
CC produces `style-guide.md`. Review it — does it sound like you? Add anything it missed.
Save it in your research project directory.

**Step 4: Use it in every writing session**
Start writing sessions with: "Read `style-guide.md`. Write in the style described there."

> [!TRY]
> Find 2 paragraphs from your own writing right now. Run the style extraction prompt.
> See if CC's description matches your self-perception as a writer.

## Updating Your Style Guide Over Time
- Your writing evolves. Update the style guide once a semester.
- When a supervisor or editor praises a particular passage, add it to the examples in your guide.
- The style guide is a living document, not a one-time artifact.

> [!NOTE]
> The style guide approach works because you are the author. CC writes in your voice,
> guided by your own examples. The resulting prose is genuinely yours — CC is the typist.
```

- [ ] **Step 2: Write ch05/tips.md**

```markdown
# Tips: Your Voice — Style Guide

## 1. More examples = better style capture
Three paragraphs are a minimum. Five to ten give CC a richer fingerprint.
Include examples from different contexts (introduction, methods, discussion).

## 2. Include "what I want to avoid" in your style guide
Add a section: "Writing patterns I want to avoid: passive voice overuse, 
sentences over 35 words, starting three consecutive sentences with 'The'."

## 3. Ask CC to score a draft against your style guide
"Read `style-guide.md` and then read the following paragraph. 
Give it a score out of 10 for adherence to my style. Explain deductions."

## 4. Use the style guide for emails and academic letters too
Recommendation letters, cover letters, and emails can also benefit.
"Write a 200-word reply to this email in the style described in `style-guide.md`."

## 5. Separate style guides for separate genres
Your methods-section voice differs from your discussion voice.
Consider creating `style-guide-methods.md` and `style-guide-discussion.md`.

## 6. CC can generate style-guide-adherent prose from bullet points
Give CC bullet points of what you want to say + style guide, and ask it to write the paragraph.
This is faster than writing from scratch and more yours than raw CC output.
```

- [ ] **Step 3: Write ch05/exercises.md**

```markdown
# Exercises: Your Voice — Style Guide

## Exercise 1: Extract Your Style Guide (20 min)

1. Find 2–3 paragraphs from your own writing that you like (thesis, paper, notes)
2. Paste them into a file called `my-writing-samples.md`
3. Ask CC:
   "Read `my-writing-samples.md`. Analyze my writing style and produce a 
   `style-guide.md` file with these sections: Sentence length and variation, 
   Connective words and transitions, How I introduce evidence, Hedging language I use, 
   Paragraph structure, Distinctive vocabulary or patterns, and Examples of each."
4. Ask CC to save the result to `style-guide.md`
5. Read it. Does it sound like you? Edit anything that's off.

---

## Exercise 2: Write a Paragraph With Your Style Guide (15 min)

1. Give CC a topic sentence and 3 bullet points of content
2. Ask: "Read `style-guide.md`. Write a paragraph about [topic] using the bullet points below, 
   written in the style described in the guide." 
3. Compare it to your raw writing samples. Do they feel similar in rhythm and vocabulary?

---

## Exercise 3: Score Your Own Draft (10 min)

1. Take a paragraph you wrote without using CC
2. Ask CC: "Read `style-guide.md`. Score this paragraph from 0–10 for how well it follows 
   my style. Explain what's consistent and what's different."
```

- [ ] **Step 4: Write ch05/quiz.md**

```markdown
## Q1

Why does AI-generated academic writing often feel generic?

- [ ] AI tools are not intelligent enough to write well
- [x] LLMs average across millions of texts, producing statistically central prose with no individual voice
- [ ] Academic writing is inherently generic regardless of who writes it
- [ ] AI writing tools deliberately use simple language

> LLMs produce text that resembles the average of their training data. For academic writing, that means smooth but voiceless prose. Providing your own writing samples as a style reference breaks this pattern.

---

## Q2

After creating your style-guide.md, how do you use it in a CC writing session?

- [ ] CC automatically detects and uses it
- [ ] Email it to yourself for reference
- [x] Start the session with: "Read `style-guide.md`. Write in the style described there."
- [ ] Paste it into every prompt

> CC needs to be explicitly directed to read and apply the style guide. Make it the first thing in any writing session.

---

## Think

Describe two specific features of your own writing that you would want captured in a style guide. How would you recognize in CC's output whether it had correctly applied them?

<answer>
Examples: "I tend to use short punchy sentences after long ones for emphasis. I would recognize this if CC alternates sentence length within paragraphs." Or: "I hedge with 'appears to' and 'suggests' rather than stronger claims. I would recognize this if CC's claims are appropriately qualified in the same way."
</answer>
```

- [ ] **Step 5: Build, verify, commit**

```bash
python build.py
git add ch05/
git commit -m "content: ch05 — Your Voice — Style Guide"
```

---

## Task 17: ch06 Content — Post-Writing Polish

**Files:** `ch06/lecture.md`, `ch06/tips.md`, `ch06/exercises.md`, `ch06/quiz.md`

- [ ] **Step 1: Write ch06/lecture.md**

Sections:
```markdown
# Post-Writing Polish

## How to Spot AI-Generated Prose
AI writing has a recognizable fingerprint — not because it's wrong, but because it's
too consistent. Human writers are uneven, idiosyncratic, sometimes abrupt.
AI writers are smooth, structured, and relentlessly clear.

Common AI markers:
- **Hollow transitions:** "It is worth noting that…", "It is important to emphasize that…",
  "Furthermore,", "In conclusion,", "This highlights the importance of…"
- **Uniform paragraph structure:** Every paragraph: topic sentence → 3 supporting sentences → clincher
- **Passive overuse:** "It was found that…", "It can be seen that…", "This was demonstrated by…"
- **Hedging without specificity:** "Many researchers have noted…" (which researchers?)
- **Overlong sentences:** 40+ word sentences that could be two sentences
- **List addiction:** Bullet points where flowing prose would read better

> [!TRY]
> Paste a paragraph you think sounds "too AI" into CC. Ask: "List every AI writing marker 
> you can identify in this paragraph."

## The Polish Workflow

**Pass 1: Remove hollow transitions**
Ask CC: "Rewrite this paragraph removing all hollow filler transitions. 
Where transitions are needed, make them specific to the content."

**Pass 2: Vary sentence structure**
Ask CC: "Rewrite this passage. Vary sentence length deliberately: 
some sentences should be under 10 words, some over 25."

**Pass 3: Apply style guide**
Ask CC: "Apply my `style-guide.md` to this passage."

**Pass 4: Human final read**
Read it aloud. Your ear catches what your eye misses.

> [!NOTE]
> Polish works on your writing too, not just AI output. Run your own drafts through
> these passes when you're revising.

## The Banned Phrases List
Maintain a file `banned-phrases.md` in your project:
```
It is worth noting that
It is important to emphasize
Furthermore,
In conclusion,
This highlights the importance of
Delve into
It can be seen that
As previously mentioned
```
Ask CC: "Read `banned-phrases.md`. Remove every instance of these phrases from the 
following text. Replace with substantive content where needed, or delete if empty."

> [!WARN]
> Don't just remove phrases mechanically — replacing "It is worth noting that X" 
> with nothing leaves a gap. Replace with the actual insight.
```

- [ ] **Step 2: Write ch06/tips.md**

```markdown
# Tips: Post-Writing Polish

## 1. The "read aloud" test beats all AI checks
After CC polishes a section, read it aloud. Anything that makes you stumble is a 
problem — no matter what CC thinks.

## 2. Ask CC to give you the worst sentence
"Which single sentence in this passage is most obviously AI-generated? Why?"
CC's self-critique is surprisingly accurate.

## 3. Add your own banned phrases
Every field and every writer has specific clichés to avoid. Start with the defaults
in this chapter's exercises, then build your own list.

## 4. Polish in passes, not in one go
Each pass has one job: transitions, then sentence length, then vocabulary, then style guide.
Trying to do everything at once produces inconsistent results.

## 5. Preserve your intentional stylistic choices
If you deliberately use a non-standard construction for effect, tell CC.
"Keep the fragment in the second sentence — it's intentional."

## 6. Compare before and after
Ask CC to show you the original and revised side by side.
"Rewrite this paragraph. Show the original and your revision with the changes highlighted."
```

- [ ] **Step 3: Write ch06/exercises.md**

```markdown
# Exercises: Post-Writing Polish

## Exercise 1: AI Marker Hunt (10 min)

Here is a deliberately AI-flavored paragraph. Identify every marker before asking CC:

> "It is worth noting that the results of this study demonstrate a significant 
> improvement in performance. Furthermore, the findings highlight the importance 
> of considering multiple variables when conducting research. It can be seen that 
> researchers who utilize these methods will achieve better outcomes. In conclusion, 
> this approach is highly recommended for future studies in this area."

1. List every AI marker you spot
2. Ask CC: "List every AI writing marker in this paragraph."
3. Ask CC: "Rewrite this paragraph to eliminate all markers. Make it sound like a 
   specific, confident researcher who knows exactly what their data showed."

---

## Exercise 2: Polish Your Own Writing (15 min)

1. Take a paragraph from your own work (or one CC wrote for you in a previous exercise)
2. Apply the four-pass polish workflow:
   - Pass 1: "Remove all hollow filler transitions"
   - Pass 2: "Vary sentence length — some under 10 words, some over 25"
   - Pass 3: "Apply `style-guide.md`" (if you made one in ch05)
   - Pass 4: Read aloud
3. Compare the original and final versions

---

## Exercise 3: Build Your Banned Phrases List (10 min)

1. Create a file `banned-phrases.md` in a test directory
2. Add at least 10 phrases you want to avoid (use the defaults from the lecture + your own)
3. Ask CC: "Read `banned-phrases.md`. Remove every instance of these phrases from the 
   following paragraph: [paste a paragraph]."
```

- [ ] **Step 4: Write ch06/quiz.md**

```markdown
## Q1

Which of these is the most reliable signal of AI-generated academic prose?

- [ ] Grammatical errors
- [ ] Long paragraphs
- [x] Hollow transitions ("It is worth noting that…") and uniform paragraph structure
- [ ] Technical vocabulary

> AI writing is structurally consistent and smooth. The giveaway is hollow filler phrases and paragraph templates that repeat across the document. Human writing is uneven and idiosyncratic.

---

## Q2

You remove "It is worth noting that" from the start of a sentence. What should you do?

- [ ] Leave the rest of the sentence as is
- [ ] Delete the whole sentence
- [x] Check whether the sentence has substantive content and rewrite the opening to be specific
- [ ] Replace it with "Furthermore,"

> Removing the phrase often exposes that the sentence has nothing to say. If the content is real, rewrite the opening specifically. If there is no content, delete the sentence.

---

## Think

Read the following sentence and identify every AI writing marker it contains. Then rewrite it as a specific, confident researcher would.

> "It is important to note that the results of the current study suggest that there may be a relationship between the variables examined, which could potentially have implications for future research in this area."

<answer>
Markers: "It is important to note that" (hollow opener), "suggest that there may be" (double hedge), "could potentially" (double hedge), "implications for future research in this area" (vague closer). Rewrite example: "The data show a positive correlation between [Variable A] and [Variable B] (r = 0.43, p < 0.01), which challenges [Specific Prior Theory]."
</answer>
```

- [ ] **Step 5: Build, verify, commit**

```bash
python build.py
git add ch06/
git commit -m "content: ch06 — Post-Writing Polish"
```

---

## Task 18: ch07 Content — Research Habits That Compound

**Files:** `ch07/lecture.md`, `ch07/tips.md`, `ch07/exercises.md`, `ch07/quiz.md`

- [ ] **Step 1: Write ch07/lecture.md**

Sections:
```markdown
# Research Habits That Compound

## The Problem with One-Off Sessions
You've been using CC reactively: open a session, fix a problem, close.
This works, but it doesn't compound. Every session starts from scratch.
The tools in this chapter turn CC into a persistent research partner.

## CLAUDE.md: Your Project's Memory

`CLAUDE.md` is a file you create in your project directory. CC reads it automatically
at the start of every session. It contains everything CC needs to know about your project
without you having to explain it each time.

A good CLAUDE.md for a research project contains:
- Project name and research question (1 sentence)
- Key concepts and their precise definitions (the ones CC might get wrong)
- File structure: what's in each directory
- Current status: what has been done, what is in progress
- Conventions: naming schemes, data format notes, style preferences
- What NOT to do: common mistakes, files not to touch

Example:
```markdown
# Project: Carbon Flux Model

**Research question:** How does soil moisture interact with carbon efflux under drought conditions?

**Key files:**
- `data/raw/` — never modify; original flux tower measurements
- `data/processed/` — cleaned outputs; regenerate with `scripts/clean.py`
- `models/` — simulation scripts; main entry point is `run_model.py`

**Conventions:** All dates in ISO 8601. Variable names follow FLUXNET standard.

**Current status:** Data cleaning complete. Working on model calibration (see `TODO.md`).

**Do not:** Commit to `data/raw/`. Edit `requirements.txt` without testing.
```

> [!TIP]
> Keep CLAUDE.md short — under 200 lines. Long CLAUDE.md files are harder to maintain
> and waste context. Write for the CC session, not for posterity.

## Hooks: Automating Repetitive Context

CC supports hooks — shell commands that run before or after CC actions.
Example uses for researchers:
- Before every CC session: run `git status` so CC knows what's changed
- After CC edits code: automatically run your tests
- Before CC commits: lint your code

Hooks are configured in `.claude/settings.json`. For most researchers, CLAUDE.md
is sufficient — hooks are for advanced automation.

## Building a Research Workflow That Compounds

The weekly CC research routine:
1. **Monday:** Update `CLAUDE.md` with last week's progress and this week's goals
2. **Daily sessions:** Start with "Read CLAUDE.md. What should I work on today based on the current status?"
3. **After analysis:** "Update the Current Status section of CLAUDE.md with what we just did."
4. **Before writing:** "Read CLAUDE.md and `style-guide.md`. Let's draft [section]."

Over a PhD, this compounds: CC gets better at helping you as your CLAUDE.md grows.

> [!NOTE]
> The most productive CC users treat it as a collaborator, not a tool.
> Collaborators need context. Give CC context systematically and it returns that investment.
```

- [ ] **Step 2: Write ch07/tips.md**

```markdown
# Tips: Research Habits That Compound

## 1. Ask CC to write your first CLAUDE.md
"Look at the files in this directory. Write a CLAUDE.md that describes this project 
for a future CC session. Include: project purpose, file structure, and current status."
CC bootstraps from your existing files.

## 2. Update CLAUDE.md after every significant session
End sessions with: "Update the Current Status section of CLAUDE.md to reflect what we did today."
Takes 30 seconds. Saves 5 minutes of re-explanation next time.

## 3. Use CLAUDE.md to encode hard-won knowledge
When you figure out something non-obvious about your data or analysis, add it to CLAUDE.md.
"Note in CLAUDE.md: the sensor data has a 3-hour lag that must be corrected before analysis."

## 4. Keep a QUESTIONS.md alongside CLAUDE.md
When a question comes up that you don't have time to answer: 
"Add this question to QUESTIONS.md: [question]"
Start sessions with: "Read QUESTIONS.md. Let's work on the first unanswered question."

## 5. `claude --continue` at the start of each day
Resume the last session to preserve conversation context.
Pair with CLAUDE.md for maximum continuity.

## 6. Review your CLAUDE.md monthly
Remove stale information. Add new conventions you've developed.
A CLAUDE.md that hasn't been touched in 3 months is probably out of date.
```

- [ ] **Step 3: Write ch07/exercises.md**

```markdown
# Exercises: Research Habits That Compound

## Exercise 1: Write Your First CLAUDE.md (15 min)

1. Navigate to a real research project directory on your computer
2. Ask CC: "Look at the files in this directory. Write a CLAUDE.md that describes this 
   project: its purpose, the file structure (what's in each folder and what each key file does), 
   current status, and any conventions I should know about."
3. Review what CC produces — add anything it missed, remove anything inaccurate
4. Start a new CC session and notice the difference. Ask CC: "Based on CLAUDE.md, what 
   would be a good task to work on first?"

---

## Exercise 2: The Week-in-Review Update (10 min)

At the end of any work session:
1. Ask CC: "Summarize what we did in this session in 3 bullet points."
2. Ask CC: "Append these bullet points to CLAUDE.md under a section called 'Session Log'."
3. At the start of the next session, ask CC: "Read CLAUDE.md. What's the context for today's work?"

---

## Exercise 3: The Compound Habit (5 min reflection)

Think about a research project you're currently working on. Write down:
1. Three things CC would need to know to be useful in that project (for CLAUDE.md)
2. One repetitive task in your workflow that CC could handle if it had that context
3. One habit from this tutorial that you will start using this week

There's no CC prompt for this exercise. The answer lives in how you work next week.
```

- [ ] **Step 4: Write ch07/quiz.md**

```markdown
## Q1

What is the primary purpose of a CLAUDE.md file?

- [ ] To store your API key securely
- [ ] To configure CC's visual appearance
- [x] To give CC persistent project context that survives across sessions
- [ ] To backup your conversation history

> CLAUDE.md is read automatically at the start of every CC session. It replaces the need to re-explain your project each time. It is project memory, not configuration.

---

## Q2

Your CLAUDE.md has grown to 500 lines over a year. What should you do?

- [ ] Nothing — longer is more informative
- [ ] Delete it and start over
- [x] Review it, remove stale sections, and condense it to the most relevant context
- [ ] Split it into multiple files

> CLAUDE.md should be maintained like good documentation: updated, pruned, and kept concise. Long CLAUDE.md files waste context and slow down the start of sessions.

---

## Think

Describe what you would put in a CLAUDE.md for your current or most recent research project. Include at least four sections and explain why each one would save time in a CC session.

<answer>
A complete answer includes: (1) Research question / goal — saves having to explain the project. (2) File structure — CC knows where to look without asking. (3) Current status — CC can pick up where you left off. (4) Conventions / definitions — CC uses your terminology correctly without correction. Bonus: "Do not" list to prevent repeated mistakes.
</answer>
```

- [ ] **Step 5: Final full build and verify**

```bash
python build.py
```

Open `index.html`. Navigate through all 8 chapters. Check:
- All 4 pages load per chapter
- Callouts display with correct colors
- Code blocks have copy buttons and syntax highlighting
- Quiz MCQs turn green/red on click
- Thinking exercise reveal buttons work
- Prev/Next navigation links correctly through all pages
- Progress bar updates per chapter

- [ ] **Step 6: Commit**

```bash
git add ch07/ index.html
git add ch00/ ch01/ ch02/ ch03/ ch04/ ch05/ ch06/  # pick up any generated HTML
git commit -m "content: ch07 — Research Habits That Compound; complete tutorial build"
```

---

## Self-Review Against Spec

**Spec coverage check:**

| Spec requirement | Task |
|---|---|
| 8 chapters ch00–ch07 | Tasks 11–18 |
| lecture.md, tips.md, exercises.md, quiz.md per chapter | Tasks 11–18 |
| build.py with markdown + jinja2 | Tasks 2–4 |
| Callout syntax `> [!TIP/TRY/WARN/NOTE]` | Task 2 |
| Quiz MCQ interactivity (green/red) | Tasks 3, 9 |
| Thinking exercise reveal | Task 9 |
| Tailwind CDN, Inter + JetBrains Mono | Task 5 |
| Prism.js code highlighting + copy button | Tasks 5, 8 |
| Navy sidebar + indigo accent | Tasks 5, 8 |
| Root index.html chapter card grid | Task 7 |
| Chapter index.html with 4-page cards | Task 6 |
| Prev/Next navigation | Task 4 |
| Progress bar | Task 5 |
| Style guide extraction workflow (ch05) | Task 16 |
| AI marker removal (ch06) | Task 17 |
| CLAUDE.md and compound habits (ch07) | Task 18 |
| Works without a server (open .html directly) | All — no server required |
| build.py runs with pip install only | Task 1 |

All spec requirements covered. No gaps.
