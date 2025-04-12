from itertools import combinations
from bisect import bisect_left

with open("puzzle_input.txt", "r") as puzzle_input:
    puzzle_input = puzzle_input.read().splitlines()

space = puzzle_input
empty_rows = [idx for idx, row in enumerate(space) if "#" not in row]
space_T = list(map(list, zip(*space)))
empty_cols = [idx for idx, col in enumerate(space_T) if "#" not in col]

galaxies = [
    (x, y)
    for x, row in enumerate(space)
    for y, symbol in enumerate(row)
    if symbol == "#"
]


def solve(expansion=2):
    total_distance = 0
    for galaxy1, galaxy2 in combinations(galaxies, 2):
        distance = abs(galaxy1[0] - galaxy2[0]) + abs(galaxy1[1] - galaxy2[1])
        x1 = min(galaxy1[0], galaxy2[0])
        x2 = max(galaxy1[0], galaxy2[0])
        y1 = min(galaxy1[1], galaxy2[1])
        y2 = max(galaxy1[1], galaxy2[1])
        num_empty_rows = bisect_left(empty_rows, x2) - bisect_left(empty_rows, x1)
        num_empty_cols = bisect_left(empty_cols, y2) - bisect_left(empty_cols, y1)
        total_distance += (expansion - 1) * (num_empty_cols + num_empty_rows) + distance
    return total_distance


part1_solution = solve(expansion=2)

# Part 1 Solution: 9563821
print(f"Part 1 Solution: {part1_solution}")

part2_solution = solve(expansion=1_000_000)

# Part 2 Solution: 827009909817
print(f"Part 2 Solution: {part2_solution}")
