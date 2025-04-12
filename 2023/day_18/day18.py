with open("puzzle_input.txt", "r") as puzzle_input:
    puzzle_input = puzzle_input.read().splitlines()

instructions = list(map(str.split, puzzle_input))

directions_map = {
    "U": (-1, 0),
    "D": (1, 0),
    "L": (0, -1),
    "R": (0, 1),
    "0": (0, 1),
    "1": (1, 0),
    "2": (0, -1),
    "3": (-1, 0),
}


def solve(instructions):
    num_perimeter = 0
    xs = []
    ys = []
    x = y = 0
    for direction, amount in instructions:
        amount = int(amount)
        num_perimeter += amount
        dx, dy = directions_map[direction]
        x += dx * amount
        y += dy * amount
        xs.append(x)
        ys.append(y)

    # Shoelace formula
    area = (
        abs(sum(xs[i] * ys[i + 1] - xs[i + 1] * ys[i] for i in range(len(xs) - 1))) // 2
    )

    # Pick's theorem
    interior_area = area - num_perimeter // 2 + 1

    return interior_area + num_perimeter


part1_solution = solve((x[0], x[1]) for x in instructions)

# Part 1 Solution: 74074
print(f"Part 1 Solution: {part1_solution}")

part2_solution = solve((x[-1][-2], int(int(x[-1][2:-2], 16))) for x in instructions)

# Part 2 Solution: 112074045986829
print(f"Part 2 Solution: {part2_solution}")
