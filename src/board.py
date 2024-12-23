import copy
import matplotlib.pyplot as plt
import numpy as np
import random
import heapq

def flatten(lst):
    return [item for sublist in lst for item in sublist]

def generate_radnom_state(n):
    total_blocks = n * n
    colors = ['green', 'white', 'red', 'yellow', 'orange', 'blue']

    blocks_per_color = (total_blocks - 1) // 6
    color_counts = {color: blocks_per_color for color in colors}
    color_counts['black'] = 1

    grid = [['' for _ in range(n)] for _ in range(n)]

    for i in range(1, n-1):
        for j in range(1, n-1):
            color = random.choice(colors)
            grid[i][j] = color
            color_counts[color] -= 1
            if color_counts[color] == 0:
                colors.remove(color)

    available_indices = [(i, j) for i in range(n) for j in range(n) if grid[i][j] == '']
    random.shuffle(available_indices)

    for color, count in color_counts.items():
        for _ in range(count):
            i, j = available_indices.pop()
            grid[i][j] = color
    return grid

def display_grid(grid):
    n = len(grid)
    block_size = 50
    border_size = 1

    image = np.ones(((n + 1) * border_size + n * block_size, (n + 1) * border_size + n * block_size, 3),
                    dtype=np.uint8) * 0

    color_mapping = {
        'green': (0, 255, 0),
        'white': (255, 255, 255),
        'red': (255, 0, 0),
        'yellow': (255, 255, 0),
        'orange': (255, 165, 0),
        'blue': (0, 0, 255),
        'black': (0, 0, 0)
    }

    for i in range(n):
        for j in range(n):
            color = color_mapping[grid[i][j]]
            start_row = i * (block_size + border_size) + border_size
            end_row = start_row + block_size
            start_col = j * (block_size + border_size) + border_size
            end_col = start_col + block_size

            image[start_row:end_row, start_col:end_col] = color

    plt.imshow(image)
    plt.axis('off')
    plt.show()


def getGoalState(grid):
    n = len(grid)
    goal = []

    for i in range(1, n - 1):
        row = grid[i][1:n - 1]
        goal.append(row)
    return goal


def display_scrambler(grid):
    n = len(grid)
    block_size = 50
    border_size = 1

    image = np.ones(((n + 1) * border_size + n * block_size, (n + 1) * border_size + n * block_size, 3),
                    dtype=np.uint8) * 0

    color_mapping = {'green': (0, 255, 0), 'white': (255, 255, 255), 'red': (255, 0, 0), 'yellow': (255, 255, 0),
                     'orange': (255, 165, 0), 'blue': (0, 0, 255), }

    for i in range(n):
        for j in range(n):
            color = color_mapping[grid[i][j]]
            start_row = i * (block_size + border_size) + border_size
            end_row = start_row + block_size
            start_col = j * (block_size + border_size) + border_size
            end_col = start_col + block_size

            image[start_row:end_row, start_col:end_col] = color

    plt.imshow(image)
    plt.axis('off')
    plt.show()

def display_goal_state(goal_state):
    n = len(goal_state)
    block_size = 50
    border_size = 1

    image = np.ones(((n + 1) * border_size + n * block_size, (n + 1) * border_size + n * block_size, 3),
                    dtype=np.uint8) * 0

    color_mapping = {'green': (0, 255, 0), 'white': (255, 255, 255), 'red': (255, 0, 0), 'yellow': (255, 255, 0),
                     'orange': (255, 165, 0), 'blue': (0, 0, 255), '': (0, 0, 0)}

    for i in range(n):
        for j in range(n):
            color = color_mapping[goal_state[i][j]]
            start_row = i * (block_size + border_size) + border_size
            end_row = start_row + block_size
            start_col = j * (block_size + border_size) + border_size
            end_col = start_col + block_size

            image[start_row:end_row, start_col:end_col] = color

    plt.imshow(image)
    plt.axis('off')
    plt.show()

def apply_moves_to_black_block(grid, moves):
    n = len(grid)

    black_row, black_col = None, None
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 'black':
                black_row, black_col = i, j
                break

    if black_row is None or black_col is None:
        raise ValueError("Black block not found in the grid")

    for move in moves:
        if move == 'left' and black_col > 0:
            grid[black_row][black_col], grid[black_row][black_col - 1] = grid[black_row][black_col - 1], \
                                                                         grid[black_row][black_col]
            black_col -= 1
        elif move == 'right' and black_col < n - 1:
            grid[black_row][black_col], grid[black_row][black_col + 1] = grid[black_row][black_col + 1], \
                                                                         grid[black_row][black_col]
            black_col += 1
        elif move == 'up' and black_row > 0:
            grid[black_row][black_col], grid[black_row - 1][black_col] = grid[black_row - 1][black_col], \
                                                                         grid[black_row][black_col]
            black_row -= 1
        elif move == 'down' and black_row < n - 1:
            grid[black_row][black_col], grid[black_row + 1][black_col] = grid[black_row + 1][black_col], \
                                                                         grid[black_row][black_col]
            black_row += 1

