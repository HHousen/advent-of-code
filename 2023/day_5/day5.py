with open("puzzle_input.txt", "r") as puzzle_input:
    puzzle_input = puzzle_input.read().split("\n\n")

seeds = list(map(int, puzzle_input[0].split(": ")[-1].split()))

mappings = []
for mapping in puzzle_input[1:]:
    current_map = {}
    mapping = mapping.strip().split("\n")[1:]
    for line in mapping:
        dest_range_start, source_range_start, range_length = map(int, line.split())
        source_range_end = source_range_start + range_length
        current_map[(source_range_start, source_range_end)] = (
            dest_range_start - source_range_start
        )
    mappings.append(current_map)

location_numbers = []
for seed in seeds:
    for mapping in mappings:
        for (source_range_start, source_range_end), offset in mapping.items():
            if source_range_start <= seed < source_range_end:
                seed += offset
                break
            # This doesn't handle numbers that are not in any range, which the problem says
            # could occur. This didn't occur for me until part 1.
    location_numbers.append(seed)

part1_solution = min(location_numbers)

# Part 1 Solution: 388071289
print(f"Part 1 Solution: {part1_solution}")

seeds = list(zip(seeds[::2], seeds[1::2]))


def work(seed, mapping, mapping_idx=0):
    # print(f"Working on {seed} with mapping {mapping_idx}")
    seed_start = seed[0]
    seed_range = seed[1]
    seed_end = seed_start + seed_range
    possible_items = []
    for (source_range_start, source_range_end), offset in mapping.items():
        # print(f"Checking {source_range_start} to {source_range_end} with offset {offset}")
        new_start = max(source_range_start, seed_start) + offset
        new_end = min(source_range_end, seed_end) + offset
        new_range = new_end - new_start - 1
        if new_start < new_end:
            if mapping_idx + 1 >= len(mappings):
                # print(f"Found {new_start} to {new_end} with range {new_range}")
                possible_items.append(new_start)
            else:
                possible_items.extend(
                    work(
                        (new_start, new_range),
                        mappings[mapping_idx + 1],
                        mapping_idx=mapping_idx + 1,
                    )
                )
    if len(possible_items) == 0:
        if mapping_idx + 1 >= len(mappings):
            # print(f"Found {seed_start} to {seed_end} with range {seed_range}")
            possible_items.append(seed_start)
        else:
            possible_items.extend(
                work(seed, mappings[mapping_idx + 1], mapping_idx=mapping_idx + 1)
            )

    return possible_items


location_numbers = []

for seed in seeds:
    data = work(seed, mappings[0])
    location_numbers.extend(data)

part2_solution = min(location_numbers)

# Part 2 Solution: 84206669
print(f"Part 2 Solution: {part2_solution}")
