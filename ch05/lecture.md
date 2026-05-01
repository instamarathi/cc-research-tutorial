# Your Voice — Style Guide

## Why AI Writing Sounds Generic

Ask an AI to write a paragraph on any academic topic and you will recognize the result immediately: well-structured, grammatically clean, and completely forgettable. The sentences are the right length. The transitions are appropriate. Nothing is wrong with it — and nothing is distinctively right with it either.

This happens because large language models are trained on hundreds of millions of texts and learn to produce statistically central prose. They average across everything they have seen. The result is writing that offends no one and sounds like no one. No rhythm. No personality. No particular way of building an argument. Your readers — reviewers, supervisors, readers who know your work — can feel this immediately, even if they cannot name it.

The solution is not to avoid CC for writing. It is to teach CC your voice.

## What Makes Your Voice Unique

Every experienced writer has a fingerprint. Most writers cannot fully articulate it — but it is there.

Your fingerprint shows up in the small decisions you make dozens of times per paragraph: how long your sentences run before you break them, whether you use "however" or "yet" or "but" to pivot, how you introduce evidence ("Smith (2018) shows that…" versus "The data here suggest…"), whether you hedge with "appears to" or "may" or "it is worth noting that," and how you open and close paragraphs. It shows up in the vocabulary you reach for, the kind of examples you choose, the way you signal that you are taking a position.

These patterns are consistent because they are yours. They developed over years of writing in your discipline. And because they are consistent — encoded in your own texts — CC can extract them.

## The Style Guide Extraction Workflow

The extraction takes about ten minutes and produces a document you will use for years.

**Step 1: Find 2–3 paragraphs you are proud of.** Choose from your own unedited work — a methods section you rewrote until it felt right, a discussion paragraph your supervisor praised, a grant application paragraph that landed. Avoid anything heavily edited by someone else; you want your voice, not a committee's.

**Step 2: Paste them into a file called `my-writing-samples.md`.** This gives CC a concrete object to work from.

**Step 3: Run the style extraction prompt:**

```
Read my-writing-samples.md. Analyze my writing style and produce a style-guide.md.
Include: typical sentence length, how I vary sentence length, connective words I use,
how I introduce evidence, how I hedge claims, paragraph structure,
distinctive vocabulary, and at least two concrete examples of each feature.
Ask CC to save the result to style-guide.md.
```

**Step 4: Review the output.** Read `style-guide.md` carefully. CC will usually get the broad strokes right and miss some of the finer texture. Add anything it missed. Delete anything that does not ring true. This review step matters — the style guide only works if it is accurate.

**Step 5: Save `style-guide.md` in your research project directory.** For work that spans multiple projects, keep a copy in your home research folder.

**Step 6: Start every writing session with:**

```
Read style-guide.md. Write in the style described there.
```

One line. That is all CC needs to shift from generic prose to something that sounds like you.

> [!TRY]
> Open CC now. Find 2 paragraphs from your own writing — something recent, something you feel represents how you actually write. Paste them in and run the extraction prompt. When CC produces the style guide, read it carefully: does the description match your self-perception? Where does it surprise you?

> [!TIP]
> More examples = better style capture. Five to ten paragraphs from different contexts — an introduction, a methods section, a discussion — give CC a richer fingerprint than two or three. If you have the samples, use them.

## Using the Style Guide

The style guide is most useful when you invoke it explicitly at the start of a writing task:

```
Read style-guide.md. I need a paragraph introducing the gap in the literature
that my study addresses. Here are the key points in bullet form:
- Most studies measure X at a single time point
- Longitudinal designs exist but are expensive
- My study uses a low-cost proxy measure to enable repeated measurement
Write the paragraph in my style.
```

This gives CC the style constraint, the content, and the task in one prompt. What comes back will be structured around your bullets but written with your characteristic moves.

A few other useful prompts once you have a style guide:

- "Read style-guide.md. Rewrite this paragraph in my style." — useful for drafts that sound too generic
- "Read style-guide.md. Score this paragraph 0–10 for adherence to my style. Explain any deductions." — useful for reviewing your own drafts
- "Read style-guide.md. Does this abstract sound like me?" — a quick gut-check before submission

The style guide is a living document. When an editor or supervisor praises a particular passage, add a note to the style guide: "praised for X." When you notice you have drifted from something the guide describes, update it. A practical rhythm is to revisit and revise the guide once a semester — your writing changes as you publish more, and the guide should keep up.

## Why This Is Ethical

The style guide is extracted from your writing. Every pattern in it was learned from sentences you composed. When CC writes using the style guide, it is applying your own fingerprint — not averaging over millions of other people's prose.

This matters because the authorship question in academic writing is not "did a human type these sentences?" It is "whose intellectual and stylistic choices shaped this text?" When you give CC your bullets, your arguments, your evidence, and your style guide, those choices are yours. CC is the typist. You are the author.

> [!NOTE]
> The style guide approach works because you are the author. CC writes in your voice, guided by your own examples. The resulting prose is genuinely yours — CC is the typist.

There is a useful analogy here: a skilled research assistant who has read all your papers and learned to write in your voice is not replacing your authorship. They are extending your capacity. CC can do this at zero marginal cost, consistently, any time you sit down to write.
