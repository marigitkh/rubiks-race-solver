from core.state import State

def misplaced_tiles(state: State) -> int:
    board = state.board.extract_goal_window()
    goal = state.goal.extract_goal_window()
    return sum(1 for i in range(len(board)) for j in range(len(board)) if board[i][j] != goal[i][j])

def manhattan_distance(state: State) -> int:
    board = state.board.grid
    goal = state.goal.extract_goal_window()
    n = len(board)
    goal_map = {}
    for i, row in enumerate(goal):
        for j, color in enumerate(row):
            goal_map.setdefault(color, []).append((i + 1, j + 1))
    total = 0
    used = set()
    for i in range(n):
        for j in range(n):
            color = board[i][j]
            if color == "_" or color not in goal_map:
                continue
            dists = [(abs(i - gi) + abs(j - gj), (gi, gj)) for (gi, gj) in goal_map[color] if (gi, gj) not in used]
            if dists:
                d, pos = min(dists)
                total += d
                used.add(pos)
    return total