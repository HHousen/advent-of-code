import math

with open("puzzle_input.txt", "r") as puzzle_input:
    puzzle_input = puzzle_input.read().splitlines()

grid = puzzle_input
H = len(grid)
W = len(grid[0])
dxdy = [(0, 1), (0, -1), (1, 0), (-1, 0)]

starting_position = [(x, y) for x, y in zip(range(H), range(W)) if grid[x][y] == "S"]

visited = set(starting_position)
for step in range(64):
    visited = {
        (x + dx, y + dy)
        for x, y in visited
        for dx, dy in dxdy
        if 0 <= x + dx < H and 0 <= y + dy < W and grid[x + dx][y + dy] != "#"
    }

part1_solution = len(visited)

# Part 1 Solution: 3743
print(f"Part 1 Solution: {part1_solution}")


# "The main thing to notice for part 2 is that the grid is a square, and there are no obstacles
# in the same row/col of the starting point. Let f(n) be the number of spaces you can reach
# after n steps. Let X be the length of your input grid. f(n), f(n+X), f(n+2X), ...., is a
# quadratic, so you can find it by finding the first 3 values, then use that to interpolate the
# final answer." - https://www.reddit.com/r/adventofcode/comments/18nevo3/comment/keaiiq7/

# "It's using the fact that there aren't any obstacles in the same row/col of the starting point.
# This means two things:
# - The area grows like a diamond
# - After expanding by X, the corners of the diamond are the "start points", just shifted
#   up/down/left/right." - https://www.reddit.com/r/adventofcode/comments/18nevo3/comment/keaphzk/

sx, sy = starting_position[0]
for x in range(H):
    if not grid[x][sy] in "S.":
        raise ValueError("Invalid grid")
for y in range(W):
    if not grid[sx][y] in "S.":
        raise ValueError("Invalid grid")

assert H == W

goal_num_steps = 26_501_365
visited = set(starting_position)
values = []

for step in range(3 * H):
    if step % H == goal_num_steps % H:
        values.append(len(visited))
    visited = {
        (x + dx, y + dy)
        for x, y in visited
        for dx, dy in dxdy
        if grid[(x + dx) % H][(y + dy) % H] != "#"
    }


def lagrangeInterpolatingPolynomial(xs, ys):
    # https://mathworld.wolfram.com/LagrangeInterpolatingPolynomial.html
    assert len(xs) == len(ys)
    n = len(xs)

    def f(x):
        return sum(
            ys[j]
            * math.prod([(x - xs[k]) / (xs[j] - xs[k]) for k in range(n) if k != j])
            for j in range(n)
        )

    return f


f = lagrangeInterpolatingPolynomial(range(len(values)), values)

# goal_num_steps // H == 202300
part2_solution = int(f(goal_num_steps // H))

# Part 2 Solution: 618261433219147
print(f"Part 2 Solution: {part2_solution}")
