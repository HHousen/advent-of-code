with open("puzzle_input.txt", "r") as puzzle_input:
    puzzle_input = puzzle_input.read().strip()

disk_map = list(map(int, puzzle_input))

free_spaces = []
files = []

filesystem = []
filesystem_idx = 0
for idx, number in enumerate(disk_map):
    file_idx = idx // 2
    free_space = idx % 2 == 1
    val = -1 if free_space else file_idx
    if free_space:
        free_spaces.append((filesystem_idx, number))
    else:
        files.append((filesystem_idx, file_idx, number))
    for i in range(number):
        filesystem.append(val)
    filesystem_idx += number


def part1(filesystem):
    compact_filesystem = filesystem.copy()
    empty_idx = compact_filesystem.index(-1)
    for item in filesystem[::-1]:
        while (
            empty_idx < len(compact_filesystem) and compact_filesystem[empty_idx] != -1
        ):
            empty_idx += 1
        if empty_idx >= len(compact_filesystem):
            return compact_filesystem
        compact_filesystem[empty_idx] = item
        compact_filesystem.pop()


part1_solution = sum(idx * item for idx, item in enumerate(part1(filesystem)))

# Part 1 Solution: 6259790630969
print(f"Part 1 Solution: {part1_solution}")

for idx, (start_fidx, file_fidx, file_size) in enumerate(files[::-1]):
    for free_space_idx, (free_space_fidx, free_space_size) in enumerate(free_spaces):
        if free_space_size >= file_size and free_space_fidx < start_fidx:
            files_idx = len(files) - idx - 1
            files[files_idx] = (free_space_fidx, file_fidx, file_size)
            if free_space_size - file_size == 0:
                free_spaces.pop(free_space_idx)
            else:
                free_spaces[free_space_idx] = (
                    free_space_fidx + file_size,
                    free_space_size - file_size,
                )

            free_spaces.append((start_fidx, file_size))

            free_spaces.sort(key=lambda x: x[0])
            for i in range(len(free_spaces) - 1, 0, -1):
                if free_spaces[i - 1][0] + free_spaces[i - 1][1] == free_spaces[i][0]:
                    free_spaces[i - 1] = (
                        free_spaces[i - 1][0],
                        free_spaces[i - 1][1] + free_spaces[i][1],
                    )
                    free_spaces.pop(i)
            break

part2_solution = 0
for idx, (start_fidx, file_fidx, file_size) in enumerate(files):
    part2_solution += file_fidx * sum(range(start_fidx, start_fidx + file_size))

# Part 2 Solution: 6289564433984
print(f"Part 2 Solution: {part2_solution}")
