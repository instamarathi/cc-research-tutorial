# Writing a Paper Section

## The Problem with Copy-Paste Writing

The default workflow for using AI on academic writing goes like this: paste an abstract into a chat window, get a paragraph back, paste the paragraph into your manuscript, realize it doesn't match your tone or reference your data correctly, and start over. Each exchange is stateless. The model knows nothing about what you wrote three paragraphs earlier, what terminology your field uses, or what argument you're trying to sustain across twenty pages.

The result is prose that is locally fluent but globally incoherent — sentences that sound like your paper but don't actually belong in it. You spend more time editing the generated text than you would have spent writing from scratch.

Claude Code solves this by holding your entire manuscript in context. It doesn't just generate — it reads, tracks, and stays consistent with what you've already written. When you ask it to draft the Methods section, it knows what the Introduction promised. When you ask it to check for hedging, it's reading the same paper you are. This is the shift that makes CC genuinely useful as a writing partner, rather than a paragraph dispenser.

## Giving CC the Full Paper Context

Before you ask CC to write a single word, give it the full manuscript. The session-opening prompt matters:

> "Read `paper.md`. This is my working draft. We're going to work on the Methods section today. Don't write anything yet — just confirm that you've read it and tell me in one sentence what the paper's central argument is."

That last instruction — confirm you've read it and restate the argument — is not busywork. It forces CC to demonstrate comprehension before it starts drafting. If its one-sentence summary is off, you know its understanding of the paper needs correction before you proceed.

Once CC has confirmed the context, it maintains it throughout the session. Subsequent prompts like "draft the next subsection" or "check this paragraph for consistency with the introduction" will be interpreted against the full manuscript, not in isolation. CC tracks your terminology, your argument structure, and your voice — as long as the paper is in context and you haven't asked it to start fresh.

For long manuscripts or multi-session projects, keep a `context.md` file that records the paper's key decisions: the research question, the main contribution, any terminology conventions, and notes on what each section is meant to accomplish. Open each session by asking CC to read both the manuscript and the context file before drafting begins.

## The Drafting Workflow

Working section by section is not just a best practice — it's the workflow that produces usable prose. Here is the sequence that works:

1. **Give CC the section's job.** Before asking it to write, describe what the section needs to accomplish: "The Methods section needs to (1) justify the sample size, (2) describe the instrument and its validation history, and (3) explain the analysis pipeline in enough detail to be replicable." This framing shapes every sentence CC generates.

2. **Draft one subsection at a time.** Ask CC to draft the first subsection only. Read it before moving on. If you ask for the whole section at once, you lose the ability to steer while it's still cheap to change direction.

3. **Revise through conversation.** When a draft is close but not right, say what's wrong specifically: "This is good but the transition from participant recruitment to instrument description is too abrupt — add a bridging sentence." Vague requests get vague revisions. Specific feedback gets specific edits.

4. **Check against context.** After completing a section, ask CC to verify it's consistent with the rest of the paper: "Does the terminology in this Methods section match how I refer to the same concepts in the Introduction?" This catches drift before it accumulates.

> [!TRY]
> Take any draft you have, even a rough one. Put it in a file and ask CC to read it. Then ask: "Which section is the weakest, and why?" CC will identify the place where the argument is underspecified, the writing is vague, or the logic is unclear. Use that diagnosis to decide where to start revising.

> [!WARN]
> Do not ask CC to write the entire paper in one prompt. Quality drops sharply on long unchecked generations. Errors in the framing of one section propagate to subsequent sections, and by the time you notice the problem you have thousands of words to revise. Write section by section, review and approve each section before moving on, and give CC explicit steering feedback at each step.

## Maintaining Consistency

Consistency is the hardest thing to maintain manually in a long document. Terminology drifts: "participants" becomes "subjects" becomes "respondents" across sections written days apart. Tense shifts between past and present without a clear logic. The contribution promised in the Introduction doesn't quite match the claim made in the Conclusion.

These are exactly the errors that pass through human editing undetected — not because the writer doesn't know better, but because it's cognitively expensive to hold ten thousand words in working memory while reading paragraph thirty-seven.

Ask CC to do what humans find effortful and it finds trivial:

- "Scan the whole paper and flag any places where the same concept is referred to by different names, or where terminology shifts without explanation."
- "Check whether the paper's tense is consistent — I'm aiming for past tense throughout the empirical sections and present tense in the theoretical frame."
- "Does the contribution I claim in the Conclusion match what I promised in the Introduction? Quote the relevant sentences from each."

> [!NOTE]
> Consistency checking is where CC dramatically outperforms manual editing. It can scan ten thousand words in seconds and catch what a tired human misses after hours of reviewing. Run a full consistency audit before every submission, not just at the end of a drafting session.

## Revision Workflow

Peer review is a structured source of writing problems. Each reviewer comment tells you something specific is broken and gives you a reader's-eye view of the failure. CC can help you address each comment systematically.

The revision prompt structure:

> "A reviewer said: '[exact reviewer quote].' Read [section name] and suggest three different ways I could revise it to address this comment. For each approach, explain the tradeoff."

Asking for three approaches rather than one prevents CC from anchoring on a single solution. You get a range — a minimal fix, a substantive revision, and a structural rethinking — and you choose based on your judgment about what the paper actually needs.

After choosing an approach, ask CC to produce a before/after comparison:

> "Revise the sample size justification paragraph to address the reviewer's comment using approach 2. Show me the original paragraph and the revised version side by side, with the key changes marked."

The explicit before/after makes it easy to verify that the revision addresses the comment without introducing new problems — a risk whenever you change prose that is already doing multiple jobs at once.

For reviewer comments that feel unclear, use CC as an interpreter before attempting a revision: "A reviewer said the Discussion 'overstates the generalizability.' What does that usually mean in the context of a study like mine, and what kinds of language or claims typically trigger that objection?" Getting clarity on what the reviewer likely meant is the prerequisite for fixing the right thing.
