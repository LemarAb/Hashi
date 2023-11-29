# Hashi Puzzle Solver

Welcome to the Hashi Puzzle Solver! This program is designed to tackle the intriguing Hashi puzzles, also known as Hashiwokakero. It's a delightful logic puzzle where your goal is to connect islands with bridges according to specific rules.

## About Hashi Puzzles
Hashi puzzles consist of a grid of islands, each displaying a number indicating how many bridges should connect to it. The bridges can only run horizontally or vertically, and no more than two bridges can connect any pair of islands. Additionally, bridges cannot cross each other or run diagonally.

## Instructions

You can start the raw solver without the gui from terminal with `python main.py` on root level. By default, it will solve the first test file, you can customise the input by providing the number of the test file, i.e. `python main.py 8`. The GUI can be started with `python gui.py`. Please note that the generation of puzzles was not implemented fully, a possible recursive algorithm can be found as comment in `gui.py`.

## Optimisation

Looking at the metrics, our default implementation already is quite speedy. However, we were able to even further cut down on execution time by excluding clauses belonging to the degree constraint that we can determine invalid even before running the solver. You can have a look at the difference between the sets of clauses for the degree constraint in `assets/bridge_sum.py` (list of clauses) and `assets/generate.py` (construction of clauses).

## Performance Metrics

We display the run times in in seconds as a pair (not optimized, optimized).

- Test 1: (0.04, 0.03)
- Test 2: (0.08, 0.06)
- Test 3: (0.1, 0.07)
- Test 11: (0.22, 0.15)