def move_away(grid, num_steps):
    n = len(grid)
    while num_steps > 0:
        up = 0
        right = 0

        while abs(up) + abs(right) != 1:
            up = random.randint(0, 1)
            right = random.randint(0, 1)

            if random.random() < 0.5:
                up *= -1
            if random.random() < 0.5:
                right *= -1

        black_row, black_col = None, None
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 'black':
                    black_row, black_col = i, j
                    break

        if (black_row - up < n and black_row - up > 0) and (black_col + right < n and black_col + right > 0):
            moves = []
            if up == 1:
                moves.append('up')
            elif up == -1:
                moves.append('down')
            if right == 1:
                moves.append('right')
            elif right == -1:
                moves.append('left')
            apply_moves_to_black_block(grid, moves)
            num_steps -= 1
class Puzzle:
    def __init__(self, n, goal, puzzle):
        self.size = n
        self.goal_state = goal
        self.puzzle = puzzle
        self.black_row, self.black_col = self.find_black_block()
        self.path_cost = 0
    def __hash__(self):
        return hash(tuple(map(tuple, self.puzzle)))
    def __eq__(self, other):
        return isinstance(other, Puzzle) and self.puzzle == other.puzzle
    def find_black_block(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.puzzle[i][j] == 'black':
                    return i, j


    def applyMove(self, m):

        if m == 'left' and self.black_col > 0:
            self.puzzle[self.black_row][self.black_col], self.puzzle[self.black_row][self.black_col - 1] = \
            self.puzzle[self.black_row][self.black_col - 1], self.puzzle[self.black_row][self.black_col]
            self.black_col -= 1
        elif m == 'right' and self.black_col < self.size - 1:
            self.puzzle[self.black_row][self.black_col], self.puzzle[self.black_row][self.black_col + 1] = \
            self.puzzle[self.black_row][self.black_col + 1], self.puzzle[self.black_row][self.black_col]
            self.black_col += 1
        elif m == 'up' and self.black_row > 0:
            self.puzzle[self.black_row][self.black_col], self.puzzle[self.black_row - 1][self.black_col] = \
            self.puzzle[self.black_row - 1][self.black_col], self.puzzle[self.black_row][self.black_col]
            self.black_row -= 1
        elif m == 'down' and self.black_row < self.size - 1:
            self.puzzle[self.black_row][self.black_col], self.puzzle[self.black_row + 1][self.black_col] = \
            self.puzzle[self.black_row + 1][self.black_col], self.puzzle[self.black_row][self.black_col]
            self.black_row += 1

        self.path_cost += 1

    def is_goal_state(self):
        for i in range(1, self.size - 1):
            for j in range(1, self.size - 1):
                if self.puzzle[i][j] != self.goal_state[i - 1][j - 1]:
                    return False
        return True

    def copy(self):
        return copy.deepcopy(self)

    def get_possible_moves(self):
        possible_moves = []
        for i in range(self.size):
            for j in range(self.size):
                if self.puzzle[i][j] == 'black':
                    if i > 0:
                        possible_moves.append("up")
                    if i < self.size - 1:
                        possible_moves.append("down")
                    if j > 0:
                        possible_moves.append("left")
                    if j < self.size - 1:
                        possible_moves.append("right")
        return possible_moves

    def __lt__(self, other):
        return (self.path_cost + self.manhattanHeuristic()) < (other.path_cost + other.manhattanHeuristic())

    def manhattanHeuristic(self):

        def manhattan_distance(pos1, pos2):
            return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

        def flatten(lst):
            return [item for sublist in lst for item in sublist]

        current_positions = {color: [] for color in set(flatten(self.puzzle))}
        goal_positions = {color: [] for color in set(flatten(self.goal_state))}

        for i in range(self.size - 2):
            for j in range(self.size - 2):
                current_color = self.puzzle[i + 1][j + 1]
                goal_color = self.goal_state[i][j]
                if current_color != '' and goal_color != '':
                    goal_positions[goal_color].append((i + 1, j + 1))

        for i in range(self.size):
            for j in range(self.size):
                current_color = self.puzzle[i][j]
                if current_color == "black":
                    continue
                current_positions[current_color].append((i, j))
        count = 0
        for color in current_positions:
            if color not in goal_positions:
                continue
            current_color_positions = current_positions[color]
            goal_color_positions = goal_positions[color]

            for goal_pos in goal_color_positions:
                distance = []
                for current_pos in current_color_positions:
                    heapq.heappush(distance, manhattan_distance(current_pos, goal_pos))
                count += heapq.heappop(distance)
        return count

    def numberOfMisplacedHeuristic(self):

        heuristic_value = (self.size - 2) * (self.size - 2)

        current_positions = {color: [] for color in set(flatten(self.puzzle))}
        goal_positions = {color: [] for color in set(flatten(self.goal_state))}

        for i in range(1, self.size - 1):
            for j in range(1, self.size - 1):

                current_color = self.puzzle[i][j]

                if current_color == "black":
                    continue
                goal_color = self.goal_state[i - 1][j - 1]

                if current_color != '' and goal_color != '':
                    goal_positions[goal_color].append((i, j))

        for i in range(1, self.size - 1):
            for j in range(1, self.size - 1):
                current_color = self.puzzle[i][j]
                if current_color == "black":
                    continue
                current_positions[current_color].append((i, j))

        for color in current_positions:
            if color == "black":
                continue

            elif color not in goal_positions:
                continue

            current_color_positions = current_positions[color]
            goal_color_positions = goal_positions[color]

            for current_pos in current_color_positions:
                if current_pos in goal_color_positions:
                    heuristic_value -= 1

        return heuristic_value



