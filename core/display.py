def print_grid(grid):
    for row in grid:
        print(" ".join(row))
    print()

def print_path(path):
    print(" -> ".join(path) if path else "No solution found.")