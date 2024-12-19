from functools import cache

with open("puzzle_input.txt", "r") as puzzle_input:
    puzzle_input = puzzle_input.read()

patterns, designs = puzzle_input.split("\n\n")

patterns = patterns.split(", ")
designs = designs.splitlines()


@cache
def solve(design):
    if len(design) == 0:
        return 1
    count = 0
    for pattern in patterns:
        if design.startswith(pattern):
            count += solve(design[len(pattern) :])
    return count


part1_solution = sum(solve(design) > 0 for design in designs)

# Part 1 Solution: 216
print(f"Part 1 Solution: {part1_solution}")


part2_solution = sum(solve(design) for design in designs)

# Part 2 Solution: 603191454138773
print(f"Part 2 Solution: {part2_solution}")
