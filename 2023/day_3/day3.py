from collections import defaultdict


with open("puzzle_input.txt", "r") as puzzle_input:
    puzzle_input = puzzle_input.read().splitlines()

grid = {}
for line_idx, line in enumerate(puzzle_input):
    for char_idx, char in enumerate(line):
        grid[(line_idx, char_idx)] = char

symbols = [item for item in grid.values() if (not item.isdigit()) and (item != ".")]

gears = defaultdict(list)

total = 0
current_number = ""
current_gear_position = None
is_adjacent_to_symbol = False
for position, item in grid.items():
    if item.isdigit():
        current_number += item
        if not is_adjacent_to_symbol:
            for adj in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)]:
                adj_position = position[0] + adj[0], position[1] + adj[1]
                symbol_at_position = grid.get(adj_position)
                if symbol_at_position == "*":
                    current_gear_position = adj_position
                if symbol_at_position in symbols:
                    is_adjacent_to_symbol = True
                    break
    else:
        if is_adjacent_to_symbol:
            current_number = int(current_number)
            total += current_number
            if current_gear_position:
                gears[current_gear_position].append(current_number)
        current_number = ""
        is_adjacent_to_symbol = False
        current_gear_position = None

part1_solution = total

p2_total = 0
for gear_position, gear in gears.items():
    if len(gear) > 1:
        p2_total += gear[0] * gear[1]

part2_solution = p2_total

# Part 1 Solution: 538046
print(f"Part 1 Solution: {part1_solution}")

# Part 2 Solution: 81709807
print(f"Part 2 Solution: {part2_solution}")
