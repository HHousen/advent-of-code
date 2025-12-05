with open("puzzle_input.txt", "r") as puzzle_input:
    puzzle_input = [x.splitlines() for x in puzzle_input.read().split("\n\n")]

fresh_ranges, available_ids = puzzle_input
fresh_ranges = [tuple(map(int, x.split("-"))) for x in fresh_ranges]
available_ids = list(map(int, available_ids))

part1_solution = sum(any(a <= available_id <= b for a, b in fresh_ranges) for available_id in available_ids)

# Part 1 Solution: 511
print(f"Part 1 Solution: {part1_solution}")

part2_solution = 0
cur_start = 0
for start, end in sorted(fresh_ranges):
    start = max(cur_start + 1, start)
    part2_solution += max(0, end - start + 1)
    cur_start = max(cur_start, end)

# Part 2 Solution: 350939902751909
print(f"Part 2 Solution: {part2_solution}")
