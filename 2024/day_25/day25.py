from itertools import product

with open("puzzle_input.txt", "r") as puzzle_input:
    puzzle_input = puzzle_input.read()

keys_and_locks = puzzle_input.split("\n\n")
locks = []
keys = []
for key_or_lock in keys_and_locks:
    key_or_lock = key_or_lock.splitlines()
    is_lock = key_or_lock[0] == "#####"
    heights = []
    for col_idx in range(len(key_or_lock[0])):
        column_height = sum(row[col_idx] == "#" for row in key_or_lock) - 1
        heights.append(column_height)
    if is_lock:
        locks.append(heights)
    else:
        keys.append(heights)

part1_solution = 0

for lock, key in product(locks, keys):
    if not any(l + k > 5 for l, k in zip(lock, key)):
        part1_solution += 1

# Part 1 Solution: 3525
print("Part 1 Solution:", part1_solution)
