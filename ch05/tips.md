# Tips for Style Guides

## 1. Use samples from different contexts — not just one section

A style guide built from two introduction paragraphs will reflect how you write introductions, not how you write methods sections or discussion paragraphs. Those genres have different rhythms. Pull 5–10 samples from across your writing: at least one introduction, one methods passage, one discussion, and one conclusion. CC will identify patterns that hold across all of them — and those are your most reliable style features.

## 2. Include "what I want to avoid" in your style guide

The best style guides are not only descriptive — they are also restrictive. When you review CC's output, add a section:

```
Things to avoid:
- Passive voice overuse (more than one passive construction per paragraph)
- Sentences over 35 words
- Starting consecutive sentences with the same word
- Hedging every single claim (one hedge per paragraph is enough)
```

CC will treat these as hard constraints. You will notice the difference.

## 3. Ask CC to score a draft against your style guide

After CC produces a paragraph, ask it to evaluate its own output:

```
Read style-guide.md. Score the paragraph you just wrote 0–10 for adherence
to my style. List specific deductions and explain each one.
```

This forces CC to reason explicitly about the gap between what it produced and what your style guide calls for. Ask it to revise after scoring. The second pass is usually noticeably better.

## 4. Use the style guide for emails and academic letters too

Your writing voice matters beyond papers. Grant letters, cover letters, reviewer responses, and professional emails all benefit from sounding like you — consistent, recognizable, considered. Keep a second, lighter style guide for professional correspondence if your email voice differs from your academic writing voice. Most researchers write slightly more informally in emails, and that difference is worth capturing.

## 5. Maintain separate style guides for separate genres

The voice appropriate for a methods section is not the same as the voice appropriate for a discussion. Methods writing tends to be terse, passive, and precise. Discussion writing is more expansive, hedged, and argumentative. If you notice that a single style guide is producing wrong results for one genre, split it:

- `style-guide-methods.md`
- `style-guide-discussion.md`

Invoke the right one for the right task.

## 6. CC can write style-adherent prose from bullet points alone

You do not need to draft sentences for CC to work from. Give it structured bullets and the style guide:

```
Read style-guide.md. Write a paragraph from these bullets in my style:
- Effect was significant (p < .01)
- Effect size was small (d = 0.24)
- Consistent with Smith (2018) but smaller than Jones (2021) estimated
- Possible explanation: our sample was more homogeneous
```

CC will turn those bullets into flowing prose in your voice. This is one of the fastest ways to turn notes into draft text — you supply the facts and the judgment, CC supplies the sentences.
