# Your First Research Session

## What "Context" Means for CC

- CC knows nothing at session start — you must **point it to files**
- Reads plain text, CSV, Python scripts, Markdown, and most structured formats
- 💡 CC cannot open PDFs directly — convert first: `pdftotext paper.pdf paper.txt`
- Context window is ~**200,000 tokens** — large but finite; be selective
- Give CC files relevant to **today's task**, not your entire project folder
- Most useful types: CSV data, Python scripts, text notes, extracted paper text

## The Research Dialogue Pattern

- Mistake: treating CC like a search box — one big prompt, copy output, done
- Think of it as a **research collaborator**: start a conversation, not a transaction
- Five-step flow:
  - **Orient** — give files, ask for overview
  - **Narrow** — follow up on one thread
  - **Generate** — ask for a script, summary, or table
  - **Challenge** — push back on outputs that seem off
  - **Capture** — write anything worth keeping to a file
- ⚡ Try: ask *"What are the three most important things I should know about this?"* — don't edit the prompt, see what CC notices

## Reading and Analyzing Data

- Start with **structure before substance** — ask for columns, types, and quality issues first:

```
Read data/responses.csv. Describe the columns, data types,
and any obvious quality issues.
```

- Follow-up questions that pay off fast:
  - "Which variables have the **most missing data**?"
  - "Are there any **duplicate rows**?"
  - "What is the range and mean of `response_time`?"
- Ask CC to write and run an exploration script — raw CSV to distribution plot in under **2 minutes**
- ⚠️ Always **verify quantitative claims** yourself — CC can make numerical mistakes

## Example: Reading the Weather Data

- Open prompt — **orient CC to the dataset:**

```
Read data/daily_steps.csv. Describe the columns, data types,
and any quality issues you notice.
```

- CC reports: 9,000 rows, 5 columns, no nulls, `date` parsed as string — flags that `date` should be converted to datetime
- CC spots without being asked: **"Steps drop roughly 30% on days where precipitation_mm > 0"** and **"a sharp step-count decline below 5°C"**
- Follow-up to narrow in: *"Is the rain effect consistent across all 50 people, or driven by a few outliers?"*
- CC finds 8 people show almost no rain effect — prompts the natural next question: *"What separates those 8 from the rest?"*
- Ask CC to **write and run** an exploration script: `"Write a script that plots mean daily steps by 5°C temperature bucket and save it to figures/steps_by_temp.png"`
- ⚡ This entire dialogue — from raw CSV to a hypothesis worth writing about — takes under **10 minutes**

## Iterative Questioning

- The power of CC is in the **follow-ups**, not the first prompt
- High-value follow-up patterns:

| Situation | What to ask |
|---|---|
| Interesting finding | "Show me the **distribution** of that variable." |
| Number seems off | "Re-check that calculation **step by step**." |
| Unexplained result | "Give me **three plausible explanations**." |
| Output too long | "Give me a **three-sentence version**." |
| Output too vague | "Give me a **specific example** from the data." |

- Budget most session time for **follow-ups**, not the opening prompt

## Ending and Resuming Sessions

- **Ctrl+C** to exit — conversation history is not automatically saved
- Only what you've written to **files** persists between sessions
- Resume the most recent session with:

```bash
claude --continue
```

- A fresh `claude` starts **blank** — previous conversation is gone unless you used `--continue`
- Build this habit: before ending, ask CC to **write a session summary** to a notes file
- That notes file becomes your bridge to the next session (Chapter 07 covers CLAUDE.md for permanent project context)
