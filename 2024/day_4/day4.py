from itertools import product


with open("puzzle_input.txt", "r") as puzzle_input:
    puzzle_input = puzzle_input.read().splitlines()

grid = list(map(list, puzzle_input))
nX = len(grid)
nY = len(grid[0])

neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]

part1_solution = 0
for x, y in product(range(nX), range(nY)):
    if grid[x][y] != "X":
        continue
    for dx, dy in neighbors:
        x1, y1 = x + dx, y + dy
        x2, y2 = x1 + dx, y1 + dy
        x3, y3 = x2 + dx, y2 + dy

        if (
            0 <= x3 < nX
            and 0 <= y3 < nY
            and grid[x1][y1] == "M"
            and grid[x2][y2] == "A"
            and grid[x3][y3] == "S"
        ):
            part1_solution += 1


# Part 1 Solution: 2454
print(f"Part 1 Solution: {part1_solution}")

diagonals = [(1, 1), (-1, 1), (1, -1), (-1, -1)]

part2_solution = 0
for x, y in product(range(nX), range(nY)):
    if grid[x][y] == "A":
        diags = [
            grid[x + dx][y + dy]
            for dx, dy in diagonals
            if 0 <= x + dx < nX and 0 <= y + dy < nY
        ]
        if len(diags) == 4 and "".join(diags) in {"MSMS", "SMSM", "SSMM", "MMSS"}:
            part2_solution += 1

# Part 2 Solution: 1858
print(f"Part 2 Solution: {part2_solution}")
