# Your First Research Session

## What "Context" Means for CC

When you start Claude Code, you are opening a conversation that lives in a single terminal session. CC does not automatically know what you are working on — you have to tell it, and the primary way you do that is by pointing it to files.

CC can read plain text, CSV, Python scripts, Markdown notes, and most structured data formats directly. It cannot open a PDF on its own.

> [!NOTE]
> CC cannot open PDFs directly. Before feeding a paper into CC, convert it first:
> ```
> pdftotext paper.pdf paper.txt
> ```
> Then tell CC: `Read paper.txt`.

CC holds roughly 200,000 tokens of context — enough for a long paper, a moderate dataset description, and your conversation so far. That sounds large, but it fills up. Be selective: give CC the files most relevant to today's specific task, not your entire project folder.

Useful file types to drop into a session:

- **CSV files** — CC will read column names, spot missing values, and describe distributions
- **Python scripts** — CC can read, modify, run, and debug them in the same session
- **Text notes** — bullet points, hypotheses, literature summaries
- **Extracted paper text** — from `pdftotext` or exported from a reference manager

## The Research Dialogue Pattern

The mistake most new CC users make is treating it like a search box: one big prompt, wait, copy the output. That misses most of the value.

Think of CC as a research collaborator sitting next to you. You would not hand a collaborator a stack of papers and say "summarize all of this." You would start a conversation: *What is this about? What stands out to you? Wait — what did you mean by that?*

A productive research session flows like this:

1. **Orient** — Give CC the relevant files and ask for a brief overview. "Read data/survey.csv. What is the structure and what stands out?"
2. **Narrow** — Follow up on one thread. "You mentioned missing values in column 3 — how many rows are affected?"
3. **Generate** — Ask CC to produce something: a script, a summary paragraph, a table.
4. **Challenge** — Push back on outputs that seem off. "I don't think that's right — re-check the calculation."
5. **Capture** — Save anything worth keeping. "Write your summary to notes/session-2026-05-01.md."

Each step builds on the one before. The dialogue is the research.

> [!TRY]
> Open CC with a paper or dataset you are currently working with. Ask:
> "What are the three most important things I should know about this?"
>
> Do not edit the prompt. See what CC notices, then decide what to ask next.

## Reading and Analyzing Data

For any unfamiliar dataset, start with structure before substance:

```
Read data/responses.csv. Describe the columns, data types, and any obvious quality issues.
```

CC will tell you column names, likely data types, row counts, and flag things like blank cells or mixed formats. From there you can dig in:

- "Which variables have the most missing data?"
- "Are there any rows that look like duplicates?"
- "What is the range and mean of the response_time column?"

CC can also write a Python exploration script right in the session:

```
Write a Python script using pandas to plot the distribution of response_time. Save the figure as figures/response_dist.png.
```

Run it immediately with `uv run python explore.py` and the figure is on disk within seconds. You have gone from raw CSV to a distribution plot in under two minutes — all through conversation.

> [!WARN]
> CC can make mistakes, especially with numerical reasoning. Always verify quantitative claims. If CC says "the mean is 4.7", check it yourself with a one-liner before trusting it in a paper. CC is good at identifying *what* to look at; you own the verification.

## Iterative Questioning

The power of CC is not in the first prompt — it is in the follow-ups.

Here are some of the most useful follow-up patterns:

| Situation | Follow-up prompt |
|---|---|
| Something interesting | "That's interesting — show me the distribution of that variable." |
| A number seems off | "I don't believe that figure — re-check your calculation step by step." |
| An unexplained result | "What are three plausible explanations for that outlier?" |
| Output is too long | "Give me a three-sentence version." |
| Output is too vague | "Be more specific — give me an example from the data." |
| Logical gap | "You jumped from X to Y — what is the reasoning in between?" |

The iterative loop is what separates a shallow scan from genuine analysis. Budget most of your session time for follow-ups, not the opening prompt.

## Ending and Resuming Sessions

When you are done, press **Ctrl+C** to exit. Your conversation history is not automatically saved — only what you have written to files persists.

To pick up where you left off, use:

```bash
claude --continue
```

This reopens the most recent session with its conversation history intact. Use it immediately after a break; if you start a fresh `claude` session instead, CC will not remember the previous conversation.

**Key limitation:** conversation memory does not carry over to a brand new session. If you close the terminal and open a new one, `claude` starts blank. Chapter 07 covers CLAUDE.md — a project-level file that gives CC persistent context every time it starts, so you never have to re-explain your project from scratch.

For now, the habit to build is: at the end of a productive session, ask CC to write a short summary of what you did and what is left to do, and save it to a notes file. That file becomes your bridge to the next session.
