with open("puzzle_input.txt", "r") as puzzle_input:
    puzzle_input = list(map(list, puzzle_input.read().splitlines()))

neighbors = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

def run(grid, p2=False):
    solution = 0
    for x, row in enumerate(grid):
        for y, cell in enumerate(row):
            if cell != "@":
                continue
            num_roles_around = 0
            for dx, dy in neighbors:
                nx, ny = x + dx, y + dy
                in_bounds = 0 <= nx < len(puzzle_input) and 0 <= ny < len(row)
                if in_bounds and puzzle_input[nx][ny] == "@":
                    num_roles_around += 1
                    if num_roles_around >= 4:
                        break
            else:
                solution += 1
                if p2:
                    grid[x][y] = "x"
    return solution

part1_solution = run(puzzle_input)

# Part 1 Solution: 1384
print(f"Part 1 Solution: {part1_solution}")

part2_solution = 0
while (out := run(puzzle_input, p2=True)) != 0:
    part2_solution += out

# Part 2 Solution: 8013
print(f"Part 2 Solution: {part2_solution}")
