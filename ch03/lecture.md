# Developing Theory

## CC as a Thinking Partner

Most researchers initially reach for Claude Code when they need to write or debug code. That instinct undersells the tool. CC is equally useful — sometimes more useful — as a thinking partner for the abstract, pre-code work of theory development: sharpening an argument, surfacing hidden assumptions, formalizing a vague intuition into something testable.

Think of CC as a brilliant peer reviewer who has read everything in your field but knows nothing specific about your problem. It brings broad pattern recognition to narrow questions. Unlike a search engine, CC doesn't retrieve — it reasons. It can take a novel combination of ideas you haven't seen articulated before and help you work out whether it holds together, where it breaks, and how to state it more precisely.

This is a different use case than coding. The output isn't a function or a script — it's a sharper version of your thinking. Treat it that way: the conversation is the product.

## From Verbal Intuition to Formal Statement

Good theory usually starts as a fuzzy conviction: "I think X happens because of Y, but only when Z." That verbal form is where the idea lives before you can test it. CC is particularly good at the translation step — turning rough language into precise, falsifiable claims.

A useful flow:

1. **State the raw intuition** — write 2-4 sentences in plain language, as if explaining to a colleague over coffee.
2. **Ask CC to formalize** — "Turn this intuition into a precise, testable hypothesis. Identify the key variables and the proposed relationship between them."
3. **Request formal notation** — "Express this hypothesis in mathematical notation" or "Write this as a LaTeX equation."
4. **Derive testable predictions** — "What would we observe if this hypothesis is true? What would falsify it?"

Each step forces you to be more specific. The process often reveals that what felt like one idea is actually two, or that you've left a critical condition implicit. CC will surface these gaps because it takes your words literally — if you haven't said it, it isn't there.

> [!TRY]
> Take a research idea you've been mulling. Write it in 2-3 sentences. Ask CC: "Formalize this as a falsifiable hypothesis and suggest how you would test it." See whether the formalized version matches what you actually meant.

## The Steelman Technique

A steelman is the opposite of a strawman: you construct the strongest possible version of an argument before attacking it. When applied to your own hypothesis, the steelman technique forces you to articulate assumptions you've been glossing over — and to confront the best version of the objections, not the easiest.

Run this three-prompt sequence with CC:

1. **Steelman the claim** — "Here is my hypothesis. Steelman it: give me the most rigorous, defensible version of this argument. Fill in any implicit assumptions and tighten the logical structure."
2. **Attack the steelman** — "Now argue against it. What are the three strongest counterarguments a skeptical reader from my field would raise?"
3. **Design around the objections** — "For each counterargument, suggest how I would design a study or analysis that would rule it out or substantially weaken it."

The result is not a list of fatal flaws — it's a map of your hypothesis's vulnerability profile. You know exactly which empirical claims are load-bearing, which assumptions are contestable, and which objections you should address proactively in your paper rather than leave for reviewers to find.

## Generating LaTeX

CC can produce publication-ready LaTeX: equations, aligned multiline derivations, theorem-proof blocks, tables, and custom environments. This is useful when you have a formal result you want to typeset but don't want to wrestle with LaTeX syntax by hand.

Effective prompts:

- "Write the following as a LaTeX `theorem` environment with a proof sketch."
- "Format this derivation as a LaTeX `align` environment."
- "Create a LaTeX `tabular` with these columns and this data, suitable for an APA-style journal."

CC will typically produce complete, compilable blocks. Ask for the `\usepackage` statements you need so you don't have to hunt them down.

> [!NOTE]
> Always verify LaTeX output compiles before including it in a manuscript. CC occasionally makes minor syntax errors in complex environments — mismatched braces, incorrect command names in specialized packages, or environments that require specific document class options. A quick `pdflatex` pass catches these before they become a submission-day problem.

## Structuring an Argument

A theoretical contribution is only as strong as its logical scaffolding. CC can help you see the scaffolding explicitly, which is hard to do when you're inside the argument.

Two moves:

**Map the logical chain.** Ask CC: "Here is my main thesis. Break down the logical chain from foundational premises to the conclusion as a numbered list. Make each inferential step explicit." Seeing the chain written out reveals whether any step is doing more work than it should, whether you've skipped a step, or whether the connection between two adjacent steps relies on an unstated assumption.

**Find the weakest link.** Once you have the chain, ask: "Which step in this argument relies most heavily on unestablished empirical assumptions? Which step would a critical reviewer be most likely to contest?" CC will identify the point of greatest vulnerability — which tells you where to focus your anticipatory response.

Use CC to find field-relevant touchstones too. Give it context about your discipline and ask: "Are there canonical results or well-known objections in [field] that bear directly on this argument?" It won't give you verified citations — but it will point you toward the conceptual territory worth checking.

> [!WARN]
> CC can confabulate citations. It may produce author names, titles, and journal names that look plausible but don't correspond to real papers. Never trust a CC-generated citation without verifying it independently — check the full reference in a database like Google Scholar, Semantic Scholar, or your field's primary index. Ask CC to explain concepts and arguments, not to source them.
