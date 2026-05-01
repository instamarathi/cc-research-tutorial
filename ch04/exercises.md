# Exercises: Writing a Paper Section

## Exercise 1: Draft a Methods Section

**Time: 20 minutes**

This exercise builds the habit of giving CC structured context before asking it to write. You'll provide a minimal research description and ask CC to draft a Methods section from it.

**Step 1.** Create a file called `paper-context.md`. Write the following, filling in your own content:

- One sentence stating your research question.
- Two sentences describing your dataset or study subjects — who or what they are, how many, and how they were selected.
- Two to three sentences describing your analysis approach — what you did to the data and why.

The content can be real (from a current project) or invented for the exercise. What matters is that it's specific enough to draft from.

**Step 2.** Ask CC to read the file and draft a Methods section:

> "Read `paper-context.md`. Draft a Methods section of approximately 200 words. Write in passive voice, past tense. Do not add information I haven't provided — if something is underspecified, mark it with [NEEDS DETAIL] so I know what to fill in."

**Step 3.** Read the draft. Find any passage that feels too vague or too generic. Ask CC to revise it:

> "The description of [X] is too vague. Here is more detail: [your detail]. Revise that passage."

Notice how the [NEEDS DETAIL] markers function as a structured handoff between what CC can infer and what only you can provide. This is the division of labor that makes section drafting efficient.

---

## Exercise 2: Consistency Audit

**Time: 10 minutes**

This exercise surfaces the consistency-checking capability that makes CC most useful on longer drafts.

**Step 1.** Write three to four paragraphs on any research topic — real or invented. As you write, deliberately introduce inconsistencies of the kind that appear naturally in real drafts:

- Use "participants" in one paragraph and "subjects" in another to refer to the same group.
- Shift between past tense ("we collected") and present tense ("we collect") across paragraphs.
- Refer to your key variable by two slightly different names in different places.

**Step 2.** Save the text to a file and ask CC to audit it:

> "Read this draft. Identify any inconsistencies in terminology or tense. List each one specifically — quote the inconsistent passages and explain what the inconsistency is."

**Step 3.** Review CC's findings. Note whether it caught everything you planted. Then ask it to fix the inconsistencies:

> "Revise the draft so that terminology and tense are consistent throughout. Use [your preferred term] and [your preferred tense] as the standard."

The goal is to internalize how fast and reliably CC does this — and to build the habit of running a consistency audit before submitting any manuscript.

---

## Exercise 3: Respond to a Reviewer Comment

**Time: 15 minutes**

Peer review is a primary driver of revision work. This exercise practices the structured workflow for addressing reviewer feedback.

**Step 1.** Write a short methods paragraph (three to five sentences) describing a fictional study's sample size choice. Keep it brief — you're deliberately leaving it under-justified so there's something to fix.

**Step 2.** Write a fictional reviewer comment to address. For example:

> "The authors do not adequately justify their choice of sample size. Given the complexity of the proposed model, the sample appears underpowered. Please provide a formal power analysis or an alternative theoretical justification for why the current sample is sufficient."

**Step 3.** Ask CC to suggest revision approaches:

> "A reviewer said: [paste the comment]. Read the methods paragraph below and suggest two different ways I could revise it to address this comment. For each approach, explain what it adds and what tradeoff it involves."

**Step 4.** Choose an approach and ask CC to produce the revision:

> "Use approach [1 or 2] to revise the paragraph. Show me the original and the revised version side by side."

Compare the two versions. Verify the revision addresses the specific concern the reviewer raised without overclaiming or adding unsupported content.
