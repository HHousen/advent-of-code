with open("puzzle_input.txt", "r") as puzzle_input:
    puzzle_input = puzzle_input.read().splitlines()

p1_total = 0
num_copies = [1] * len(puzzle_input)

for card_idx, line in enumerate(puzzle_input):
    numbers = line.split(": ")[-1]
    winning, have = map(str.split, numbers.split(" | "))

    num_matches = len(set(winning) & set(have))
    if num_matches > 0:
        score = 2**(num_matches-1)
        p1_total += score
    
    to_copy = sum(x in winning for x in have)
    for i in range(card_idx+1, card_idx + to_copy + 1):
        num_copies[i] += num_copies[card_idx]

part1_solution = p1_total

# Part 1 Solution: 24542
print(f"Part 1 Solution: {part1_solution}")

part2_solution = sum(num_copies)

# Part 2 Solution: 8736438
print(f"Part 2 Solution: {part2_solution}")
