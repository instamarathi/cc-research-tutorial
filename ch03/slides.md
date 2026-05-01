# Developing Theory

## CC as a Thinking Partner

- CC is useful beyond code — valuable for **pre-code, abstract theory work**
- Think of CC as a **peer reviewer who has read everything but knows nothing about your specific problem**
- Unlike search engines, CC **reasons** — it doesn't just retrieve
- CC can take novel idea combinations and help you work out whether they hold together
- The output here isn't a script — it's a **sharper version of your thinking**
- Treat the conversation itself as the product

## From Verbal Intuition to Formal Statement

- Good theory starts fuzzy: "I think X happens because of Y, but only when Z"
- **Step 1**: State the raw intuition — 2–4 sentences, plain language
- **Step 2**: Ask CC to formalize — "Turn this into a precise, testable hypothesis. Identify key variables."
- **Step 3**: Request formal notation — "Express this as a LaTeX equation."
- **Step 4**: Derive predictions — "What would we observe if this is true? What would falsify it?"
- Each step forces precision — often reveals **one idea is actually two**, or a critical condition is implicit
- ⚡ Try: write your research idea in 2–3 sentences, ask CC to formalize and suggest how to test it

## Example: Formalizing the Hypothesis

- **Raw intuition given to CC:** "People probably walk less on rainy or cold days — bad weather makes going outside unpleasant, so daily step counts should be lower."
- **Prompt:** "Turn this into a precise, testable hypothesis. Identify the key variables and express it as a regression equation."
- **Formal equation CC returns:** `steps_i = β₀ + β₁·temp_c + β₂·rain + ε_i`
- **Key variables identified:** outcome = `steps` (continuous); predictors = `temp_c` (continuous, °C), `rain` (binary, ≥1 mm); unit of observation = person-day
- **Directional predictions:** β₁ > 0 (warmer → more steps), β₂ < 0 (rain → fewer steps)
- Formalization revealed an implicit condition: the effect may vary **within-person** vs. **across people** — suggests adding a person fixed effect

## The Steelman Technique

- A **steelman** = strongest possible version of an argument (opposite of strawman)
- Apply to your own hypothesis to surface glossed-over assumptions
- **Prompt 1 — Steelman**: "Give me the most rigorous, defensible version of this argument. Fill in implicit assumptions."
- **Prompt 2 — Attack**: "What are the three strongest counterarguments a skeptical reader would raise?"
- **Prompt 3 — Design**: "For each counterargument, how would I design a study to rule it out?"
- Result: a **vulnerability map** — you know which claims are load-bearing and which objections to address proactively

## Example: Steelmanning the Weather Claim

- **Prompt used:** "What are the three strongest counterarguments a skeptical reviewer would raise against the claim that rain reduces daily step counts?"
- **Counterargument 1 — Seasonal confounding:** Rain is more common in winter; cold temperatures (not rain itself) may drive reduced activity, making the rain coefficient spurious without proper temperature controls
- **Counterargument 2 — Selection bias:** People who exercise outdoors drop off on rainy days, but gym-goers may compensate — step counts from wearables **undersample** gym exercise and overstate the effect
- **Counterargument 3 — Reverse causality / mood loop:** Low activity days may make people *perceive* weather as worse, inflating self-reported rain associations in diary-based data
- **Follow-up prompt:** "For each counterargument, what study design or control variable would rule it out?" — produces a concrete **robustness checklist**
- Result: the blog post "Why You Skip the Gym When It Rains" must acknowledge seasonal controls and gym-substitution before reviewers do

## Generating LaTeX

- CC produces **publication-ready LaTeX**: equations, aligned derivations, theorem-proof blocks, tables
- Useful prompts:
  ```
  "Write this as a LaTeX theorem environment with a proof sketch."
  "Format this as a LaTeX align environment."
  "Create a tabular for an APA-style journal with these columns."
  ```
- Ask CC for the required `\usepackage` statements — saves hunting them down
- CC typically produces **complete, compilable blocks**
- 📝 Always run `pdflatex` to verify before including in a manuscript — minor syntax errors do occur

## Structuring an Argument

- A theoretical contribution is only as strong as its **logical scaffolding**
- **Map the chain**: "Break down the logical chain from premises to conclusion. Make each inferential step explicit."
- Reveals steps doing **too much work**, skipped steps, or unstated assumptions between adjacent steps
- **Find the weakest link**: "Which step relies most on unestablished empirical assumptions? What would a reviewer contest?"
- Ask for **field-relevant touchstones**: "Are there canonical results in [field] that bear on this argument?"
- ⚠️ CC can **confabulate citations** — plausible-looking but nonexistent. Never trust without verifying in Google Scholar or Semantic Scholar
