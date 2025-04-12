with open("puzzle_input.txt", "r") as puzzle_input:
    puzzle_input = puzzle_input.read().strip()


def get_hash(chars):
    the_hash = 0
    for c in chars:
        the_hash += ord(c)
        the_hash *= 17
        the_hash %= 256
    return the_hash


steps = puzzle_input.split(",")

part1_solution = sum(get_hash(step) for step in steps)

# Part 1 Solution: 515495
print(f"Part 1 Solution: {part1_solution}")

boxes = [{} for _ in range(256)]

for step in steps:
    match step.strip("-").split("="):
        case [label, focal_length]:
            boxes[get_hash(label)][label] = int(focal_length)
        case [label]:
            boxes[get_hash(label)].pop(label, None)

part2_solution = sum(
    (1 + box_idx) * (1 + slot_idx) * focal_length
    for box_idx, box in enumerate(boxes)
    for slot_idx, focal_length in enumerate(box.values())
)

# Part 2 Solution: 229349
print(f"Part 2 Solution: {part2_solution}")
