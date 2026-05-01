# Tips: Simulations & Code

## 1. Describe the model, not the implementation

Tell CC what the scientific process is — the entities, the rules, the parameters, the output. Let CC decide whether to use numpy, a list comprehension, or a dataclass. Researchers who over-specify the implementation often end up constraining CC to a suboptimal approach. "Simulate a 2D Ising model at temperature T with periodic boundary conditions" is better than "make a 2D numpy array and use a for loop".

## 2. Ask CC to add assertions for sanity checking

After a simulation runs, have CC add assertions that verify the output is scientifically reasonable. For example: "Add an assertion that checks the mean final position is within 2 standard errors of zero." Assertions catch silent bugs — cases where the code runs without error but produces wrong results. They also document your expectations inside the code itself.

## 3. Ask CC to create a CLAUDE.md for your simulation project

Once your code structure is settled, ask: "Create a CLAUDE.md for this project. Document what the simulation models, the key parameters and their units, how to run it, and any known limitations." This primes CC for future sessions — when you come back in two weeks, CC will have the context it needs without you re-explaining everything.

## 4. "Run it with these parameters and show me the output" — don't run it yourself

Resist the habit of running the script yourself and pasting output back. Ask CC to run it: "Run simulate.py with n_steps=500 and n_particles=2000 and show me the results." CC can capture the output, generate a plot, and interpret what it sees — all in one turn. This keeps the loop inside CC where it can iterate if something goes wrong.

## 5. Parameterize early — ask CC to refactor before you accumulate hardcoded runs

As soon as you find yourself thinking "I want to try a few different values of this parameter," ask CC to refactor. "Replace all the hardcoded simulation parameters with command-line arguments using argparse." Do this before you have five nearly-identical scripts with slightly different numbers. A parameterized script is vastly easier to manage, share, and reproduce.

## 6. Ask CC to set up git if you haven't

Simulation code evolves quickly, and it is easy to lose a working version. If your project is not yet in version control, ask CC: "Initialize a git repository here and make an initial commit. Add a .gitignore appropriate for a Python data science project." From then on, ask CC to commit whenever you reach a working checkpoint: "Commit the current state with a message describing what the simulation does."
