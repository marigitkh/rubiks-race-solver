from board import display_grid
from collections import deque


class HillClimbingSearch:
    def __init__(self, initial_state,  n):
        self._n = n
        self.initial_state = initial_state
        self.current_state = (self.convert_to_hashable(self.initial_state.puzzle), self.initial_state)

    def convert_to_hashable(self, puzzle):
        if isinstance(puzzle, list):
            return tuple(self.convert_to_hashable(item) for item in puzzle)
        else:
            return puzzle

    def search_misplaced(self):
        visited = set()
        count_expanded = 0

        while True:
            current_state = self.current_state[1]

            if self.convert_to_hashable(current_state.puzzle) in visited:
                return False
            if current_state.is_goal_state():
                display_grid(current_state.puzzle)
                print("count expanded: "+str(count_expanded))
                return True
            neighbors = [
                (
                    neighbor.numberOfMisplacedHeuristic(),
                    neighbor
                )
                for neighbor in self.generate_neighbors(current_state)
            ]
            count_expanded+=len(neighbors)
            if not neighbors:
                return False

            best_neighbor =  min(neighbors, key=lambda x: x[0])
            if self.convert_to_hashable(best_neighbor[1].puzzle) in visited:
                sorted_neighbors = sorted(neighbors, key=lambda x: x[0])
                filtered_neighbors = [n for n in sorted_neighbors if n != best_neighbor]
                for x in filtered_neighbors:
                    if self.convert_to_hashable(x[1].puzzle) not in visited:
                        best_neighbor=x
                        break

            if best_neighbor[0] > self.current_state[1].numberOfMisplacedHeuristic():
                return False

            visited.add(self.convert_to_hashable(current_state.puzzle))
            self.current_state = (self.convert_to_hashable(best_neighbor[1].puzzle), best_neighbor[1])

    def search_manhattan(self):
        visited = set()
        count_expanded = 0
        while True:
            current_state = self.current_state[1]

            if self.convert_to_hashable(current_state.puzzle) in visited:
                return False
            if current_state.is_goal_state():
                display_grid(current_state.puzzle)
                print("count expanded: "+str(count_expanded))
                return True
            neighbors = [
                (
                    neighbor.manhattanHeuristic(),
                    neighbor
                )
                for neighbor in self.generate_neighbors(current_state)
            ]
            if not neighbors:
                return False
            count_expanded+=len(neighbors)
            best_neighbor =  min(neighbors, key=lambda x: x[0])
            if self.convert_to_hashable(best_neighbor[1].puzzle) in visited:
                sorted_neighbors = sorted(neighbors, key=lambda x: x[0])
                filtered_neighbors = [n for n in sorted_neighbors if n != best_neighbor]
                for x in filtered_neighbors:
                    if self.convert_to_hashable(x[1].puzzle) not in visited:
                        best_neighbor=x
                        break

            if best_neighbor[0] > self.current_state[1].manhattanHeuristic():
                return False

            visited.add(self.convert_to_hashable(current_state.puzzle))
            self.current_state = (self.convert_to_hashable(best_neighbor[1].puzzle), best_neighbor[1])

    def generate_neighbors(self, current_state):
        neighbors = []
        for move in current_state.get_possible_moves():
            neighbor = current_state.copy()
            neighbor.applyMove(move)
            neighbors.append(neighbor)
        return neighbors

class BreadthFirstSearch:
    def __init__(self, initial_state,  n):
        self._n = n
        self.initial_state = initial_state
        self.frontier = deque([self.initial_state])
        self.visited = set()
    def convert_to_hashable(self, puzzle):
        if isinstance(puzzle, list):
            return tuple(self.convert_to_hashable(item) for item in puzzle)
        else:
            return puzzle

    def search(self):
        while self.frontier:
            current_state = self.frontier.popleft()

            if self.convert_to_hashable(current_state.puzzle) in self.visited:
                continue

            self.visited.add(self.convert_to_hashable(current_state.puzzle))

            if current_state.is_goal_state():
                display_grid(current_state.puzzle)
                print("Goal State Reached")
                return True

            for move in current_state.get_possible_moves():
                new_state = current_state.copy()

                new_state.applyMove(move)
                self.frontier.append(new_state)

        return False
