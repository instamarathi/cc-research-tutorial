## Q1

You want CC to write and run a Monte Carlo simulation of protein folding. Which prompt will get you the best result?

- [ ] "Write Python code for a protein folding simulation using numpy arrays."
- [ ] "Write a simulation."
- [x] "Simulate a 50-residue protein chain using a lattice model. Each step, attempt to move a randomly chosen residue to an adjacent empty lattice site. Accept moves that lower energy or pass a Boltzmann test at temperature T=1.5. Run for 100,000 steps, track the energy over time, and plot the energy trajectory. Run the script and show me the output."
- [ ] "I need a Python class with methods for initializing the lattice, computing energy, and running the MCMC loop."

> The third option describes the scientific model (lattice, move type, acceptance criterion, temperature), the scale (100,000 steps), the output (energy trajectory, plot), and asks CC to run it. The first option over-specifies the implementation. The second is too vague. The fourth specifies architecture without explaining the science.

---

## Q2

You run `python simulation.py` and get a `TypeError: unsupported operand type(s) for +: 'float' and 'NoneType'`. What is the most efficient next step?

- [ ] Read the traceback, identify the line, fix it yourself, and re-run.
- [ ] Copy the error and paste it into Claude.ai for suggestions.
- [ ] Ask CC: "Look at line 47 of simulation.py — why does it fail?"
- [x] Ask CC: "Run simulation.py. If it errors, fix the bug and run it again until it produces output."

> Asking CC to run the script gives it access to both the full traceback and the source code simultaneously. It can fix the bug and verify the fix by re-running — no copy-pasting required, and no risk of missing a second bug that would only appear after the first is fixed.

---

## Q3

You have a working simulation but you want to verify it is producing scientifically correct output, not just running without errors. What is the best approach?

- [ ] Run it several times and check that the numbers look reasonable by eye.
- [ ] Ask CC to write unit tests for each function.
- [x] Ask CC to add assertions that check known statistical properties of the output — for example, that the mean is near the theoretical value and the variance is within a reasonable range.
- [ ] Ask CC to compare the output to a reference implementation.

> Assertions that check statistical properties catch silent bugs — cases where the code runs without error but produces wrong results. They encode your scientific expectations directly in the code. Unit tests work well for deterministic functions, but stochastic simulations need statistical checks, not exact-value tests.

---

## Think

Describe a simulation or analysis script you use in your own research. How would you explain it to CC so that CC could re-implement it from scratch, without seeing the original code?

<answer>
A good answer includes: (1) the scientific process being modeled — what entities exist, what rules govern their behavior; (2) the key input parameters with types and typical ranges (e.g., "temperature T, a float between 0.5 and 5.0 in units of kT"); (3) what is computed at each step of the simulation; (4) what the expected output looks like — a distribution, a time series, a scalar summary statistic; (5) any constraints on runtime, dependencies, or numerical precision. The more specific and quantitative the description, the less ambiguity CC has to resolve. A prompt that says "the mean should converge to approximately X for these parameter values" is far more useful than one that says "the output should look right."
</answer>
