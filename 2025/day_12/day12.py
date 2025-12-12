import re

with open("puzzle_input.txt", "r") as puzzle_input:
    puzzle_input = puzzle_input.read().splitlines()

part1_solution = 0

for line in puzzle_input[30:]:
    x, y, *shape_quantity = map(int, re.findall(r'\d+', line))
    total_shapes = sum(shape_quantity)
    # Compute the number of 3x3 squares in the given region. If the number of
    # shapes we want to fit is less than or equal to the number of 3x3 squares,
    # then they can definitely fit without overlapping (because each shape fits
    # in a 3x3 square). Turns out this is sufficient to solve the problem.
    nonoverlapping_spaces = (x // 3) * (y // 3)
    if total_shapes <= nonoverlapping_spaces:
        part1_solution += 1

# Part 1 Solution: 510
print(f"Part 1 Solution: {part1_solution}")
