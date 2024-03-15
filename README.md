# Hashi Puzzle Solver

Welcome to the Hashi Puzzle Solver! This program is designed to tackle the intriguing Hashi puzzles, also known as Hashiwokakero. It's a delightful logic puzzle where your goal is to connect islands with bridges according to specific rules. This is done by encoding the game rules into a CNF formula that is passed on to a SAT-solver like Minisat or CadiCal.

I explained the theory behind the encoding in [this paper](Hashi.pdf)

## About Hashi Puzzles
Hashi puzzles consist of a grid of islands, each displaying a number indicating how many bridges should connect to it. The bridges can only run horizontally or vertically, and no more than two bridges can connect any pair of islands. Additionally, bridges cannot cross each other or run diagonally.

## Instructions

You can start the raw solver without the gui from terminal with `python main.py` on root level. By default, it will solve the first test file, you can customise the input by providing the number of the test file, i.e. `python main.py 8`. The GUI can be started with `python gui.py`. Please note that the generation of puzzles was not implemented fully, a possible recursive algorithm can be found as comment in `gui.py`.


