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


def extract_callouts(text: str) -> tuple:
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


def parse_quiz(text: str) -> list:
    """Parse quiz.md into a list of question dicts for template rendering."""
    questions = []
    blocks = re.split(r'\n---\n', text.strip())
    for block in blocks:
        block = block.strip()
        if not block:
            continue
        # Thinking exercise: has <answer> tag
        if '<answer>' in block:
            answer_m = re.search(r'<answer>\s*(.*?)\s*</answer>', block, re.DOTALL)
            answer = answer_m.group(1).strip() if answer_m else ''
            # Remove heading line and answer block to get question text
            body = re.sub(r'<answer>.*?</answer>', '', block, flags=re.DOTALL)
            body = re.sub(r'^##\s+Think\s*\n', '', body).strip()
            questions.append({
                "type": "think",
                "question": body,
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
                text_val = re.sub(r'^- \[[ x]\]\s*', '', opt).strip()
                options.append({"text": text_val, "correct": correct})
            if options:
                questions.append({
                    "type": "mcq",
                    "question": '\n'.join(question_lines).strip(),
                    "options": options,
                    "explanation": ' '.join(explanation_lines).strip(),
                })
    return questions


def parse_slides(text: str) -> list:
    """Split lecture.md into slide dicts, one per ## section."""
    slides = []
    parts = re.split(r'^(## .+)$', text, flags=re.MULTILINE)
    for i in range(1, len(parts), 2):
        heading = parts[i][3:].strip()
        body = parts[i + 1] if i + 1 < len(parts) else ''
        slides.append({"title": heading, "html": render_md(body.strip())})
    return slides


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

        # Build slides from slides.md (falls back to lecture.md)
        slides_src_path = chapter_dir / 'slides.md'
        if not slides_src_path.exists():
            slides_src_path = chapter_dir / 'lecture.md'
        if slides_src_path.exists():
            slides = parse_slides(slides_src_path.read_text(encoding='utf-8'))
            slides_tmpl = env.get_template('slides.html')
            slides_out = slides_tmpl.render(
                chapter=chapter,
                chapter_index=i,
                slides=slides,
            )
            (chapter_dir / 'slides.html').write_text(slides_out, encoding='utf-8')

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


def _prev_page(chapter_index: int, page_type: str) -> dict:
    page_order = PAGE_TYPES
    pi = page_order.index(page_type)
    if pi > 0:
        return {"chapter": CHAPTERS[chapter_index], "page": page_order[pi - 1]}
    if chapter_index > 0:
        return {"chapter": CHAPTERS[chapter_index - 1], "page": page_order[-1]}
    return None


def _next_page(chapter_index: int, page_type: str) -> dict:
    page_order = PAGE_TYPES
    pi = page_order.index(page_type)
    if pi < len(page_order) - 1:
        return {"chapter": CHAPTERS[chapter_index], "page": page_order[pi + 1]}
    if chapter_index < len(CHAPTERS) - 1:
        return {"chapter": CHAPTERS[chapter_index + 1], "page": page_order[0]}
    return None


if __name__ == '__main__':
    build()
