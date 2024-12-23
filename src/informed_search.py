from board import display_grid
import heapq


class AStarSearchGraph:
    def __init__(self, initial_state,  n):
        self._n = n
        self.initial_state = initial_state
        self.frontier = []

    def searchManhattan(self):
        heapq.heappush(self.frontier,
                       (self.initial_state.path_cost + self.initial_state.manhattanHeuristic(), self.initial_state))
        generated_nodes = 0
        expanded_nodes = 0
        visited = []

        while self.frontier:
            current_state = heapq.heappop(self.frontier)[1]

            if current_state in visited:
                continue

            expanded_nodes += 1

            if current_state.is_goal_state():
                print("Goal state reached!")
                display_grid(current_state.puzzle)
                return

            for move in current_state.get_possible_moves():
                new_state = current_state.copy()
                new_state.applyMove(move)
                cost = new_state.path_cost + new_state.manhattanHeuristic()

                heapq.heappush(self.frontier, (cost, new_state))
                generated_nodes += 1

            visited.append(current_state)

        return None

    def searchNumOfMisplaced(self):
        heapq.heappush(self.frontier,
                       (self.initial_state.path_cost + self.initial_state.numberOfMisplacedHeuristic(), self.initial_state))
        generated_nodes = 0
        expanded_nodes = 0
        visited = []

        while self.frontier:
            current_state = heapq.heappop(self.frontier)[1]

            if current_state in visited:
                continue

            expanded_nodes += 1

            if current_state.is_goal_state():
                print("Goal state reached!")
                display_grid(current_state.puzzle)
                return

            h = []
            for move in current_state.get_possible_moves():
                new_state = current_state.copy()
                new_state.applyMove(move)
                cost = new_state.path_cost + new_state.numberOfMisplacedHeuristic()
                h.append(cost)
                heapq.heappush(self.frontier, (cost, new_state))
                generated_nodes += 1
            visited.append(current_state)

        return None

class IDA:
    def __init__(self, initial_state, n):
        self._n = n
        self.initial_state = initial_state
        self.threshold = None
        self.pruned = []

    def searchNumMisplacedTiles(self):
        self.pruned = []
        self.threshold = self.initial_state.path_cost + self.initial_state.numberOfMisplacedHeuristic()
        heapq.heappush(self.pruned, (self.initial_state.path_cost + self.initial_state.numberOfMisplacedHeuristic(), self.initial_state))

        c = 0
        while True:
            c += 1
            result = self.NumMisplacedTiles_search_depth(self.initial_state, self.initial_state.path_cost)
            if result:
                print("Goal state reached!")
                return result

            else:

                self.threshold += heapq.heappop(self.pruned)[0]

    def NumMisplacedTiles_search_depth(self, current_state, g, visited=0):
        visited += 1
        f = g + current_state.numberOfMisplacedHeuristic()

        if f > self.threshold:
            heapq.heappush(self.pruned, (current_state.path_cost + current_state.numberOfMisplacedHeuristic(), current_state))

            return None

        if current_state.is_goal_state():
            return current_state

        min_cost = float('inf')

        for move in current_state.get_possible_moves():
            new_state = current_state.copy()
            new_state.applyMove(move)

            child_result = self.NumMisplacedTiles_search_depth(new_state, g + 1, visited)

            if child_result:
                return child_result

            cost = new_state.path_cost + new_state.numberOfMisplacedHeuristic()
            min_cost = min(min_cost, cost)

        return None

    def searchManhattanDist(self):
        self.pruned = []
        self.threshold = self.initial_state.path_cost + self.initial_state.manhattanHeuristic()
        heapq.heappush(self.pruned,
                       (self.initial_state.path_cost + self.initial_state.manhattanHeuristic(), self.initial_state))
        visited = 0
        c = 0
        while True:
            c += 1
            result = self.ManhattanDist_search_depth(self.initial_state, self.initial_state.path_cost)
            if result:
                print("Goal state reached!")

                return result

            else:
                visited += 1
                self.threshold += heapq.heappop(self.pruned)[0]

    def ManhattanDist_search_depth(self, current_state, g, visited=0):
        visited += 1
        f = g + current_state.manhattanHeuristic()

        if f > self.threshold:
            heapq.heappush(self.pruned,
                           (self.initial_state.path_cost + self.initial_state.manhattanHeuristic(), self.initial_state))

            return None

        if current_state.is_goal_state():
            return current_state

        min_cost = float('inf')

        for move in current_state.get_possible_moves():
            new_state = current_state.copy()
            new_state.applyMove(move)

            child_result = self.ManhattanDist_search_depth(new_state, g + 1, visited)

            if child_result:
                return child_result

            cost = new_state.path_cost + new_state.manhattanHeuristic()
            min_cost = min(min_cost, cost)

class AStarSearchTree:
    def __init__(self, initial_state,  n):
        self._n = n
        self.initial_state = initial_state
        self.frontier = []

    def searchManhattan(self):
        heapq.heappush(self.frontier,
                       (self.initial_state.path_cost + self.initial_state.manhattanHeuristic(), self.initial_state))
        generated_nodes = 0
        expanded_nodes = 0
        visited = []

        while self.frontier:
            current_state = heapq.heappop(self.frontier)[1]

            expanded_nodes += 1

            if current_state.is_goal_state():
                print("Goal state reached!")
                display_grid(current_state.puzzle)
                return

            for move in current_state.get_possible_moves():
                new_state = current_state.copy()
                new_state.applyMove(move)
                cost = new_state.path_cost + new_state.manhattanHeuristic()

                heapq.heappush(self.frontier, (cost, new_state))
                generated_nodes += 1

            visited.append(current_state)

        return None

    def searchNumOfMisplaced(self):
        heapq.heappush(self.frontier,
                       (self.initial_state.path_cost + self.initial_state.numberOfMisplacedHeuristic(), self.initial_state))
        generated_nodes = 0
        expanded_nodes = 0
        visited = []

        while self.frontier:
            current_state = heapq.heappop(self.frontier)[1]
            expanded_nodes += 1

            if current_state.is_goal_state():
                print("Goal state reached!")
                display_grid(current_state.puzzle)
                return

            for move in current_state.get_possible_moves():
                new_state = current_state.copy()
                new_state.applyMove(move)
                cost = new_state.path_cost + new_state.numberOfMisplacedHeuristic()

                heapq.heappush(self.frontier, (cost, new_state))
                generated_nodes += 1

            visited.append(current_state)

        return None
