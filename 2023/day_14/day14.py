from copy import deepcopy

with open("puzzle_input.txt", "r") as puzzle_input:
    puzzle_input = puzzle_input.read().splitlines()

grid = list(map(list, puzzle_input))


def roll(grid):
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] != "O":
                continue
            new_x = x
            while new_x > 0 and grid[new_x - 1][y] == ".":
                new_x -= 1
            if new_x != x:
                grid[x][y] = "."
                grid[new_x][y] = "O"
    return grid


def load(grid):
    size = len(grid)
    return sum((size - x) * sum(y == "O" for y in grid[x]) for x in range(size))


part1_solution = load(roll(deepcopy(grid)))

# Part 1 Solution: 109385
print(f"Part 1 Solution: {part1_solution}")


def rotate_matrix(m):
    return list(list(x) for x in zip(*m[::-1]))


def roll_all_directions(grid):
    for _ in range(4):
        grid = rotate_matrix(roll(grid))
    return grid


def stringify(grid):
    return "\n".join("".join(x) for x in grid)


def find_cycle(grid):
    seen = {stringify(grid): 0}
    idx = 1
    while True:
        grid = roll_all_directions(grid)
        grid_str = stringify(grid)
        if grid_str in seen:
            cycle_start = seen[grid_str]
            cycle_length = idx - cycle_start
            return cycle_start, cycle_length, seen
        seen[grid_str] = idx
        idx += 1


desired_time = 1_000_000_000
cycle_start, cycle_length, seen = find_cycle(grid)
cycle_time = (desired_time - cycle_start) % cycle_length
final_grid_idx = cycle_start + cycle_time
final_grid = None
for grid_str, idx in seen.items():
    if idx == final_grid_idx:
        final_grid = grid_str
        break

part2_solution = load([list(x) for x in final_grid.splitlines()])

# Part 2 Solution: 93102
print(f"Part 2 Solution: {part2_solution}")
