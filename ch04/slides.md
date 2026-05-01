# Writing a Paper Section

## The Problem with Copy-Paste Writing

- **Stateless chat** knows nothing about your prior paragraphs, field terminology, or argument
- Generated prose is **locally fluent but globally incoherent** — sounds like your paper, doesn't belong in it
- You spend more time editing AI output than writing from scratch
- **Claude Code holds your entire manuscript in context** across the whole session
- Reads, tracks, and stays consistent — not a paragraph dispenser

## Giving CC the Full Paper Context

- **Load the manuscript before writing a single word**
- Opening prompt: ask CC to read the file, then restate the central argument in one sentence
- If the summary is off, **correct CC's understanding before drafting begins**
- Once context is set, subsequent prompts ("draft next subsection") resolve against the full manuscript
- For long projects, keep a **`context.md`** with: research question, contribution, terminology conventions, per-section goals
- Open every session: ask CC to read both `paper.md` and `context.md`

## Example: Loading the Project

- **Opening prompt** loads all three project artifacts at once:
  `Read weather_exercise/data/daily_steps.csv, analysis.py, and blog_outline.md`
- Ask CC to summarize the central claim in one sentence — **verify before drafting**
- Sample confirmation prompt: `"The blog argues that rainy days cause a ~28% step reduction. Does your reading of analysis.py support that?"`
- If analysis outputs differ from the outline, **resolve the discrepancy before writing prose**
- Keep a `context.md` noting: metric = daily steps, n = 50 participants × 180 days, tone = accessible science blog, target reader = general fitness audience

## The Drafting Workflow

- **Step 1 — Frame the section's job** before asking for prose (e.g., "justify sample size, describe instrument, explain pipeline")
- **Step 2 — Draft one subsection at a time**; read it before requesting the next
- **Step 3 — Revise through conversation** with specific feedback ("transition is too abrupt — add a bridging sentence")
- **Step 4 — Check consistency** after completing a section ("does terminology here match the Introduction?")
- Vague requests get vague revisions — **be specific**
- ⚡ Diagnose first: ask CC "which section is weakest and why?" to find where to start revising

## Example: Drafting the Results Section

- **Prompt:** `"Draft the Results section. Cover: rainy-day step average, % drop vs dry days, p-value, temperature effect size. Tone: accessible but precise. Max 3 short paragraphs."`
- CC produces a grounded excerpt anchored in the actual numbers:
  ```
  On rainy days, participants averaged 6,240 steps — 28% fewer than on dry days
  (p < 0.001). Temperature had a smaller but significant effect: each 10 °F drop
  below 60 °F was associated with ~400 fewer steps (p = 0.03).
  ```
- **Review immediately:** check that percentages and p-values match `analysis.py` output before proceeding
- If the tone drifts academic, prompt: `"Rewrite keeping the numbers exact but aimed at a reader who has never seen a p-value"`
- Draft the next subsection only after the previous one is locked — **one subsection at a time**

## Maintaining Consistency

- Terminology **drifts across sessions**: "participants" → "subjects" → "respondents"
- Tense shifts, and promised contributions diverge between Introduction and Conclusion
- These errors are cognitively expensive for humans to catch — **trivial for CC**
- Ask CC to: **flag concept name drift**, check tense consistency, quote matching claims from Introduction and Conclusion
- 💡 Run a **full consistency audit before every submission**, not just at end of drafting

## Revision Workflow

- Peer review comments are **structured, specific writing problems** — use them as prompts
- Prompt structure: paste exact reviewer quote → ask for **three revision approaches** with tradeoffs
- Three options prevents anchoring; you get minimal fix, substantive revision, structural rethinking
- Follow up with a **before/after comparison** to verify the fix doesn't introduce new problems
- For unclear comments, ask CC to **interpret the reviewer's likely meaning** before attempting a revision
