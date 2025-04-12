from collections import namedtuple
from itertools import combinations
import z3

Hailstone = namedtuple("Hailstone", ("px", "py", "pz", "vx", "vy", "vz"))

with open("puzzle_input.txt", "r") as puzzle_input:
    puzzle_input = puzzle_input.read().splitlines()

intersect_region = (200000000000000, 400000000000000)

data = []
for line in puzzle_input:
    position, velocity = line.split(" @ ")
    position = list(map(int, position.split(", ")))
    velocity = list(map(int, velocity.split(", ")))
    data.append(Hailstone(*position, *velocity))


def line_point_intersection(h1, h2):
    # https://en.wikipedia.org/wiki/Line%E2%80%93line_intersection#Given_two_line_equations
    h1_slope = h1.vy / h1.vx
    h2_slope = h2.vy / h2.vx
    if h1_slope == h2_slope:
        return False
    h1_y_intercept = h1.py - h1_slope * h1.px
    h2_y_intercept = h2.py - h2_slope * h2.px
    intercept_x = (h2_y_intercept - h1_y_intercept) / (h1_slope - h2_slope)
    intercept_y = h1_slope * intercept_x + h1_y_intercept
    if (intercept_x - h1.px) / h1.vx < 0 or (intercept_x - h2.px) / h2.vx < 0:
        return False
    if (
        intersect_region[0] <= intercept_x <= intersect_region[1]
        and intersect_region[0] <= intercept_y <= intersect_region[1]
    ):
        return True
    return False


part1_solution = sum(
    line_point_intersection(h1, h2) for h1, h2 in combinations(data, 2)
)

# Part 1 Solution: 11246
print(f"Part 1 Solution: {part1_solution}")

solver = z3.Solver()

px, py, pz, vx, vy, vz = z3.Reals("px py pz vx vy vz")

for idx, h in enumerate(data):
    t = z3.Real(f"t_{idx}")
    solver.add(t >= 0)
    solver.add(px + vx * t == h.px + h.vx * t)
    solver.add(py + vy * t == h.py + h.vy * t)
    solver.add(pz + vz * t == h.pz + h.vz * t)

solver.check()
model = solver.model()

part2_solution = sum(model[var].as_long() for var in [px, py, pz])

# Part 2 Solution: 716599937560103
print(f"Part 2 Solution: {part2_solution}")
