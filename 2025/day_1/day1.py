with open("puzzle_input.txt", "r") as puzzle_input:
    puzzle_input = puzzle_input.read().splitlines()

dial = 50
part1_solution = 0
part2_solution = 0

for line in puzzle_input:
    direction, amount = line[0], int(line[1:])
    part2_solution += amount // 100  # full rotations due to current move

    if direction == "L":
        new_dial = (dial - amount) % 100
        # If `dial == 0`, we are starting from 0, so all rotations are accounted for above.
        # If we end on a 0 or cross over it, we have an additional rotation.
        if dial != 0 and (new_dial == 0 or new_dial > dial):
            part2_solution += 1
    else:
        new_dial = (dial + amount) % 100
        if new_dial < dial:  # must have crossed 0 due to previous dial position
            part2_solution += 1

    dial = new_dial

    if dial == 0:
        part1_solution += 1

# Part 1 Solution: 1141
print(f"Part 1 Solution: {part1_solution}")

# Part 2 Solution: 6634
print(f"Part 2 Solution: {part2_solution}")
