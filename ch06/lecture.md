# Post-Writing Polish

## How to Spot AI-Generated Prose

AI writing is too consistent. That is the tell. Human writers are uneven — they have good paragraphs and bad ones, moments of precision and moments of vagueness, sentence rhythms that shift with mood and energy. AI writers are smooth from first word to last, structured without lapse, relentlessly clear.

Once you can see that, the individual markers become obvious.

**Hollow transitions.** AI text is stitched together with connective tissue that sounds logical but carries no information. "It is worth noting that the results confirm…" — what is worth noting? The results confirming the hypothesis is the entire sentence. The opener adds nothing. The same goes for "It is important to emphasize that…", "Furthermore,", "In conclusion,", and "This highlights the importance of…" These phrases exist to signal structure without creating it.

**Uniform paragraph structure.** Open any AI-generated section and you will find the same architecture repeated: a topic sentence, three supporting sentences of roughly equal length, a clincher that echoes the topic sentence. Human paragraphs are shaped by the argument. Some are three sentences. Some are one. Some run half a page because the idea requires it.

**Passive overuse.** Academic writing has always leaned passive, but AI leans harder. "It was found that…", "It can be seen that…", "The data were analyzed using…" — the agent disappears from every sentence. Your readers do not know who found what, or who can see what, or who did the analysis.

**Hedging without specificity.** "Many researchers have noted the importance of replication." Which researchers? In which studies? What exactly did they note? Vague attribution sounds cautious and rigorous while saying nothing verifiable.

**Overlong sentences.** AI prose favors 40-plus word sentences that travel from premise to qualification to conclusion in one continuous clause, which makes the logic appear seamless but requires the reader to hold more than necessary in working memory. Most of these split cleanly into two.

**List addiction.** AI defaults to bullets when ideas could flow. Bullet points are useful for genuinely discrete items — steps, enumerated criteria, parallel options. When every paragraph of analysis becomes a list, the connections between ideas vanish.

## The Polish Workflow

Four passes. One job per pass. Do not combine them.

**Pass 1: Remove hollow transitions.** Prompt: "Rewrite this paragraph removing all hollow filler transitions. Do not add anything — just cut or replace the dead phrases with the actual content they were obscuring."

**Pass 2: Vary sentence structure.** Prompt: "Rewrite this passage. Vary sentence length deliberately: some under 10 words, some over 25. The rhythm should feel intentional, not mechanical."

**Pass 3: Apply your style guide.** If you maintain a `style-guide.md` — preferred terminology, tense conventions, formatting rules — apply it here. Prompt: "Apply my style-guide.md to this passage. Flag any place where you're uncertain which convention applies."

**Pass 4: Human final read.** Read it aloud. Your ear catches what your eye misses. A sentence that parses cleanly on the page can sound robotic or stilted the moment you speak it. Mark anything that makes you stumble and fix it by hand.

> [!TIP]
> The "read aloud" test beats all AI checks. After CC polishes, read the passage out loud. Anything that makes you stumble is a problem — a sentence too long, a transition too abrupt, a phrase that no real person would say. Fix those by hand.

## The Banned Phrases List

Maintain a file called `banned-phrases.md` in your project directory. Every time you notice a phrase that marks your prose as AI-generated, add it. The file accumulates your own editorial judgment.

A starter list:

```
It is worth noting that
It is important to emphasize
Furthermore,
In conclusion,
This highlights the importance of
Delve into
It can be seen that
As previously mentioned
```

The prompt to use it:

> "Read banned-phrases.md. Remove every instance of these phrases from the following text. Where a phrase was load-bearing — where something needed to be said — rewrite the sentence to say it directly. Where the phrase was empty, delete the sentence."

That last clause matters. Mechanical removal leaves gaps. "It is worth noting that replication rates have declined" does not become "replication rates have declined." It becomes: "Replication rates have declined from 85% in 2000 to 39% in 2020 — a collapse severe enough to trigger the ongoing credibility crisis." Replace with the actual insight, or acknowledge there was no insight there and cut.

> [!WARN]
> Do not remove phrases mechanically and walk away. Every hollow opener was hiding something — sometimes a real point stated badly, sometimes nothing at all. Check each removal. If the sentence had substance, bring it forward. If it didn't, the deletion was correct.

## Polish Works on Your Writing Too

These four passes improve any academic prose, not just text generated by CC. Run your own drafts through the same workflow when revising. The hollow transitions appear in human writing too — they appear because writing is hard and openers are easy shortcuts. The uniform paragraph structure appears because the five-paragraph essay model is the scaffold most people learned and never fully escaped.

The difference is that when you run your own prose through this workflow, you often find the AI markers are also the places where your thinking is underspecified. The hollow opener "it is important to note that" is frequently hiding a claim you haven't quite committed to. Removing the hedge forces the commitment.

> [!TRY]
> Paste a paragraph from your own writing that you suspect sounds too polished or generic. Ask CC: "List every AI writing marker you can identify in this paragraph." The result will surprise you — not because the paragraph is AI-generated, but because the habits are shared.
