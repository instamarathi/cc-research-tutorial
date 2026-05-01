# Your Voice — Style Guide

## Why AI Writing Sounds Generic

- LLMs are trained to produce **statistically central prose** — the average of millions of texts
- Output is grammatically clean, structurally correct, and **completely forgettable**
- No rhythm, no personality, no characteristic way of building an argument
- Reviewers and supervisors **feel it immediately**, even if they can't name it
- Solution: don't avoid CC for writing — **teach CC your voice**

## What Makes Your Voice Unique

- Your fingerprint lives in **small decisions made dozens of times per paragraph**
- Sentence length variation, pivot words ("however" vs. "yet" vs. "but"), how you introduce evidence
- **Hedging patterns**: "appears to" vs. "may" vs. "it is worth noting that"
- How you open and close paragraphs; the vocabulary you reach for
- These patterns are **consistent and encoded in your own texts** — CC can extract them

## The Style Guide Extraction Workflow

- **Step 1:** Find 2–3 paragraphs you are proud of from your own unedited work
- **Step 2:** Save them to `my-writing-samples.md`
- **Step 3:** Run the extraction prompt — ask CC to produce `style-guide.md` covering sentence length, connectives, evidence framing, hedging, paragraph structure, vocabulary
- **Step 4:** Review carefully — CC gets broad strokes right, may miss finer texture; **add and delete as needed**
- **Step 5:** Save `style-guide.md` in your project directory (keep a copy in your home research folder)
- **Step 6:** Start every writing session with `Read style-guide.md. Write in the style described there.`
- ⚡ Try now: paste 2 paragraphs and run the extraction — does CC's description match your self-perception?
- 💡 More samples = better capture; 5–10 paragraphs from varied contexts (intro, methods, discussion) beats 2–3

## Example: Applying Voice to the Blog

- CC's **generic draft** (before style guide):
  `"Rainy weather has been shown to negatively impact physical activity levels among study participants."`
- **After** loading `style-guide.md` and rewriting:
  `"When it rains, people move less — 28% less, in fact. That's not a rounding error; that's a skipped workout."`
- What changed: **sentence length halved**, hedging stripped ("has been shown" → stated directly), **em-dash rhythm** introduced, concrete number pulled forward
- The style guide told CC: short declarative sentences, lead with the finding, use plain verbs, avoid passive constructions
- **Prompt that produced the rewrite:** `"Read style-guide.md. Rewrite the following sentence in my style, keeping all numbers exact: [paste draft sentence]"`

## Using the Style Guide

- Invoke the style guide **explicitly at the start of every writing task**
- Effective prompt: read style-guide + bullet-point content + task = prose in your style
- Key reuse prompts:
  - **"Rewrite this paragraph in my style"** — fixes generic-sounding drafts
  - **"Score this paragraph 0–10 for adherence to my style"** — reviews your own drafts
  - **"Does this abstract sound like me?"** — quick gut-check before submission
- The style guide is a **living document**: add praised passages, update when your writing evolves, revisit once a semester

## Why This Is Ethical

- The style guide is **extracted from your own writing** — every pattern came from sentences you composed
- Authorship question is not "did a human type this?" but **"whose intellectual and stylistic choices shaped it?"**
- When you provide bullets, arguments, evidence, and style guide — **those choices are yours; CC is the typist**
- Analogy: a research assistant who has read all your papers and writes in your voice is not replacing authorship — it is **extending capacity**
- 💡 CC writes in your voice, guided by your own examples — the resulting prose is genuinely yours
