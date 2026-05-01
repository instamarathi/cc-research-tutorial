# Post-Writing Polish

## How to Spot AI-Generated Prose

- **Too consistent** — human writers are uneven; AI prose is smooth from first word to last
- **Hollow transitions** — "It is worth noting that…", "Furthermore,", "This highlights the importance of…" add structure without content
- **Uniform paragraph structure** — topic sentence + three equal sentences + clincher, repeated
- **Passive overuse** — "It was found that…", "It can be seen that…" erases the agent from every sentence
- **Hedging without specificity** — "Many researchers have noted…" names no one and cites nothing
- **Overlong sentences** — 40+ word clauses that force readers to hold too much in working memory
- **List addiction** — bullets replacing analysis, hiding the connections between ideas

## The Polish Workflow

- **Four passes, one job each** — do not combine them
- **Pass 1 — Remove hollow transitions:** "Rewrite removing all hollow filler transitions. Cut or replace dead phrases with actual content."
- **Pass 2 — Vary sentence structure:** "Vary sentence length deliberately: some under 10 words, some over 25."
- **Pass 3 — Apply your style guide:** prompt CC to apply `style-guide.md`; flag uncertain conventions
- **Pass 4 — Human final read:** read aloud — your ear catches what your eye misses
- 💡 The read-aloud test beats all AI checks — stumbles flag sentences that are too long, too abrupt, or unnatural

## Example: Polishing the Weather Blog

- **Before (AI-sounding):** "It is worth noting that precipitation levels demonstrate a significant correlation with reduced ambulatory activity across the study cohort."
- **After (human voice):** "Rain hit harder than cold. On wet days, people took 28% fewer steps — regardless of temperature."
- **Change 1 — Cut the hollow opener:** "It is worth noting that" deleted; the actual finding leads the sentence
- **Change 2 — Replace latinate nouns:** "precipitation levels" → "rain"; "ambulatory activity" → "steps"; "study cohort" → dropped entirely
- **Change 3 — Vary sentence length:** one punchy 5-word sentence followed by one 11-word sentence with an em-dash pause
- **Change 4 — Make the agent concrete:** passive "demonstrate a significant correlation" → active "people took 28% fewer steps"
- **Change 5 — Lead with the surprise:** temperature buried at the end signals it matters less — that's the real insight

## The Banned Phrases List

- Maintain **`banned-phrases.md`** in your project root — add phrases as you notice them
- Starter entries: `It is worth noting that`, `Delve into`, `As previously mentioned`, `In conclusion,`
- Prompt: "Read banned-phrases.md. Remove every instance. Where load-bearing, rewrite directly. Where empty, delete."
- **Do not remove mechanically** — check each deletion; bring real substance forward
- "It is worth noting that replication rates have declined" → "Replication rates fell from 85% (2000) to 39% (2020)"
- ⚠️ Every hollow opener hides something — either a real point stated badly, or nothing at all

## Polish Works on Your Writing Too

- The four-pass workflow improves **any** academic prose, not just CC-generated text
- Hollow transitions appear in human writing too — openers are easy shortcuts when writing is hard
- AI markers in your own prose often signal **underspecified thinking**, not just stylistic habit
- Removing "it is important to note that" forces you to **commit to the actual claim**
- ⚡ Paste a paragraph from your own writing and ask CC: "List every AI writing marker in this paragraph." The results will surprise you.
