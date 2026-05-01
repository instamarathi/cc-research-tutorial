# Simulations & Code

## CC as Your Coding Partner

Every researcher who has used Claude.ai to help with code knows the ritual: write code, hit an error, copy the traceback, open a browser, paste everything into Claude.ai, read the fix, copy it back, run it again. It works, but the friction adds up. Each round-trip breaks your focus, and you lose the thread of what you were actually trying to model.

Claude Code eliminates that loop entirely. CC has access to your entire project — not just the snippet you paste. It can read your files, execute code, see the full traceback alongside the source, and try a fix without you doing anything. The loop still happens; it just happens inside CC.

The mental model shift is this: you are no longer the code executor. You describe what you want to compute, CC figures out how to write and run it, and you review the output. Your job moves up a level — from debugging syntax to evaluating whether the science is right.

Old workflow:
1. Write code
2. Run it, get error
3. Copy error + code into Claude.ai
4. Read response, paste fix back
5. Repeat

New workflow:
1. Describe the simulation
2. CC writes it, runs it, fixes any errors
3. You review the output

The second workflow is not just faster — it keeps you thinking about your research problem rather than about Python syntax.

> [!TRY]
> Open CC in a directory that contains a Python script. Ask: "Read script.py and describe what each function does. What would happen if I called main() with an empty list?" Notice that CC reads the file first, then reasons about the behavior — no copy-pasting required.

---

## Writing New Simulation Code

The most common mistake researchers make when asking CC to write code is being too implementation-focused. You do not need to say "write a numpy array of shape (n_particles, n_steps)". You need to describe the science.

Think about what you would tell a new PhD student who knows Python but not your subfield. You would explain the process being modeled, the parameters it takes, and what output you expect. That is exactly what CC needs.

A good prompt describes:
- **The process**: what is actually happening in the simulation
- **The parameters**: what inputs control it, with typical ranges
- **The output**: what you want to see — a number, a distribution, a plot
- **The action**: ask CC to write it *and run it*

For example: "Simulate 1000 random walks of 100 steps each. At each step, each walker moves +1 or -1 with equal probability. Track the final position of every walker and plot a histogram of the distribution. Run the script and show me the plot."

This prompt tells CC the model (random walk), the scale (1000 walkers, 100 steps), the output format (histogram), and asks for execution. CC can write this from scratch, run it, and return the plot — without you touching a keyboard for anything other than that prompt.

> [!TIP]
> Describe the science, let CC handle the syntax. "Simulate 10,000 random walks and plot the final position distribution" is a better prompt than "write numpy code that initializes a 2D array and uses cumsum". The first gives CC room to choose the right implementation; the second constrains it to an approach you may have guessed at.

---

## The Debug Loop

When code breaks, the instinct is to read the error yourself and start reasoning about the fix. With CC, you can skip that step entirely.

Ask CC to run the script directly:

```
python simulate.py
```

When it fails, CC sees both the full traceback *and* the source code at the same time. It does not need you to copy-paste anything. More importantly, it can try a fix and immediately re-run the script to confirm whether the fix worked — all in one turn.

The most effective debug prompt is: "Run simulate.py. If it fails, fix the error and run it again. Keep going until it produces output."

This instruction hands CC the debug loop. It will read the error, locate the relevant line in the source, apply a fix, and run again. For common errors (name errors, shape mismatches, missing imports), this resolves in one or two iterations. You can watch it work, or come back when it is done.

This beats the copy-paste cycle for several reasons. CC sees the full context — not just the snippet you selected. It knows what the script is supposed to do because it wrote it (or read it). And it can verify its own fix by running the code, rather than reasoning about it abstractly.

> [!WARN]
> Be specific about what "working" means. "Make it not crash" is different from "produce correct output for these test cases." A script that runs without error but produces nonsense is still broken. Tell CC what correct output looks like: "The mean final position should be near 0, and the standard deviation should be near 10."

---

## Iterative Improvement

Once a simulation runs, you will almost always want to change something. CC handles the full improvement cycle in the same session — no need to start over or re-explain the context.

Common improvement requests that work well:

- **Speed**: "This takes 90 seconds. Profile it and make it at least 3× faster."
- **Progress reporting**: "Add a progress bar that updates every 1000 iterations so I can see it's still running."
- **Parameterization**: "Replace all the hardcoded numbers with command-line arguments so I can run different configurations without editing the file."
- **Refactoring**: "Refactor this into a class so I can easily instantiate multiple runs with different parameter sets."
- **Validation**: "Add assertions that check the output is statistically reasonable — e.g., that the mean is within 3 standard deviations of the expected value."

The key is that CC retains context from earlier in the conversation. It knows the code it wrote, the parameters it used, and what the simulation is supposed to model. You are iterating on a shared understanding, not re-explaining everything each time.

For profiling and optimization, CC can use Python's `cProfile` module, identify the bottleneck function, and propose a vectorized or algorithmic improvement. Ask it to show you the profile output before and after so you can verify the speedup is real.

---

## Running and Visualizing Results

CC can save results and generate plots as part of the same session.

After a simulation runs, ask CC to: "Save the results to results.csv and generate a plot of the final position distribution. Save the plot as distribution.png."

You can also ask CC to interpret the output: "Describe what this plot shows. Does the distribution look like what we'd expect from a random walk?" This is a useful sanity check — if CC's description does not match your expectation, something is wrong with either the code or your mental model of the simulation.

For visualization, CC works well with `matplotlib` for standard scientific plots, `seaborn` for statistical visualizations, and `plotly` for interactive plots that you can explore in a browser. If you have a preference, mention it. If you do not, CC will usually default to matplotlib with reasonable styling.

A practical pattern: run the simulation, save results to CSV, generate a plot, and ask CC to describe what it sees. That three-step sequence — run, save, describe — turns a black-box script into something you can reason about together.
