# Tips for Developing Theory with CC

## 1. "What assumptions am I making that I'm not explicitly stating?"

This is the single most useful theory-building prompt in your toolkit. Ask it after you've written out your hypothesis or argument. CC will surface the implicit premises — about causal direction, measurement equivalence, boundary conditions, population homogeneity — that you've been treating as obvious. Reviewers won't.

## 2. Generate rival hypotheses

Don't let confirmation bias narrow your thinking. After stating your hypothesis, prompt: "Give me three alternative hypotheses that could explain the same data pattern." This forces you to consider what you'd have to rule out empirically and often reveals that your favored explanation requires more evidentiary work than you thought.

## 3. Ask CC to draw the causal diagram

If your theory involves causal relationships — and most theories do — ask CC to make them explicit: "Describe the causal relationships in my theory as a directed acyclic graph (DAG) in plain English. List each node and each directed edge." You don't need graph software for this; the plain-language version already clarifies whether you've assumed away confounders or left feedback loops unaddressed.

## 4. "Explain this to a skeptical reader in field X"

Theoretical arguments often use field-specific language as a kind of shorthand that glosses over steps that practitioners in adjacent fields would demand you justify. Prompting CC to translate your argument for a different audience — "Explain this argument to a skeptical economist" or "Explain this to a reader trained in experimental psychology" — reveals which steps rely on disciplinary assumptions rather than general logic.

## 5. LaTeX template prompt

For formal results, use: "Write the following as a LaTeX theorem block with proof sketch." Supply the theorem statement and the key steps of the proof; CC will produce a complete, properly formatted `theorem`/`proof` environment. Useful for working papers, dissertations, or supplementary materials where formal presentation matters.

## 6. Ask for the option space, not the answer

CC is better at generating possibilities than picking winners. When you're stuck on how to operationalize a construct or which identification strategy to use, ask: "What are five different ways I could test this hypothesis empirically?" rather than "What is the best way to test this?" Then apply your own domain knowledge to evaluate the options. This division of labor — CC generates, you judge — consistently outperforms asking CC to do both.
