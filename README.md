# Overview

I created this project as the final project in CS111 (Introduction to Computer Science 1) at Boston University. It uses object-oriented programming in order to create a working 8-Puzzle Solver in Python.

# Files

The file eight_puzzle.py is the driver that allows the solver to work. It allows you to input a board initial configuration and the algorithm to be used to solve the puzzle. It also defines how the board file is processed. All of the algorithms are defined in searcher.py. A general searcher class is defined, which defines the processes of adding and removing board states and the logic behind those actions. Additonally, the main algorithm classes are also defined here: BFS, DFS, and two greedy algorithms. The state.py file defines the state class, which is a representation for the board configuration at any given time. It also determines if the algorithm is successful and which states can be reached next. The plain text files with "moves" in the titles are sample initial board configurations, and the number in the titles correspond to the optimal number of moves to solve the puzzle. The results.txt file stores the results of running all of the different algorithms on all of the different move files.
