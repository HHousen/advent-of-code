with open("puzzle_input.txt", "r") as puzzle_input:
    puzzle_input = puzzle_input.read()

patterns = list(map(str.split, puzzle_input.split("\n\n")))


def horizontal_num_above(pattern, num_smudges):
    for idx in range(len(pattern)):
        if (
            sum(
                x != y
                for row_x, row_y in zip(pattern[idx:], pattern[idx - 1 :: -1])
                for x, y in zip(row_x, row_y)
            )
            == num_smudges
        ):
            return idx
    return 0


def solve(patterns, num_smudges):
    return sum(
        100 * horizontal_num_above(pattern, num_smudges)
        + horizontal_num_above(list(zip(*pattern)), num_smudges)
        for pattern in patterns
    )


part1_solution = solve(patterns, 0)

# Part 1 Solution: 27202
print(f"Part 1 Solution: {part1_solution}")

part2_solution = solve(patterns, 1)

# Part 2 Solution: 41566
print(f"Part 2 Solution: {part2_solution}")
