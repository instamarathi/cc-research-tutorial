# Claude Code Tutorial — Design Spec

**Date:** 2026-05-01  
**Status:** Approved

---

## Overview

A self-paced, locally-hosted HTML tutorial teaching researchers how to use Claude Code (CC) as a research superpower. The target student already writes Python, uses ChatGPT/Claude.ai for copy-paste code generation, but has never used Claude Code. The tutorial's core narrative is: *you've been using a calculator when you could have been using a computer*.

---

## Audience

- PhD students in any field
- Comfortable with Python; not a software engineer
- Familiar with AI assistants (ChatGPT, Claude.ai) via copy-paste
- No prior experience with Claude Code CLI
- Domain-agnostic: examples are generic enough that any researcher can adapt them

---

## Output Format

A folder-based repo where each chapter is a directory. A Python build script (`build.py`) converts Markdown source files into styled HTML. Output works by opening `.html` files directly in a browser — no server required. Later exportable to GitHub Pages by pushing the generated HTML files.

---

## Chapter Structure

8 chapters, ~30–45 min each. Each chapter folder contains 4 files:

| File | Purpose |
|------|---------|
| `lecture.md` | Core teaching content with inline callouts and "Try It" prompts |
| `tips.md` | Practical shortcuts, prompt patterns, and CC-specific tricks |
| `exercises.md` | Hands-on tasks the student completes themselves in CC |
| `quiz.md` | MCQ and thinking exercises to consolidate the chapter |

### Chapters

| Folder | Title | Core Concept |
|--------|-------|-------------|
| `ch00` | Welcome & The Superpower | Why CC ≠ copy-paste AI. Installation, first run, mental model shift. |
| `ch01` | Your First Research Session | File context, reading papers/data with CC, iterative dialogue. |
| `ch02` | Simulations & Code | Writing, running, debugging simulation code — CC as coding partner in your project directory. |
| `ch03` | Developing Theory | Formalizing ideas, pressure-testing logic, generating LaTeX, structuring arguments with CC. |
| `ch04` | Writing a Paper Section | Drafting, revising, maintaining flow and consistency across a full paper with CC. |
| `ch05` | Your Voice — Style Guide | Feed CC handwritten prose → extract personal style guide → use it for all future writing. |
| `ch06` | Post-Writing Polish | Remove AI markers, vary sentence structure, inject authentic scholarly voice. |
| `ch07` | Research Habits That Compound | `CLAUDE.md`, memory, hooks, project-level workflows that improve over time. |

---

## Repository Structure

```
cc-tutorial/
├── build.py                  # Converts .md → .html via Jinja2 templates
├── index.html                # Root table of contents (generated)
├── assets/
│   ├── style.css             # Shared styles (Tailwind overrides + custom)
│   ├── prism.css             # Code highlighting (One Dark theme)
│   └── prism.js              # Syntax highlighting library
├── templates/
│   ├── base.html             # Base layout: sidebar nav, top bar, fonts
│   ├── lecture.html
│   ├── tips.html
│   ├── exercises.html
│   └── quiz.html
├── ch00/
│   ├── lecture.md
│   ├── tips.md
│   ├── exercises.md
│   ├── quiz.md
│   └── index.html            # Generated chapter landing page
├── ch01/ … ch07/             # Same structure
└── docs/
    └── superpowers/specs/
        └── 2026-05-01-phd-tutorial-design.md
```

---

## Build System

`build.py` responsibilities:
1. Walk each `chXX/` directory
2. Parse each `.md` file using Python `markdown` library (with `fenced_code`, `tables`, `toc` extensions)
3. Render parsed HTML into the appropriate Jinja2 template
4. Write output `.html` files in-place alongside the `.md` sources
5. Generate root `index.html` as a chapter card grid (title, description, estimated time)

**Dependencies:** `markdown`, `jinja2` — both installable via `pip`. No Node.js required.

**Usage:**
```bash
pip install markdown jinja2
python build.py
# Open ch00/lecture.html in browser
```

---

## Visual Design

| Element | Spec |
|---------|------|
| Prose font | Inter (Google Fonts CDN) |
| Code font | JetBrains Mono (Google Fonts CDN) |
| Background | `#f9f8f6` (warm off-white) |
| Sidebar | `#1a1f2e` (dark navy), fixed position |
| Accent | `#6366f1` (indigo) for links and active states |
| Code blocks | Prism.js One Dark theme, copy-to-clipboard button |
| Layout | Sidebar (240px fixed) + content area (max-width 760px, centered) |
| Top bar | Chapter title + thin progress bar |

### Callout Box Types

| Type | Trigger | Border Color |
|------|---------|-------------|
| `💡 Tip` | `> [!TIP]` | Soft yellow `#fbbf24` |
| `⚡ Try It` | `> [!TRY]` | Green `#22c55e` |
| `⚠️ Watch Out` | `> [!WARN]` | Orange `#f97316` |
| `🔬 Research Note` | `> [!NOTE]` | Blue `#3b82f6` |

### Navigation

- Left sidebar: chapter list with active chapter expanded, showing its 4 pages
- Bottom of every page: ← Prev / Next → buttons
- Sidebar collapses on narrow viewports (mobile-friendly)

### Quiz Interactivity (pure JS, no backend)

- MCQ: options rendered as clickable cards; correct answer turns green, wrong turns red, with brief explanation revealed on click
- Thinking exercises: open `<textarea>` + "Reveal suggested answer" toggle button

---

## Post-Writing Humanization Workflow (ch05–ch06)

**Style guide extraction (ch05):**
1. Student pastes 2–3 paragraphs of their own handwritten prose into CC
2. CC analyzes and produces a `style-guide.md`: sentence length, vocabulary level, transition patterns, paragraph rhythm, preferred hedging language, field-specific conventions
3. Student stores `style-guide.md` in their research project directory
4. CC references it for all future writing in that project

**AI marker removal (ch06):**
- Teach student to spot common AI patterns: overlong sentences, hollow transitions ("It is worth noting that…"), passive overuse, uniform paragraph length, missing hedging specificity
- Exercises: student pastes an AI-generated paragraph and iteratively prompts CC to revise using the style guide
- Tips file includes a "banned phrases" starter list students can customize

---

## Success Criteria

- A student with zero CC experience completes ch00 and runs their first CC session within 30 minutes
- By ch02, the student has used CC to write and debug a real simulation or data script in their own project
- By ch05, the student has a working `style-guide.md` that produces noticeably more personal writing output
- The HTML renders correctly in Chrome, Firefox, and Safari with no server
- `build.py` runs with a clean `pip install` and no other dependencies
