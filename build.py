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
