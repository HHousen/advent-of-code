with open("puzzle_input.txt", "r") as puzzle_input:
    puzzle_input = puzzle_input.read().splitlines()

puzzle_input = [[int(i) for i in line.split()] for line in puzzle_input]


def next_value(row):
    if all(i == 0 for i in row):
        return 0
    new_row = [row[idx + 1] - row[idx] for idx in range(len(row) - 1)]
    return row[-1] + next_value(new_row)


part1_solution = sum(next_value(row) for row in puzzle_input)

# Part 1 Solution: 1696140818
print(f"Part 1 Solution: {part1_solution}")

part2_solution = sum(next_value(row[::-1]) for row in puzzle_input)

# Part 2 Solution: 1152
print(f"Part 2 Solution: {part2_solution}")
