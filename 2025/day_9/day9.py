import itertools


with open("puzzle_input.txt", "r") as puzzle_input:
    puzzle_input = puzzle_input.read().splitlines()

coords = [tuple(map(int, line.split(","))) for line in puzzle_input]

max_area = max(
    (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
    for (x1, y1), (x2, y2) in itertools.combinations(coords, 2)
)

part1_solution = max_area

# Part 1 Solution: 4744899849
print(f"Part 1 Solution: {part1_solution}")

closed_coords = coords + [coords[0]]
lines = list(zip(closed_coords, closed_coords[1:]))

max_area = 0
for (x1, y1), (x2, y2) in itertools.combinations(coords, 2):
    box_x1, box_y1 = min(x1, x2), min(y1, y2)
    box_x2, box_y2 = max(x1, x2), max(y1, y2)
    for (line_x1, line_y1), (line_x2, line_y2) in lines:
        # line_start_x, line_start_y = min(line_x1, line_x2), min(line_y1, line_y2)
        # line_end_x, line_end_y = max(line_x1, line_x2), max(line_y1, line_y2)
        # We directly use the min and max instead of the variables above to take
        # advantage of a several second speed up due to short-circuit evaluation.

        # Check if line intersects box. A box is invalid if any line intersects it.
        if (max(line_x1, line_x2) > box_x1 and min(line_x1, line_x2) < box_x2 and
            max(line_y1, line_y2) > box_y1 and min(line_y1, line_y2) < box_y2):
            # Line intersects box, try next line
            break
    else:
        # No lines intersect box, box is valid, check if largest
        area = (box_x2 - box_x1 + 1) * (box_y2 - box_y1 + 1)
        max_area = max(max_area, area)
            

part2_solution = max_area

# Part 2 Solution: 1540192500
print(f"Part 2 Solution: {part2_solution}")
