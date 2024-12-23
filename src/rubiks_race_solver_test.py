from board import Puzzle, display_grid, display_scrambler, generate_radnom_state, getGoalState, move_away
from informed_search import AStarSearchGraph, AStarSearchTree, IDA
from hill_climnbing_and_bfs import HillClimbingSearch, BreadthFirstSearch

# n is the size of our n x n grid
# number of moves away is how far we want our initial state to be from the goal state

# change the values from None to the desired size and moves away value
n = None
number_of_moves_away = None
state = generate_radnom_state(n)
display_grid(state)
goal = getGoalState(state)
display_grid(goal)
move_away(state, number_of_moves_away)
display_grid(state)
puzzle = Puzzle(n=n, goal=goal, puzzle=state)
display_grid(puzzle.puzzle)  #displayes initial state
display_scrambler(goal)   #displayes the goal  


# 1
# This is to run the A* search tree algorithm

# 1.1
# using manhattan distance heuristic
# AStarSearchTree(initial_state=puzzle, n=puzzle.size).searchManhattan()

# 1.2
# using number of misplaced tiles heuristic
# AStarSearchTree(initial_state=puzzle, n=puzzle.size).searchNumOfMisplaced()


# 2
# This is to run the A* search graph algorithm
# 2.1
# using manhattan distance heuristic
# AStarSearchGraph(initial_state=puzzle, n=puzzle.size).searchManhattan()

# 2.2
# using number of misplaced tiles heuristic
# AStarSearchGraph(initial_state=puzzle, n=puzzle.size).searchNumOfMisplaced()


# 3
# This is to run the Hill Climbing algorithm

# 3.1
# using manhattan distance heuristic
# HillClimbingSearch(initial_state=puzzle, n=puzzle.size).search_manhattan()

# 3.2
# using number of misplaced tiles heuristic
# HillClimbingSearch(initial_state=puzzle, n=puzzle.size).search_misplaced()


# 4
# This is to run the IDA* search graph algorithm

# 4.1
# using manhattan distance heuristic
# IDA(initial_state=puzzle, n=puzzle.size).searchManhattanDist()

# 4.2
# using number of misplaced tiles heuristic
# IDA(initial_state=puzzle, n=puzzle.size).searchNumMisplacedTiles()


# 5
# This is to run the Breadth First Search algorithm
# BreadthFirstSearch(puzzle, puzzle.size).search()
