from collections import defaultdict


with open("puzzle_input.txt", "r") as puzzle_input:
    puzzle_input = puzzle_input.read().splitlines()

for idx, x in enumerate(puzzle_input[0]):
    if x == "S":
        start = idx
        break

beams = {start: 1}
splits = 0
for row_idx in range(len(puzzle_input)):
    new_beams = defaultdict(int)
    for beam, count in beams.items():
        if puzzle_input[row_idx][beam] == "^":
            new_beams[beam - 1] += count
            new_beams[beam + 1] += count
            splits += 1
        else:
            new_beams[beam] += count
    beams = new_beams
    # viz = "".join(f"({beams[col_idx]})" if beams[col_idx] > 0 else "." for col_idx in range(len(puzzle_input[0])))
    # input(viz)

part1_solution = splits
part2_solution = sum(beams.values())

# Part 1 Solution: 1649
print(f"Part 1 Solution: {part1_solution}")

# Part 2 Solution: 16937871060075
print(f"Part 2 Solution: {part2_solution}")
