with open("puzzle_input.txt", "r") as puzzle_input:
    puzzle_input = puzzle_input.read().splitlines()

p1_total = 0
p2_total = 0
for line in puzzle_input:
    p1_digits = []
    p2_digits = []
    for line_idx, character in enumerate(line):
        if character.isdigit():
            p1_digits.append(character)
            p2_digits.append(character)
        for num_idx, num_string in enumerate(
            ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        ):
            if line[line_idx:].startswith(num_string):
                p2_digits.append(num_idx + 1)

    p1_total += int(f"{p1_digits[0]}{p1_digits[-1]}")
    p2_total += int(f"{p2_digits[0]}{p2_digits[-1]}")

part1_solution = p1_total
part2_solution = p2_total

# Part 1 Solution: 54634
print(f"Part 1 Solution: {part1_solution}")

# Part 2 Solution: 53855
print(f"Part 2 Solution: {part2_solution}")
