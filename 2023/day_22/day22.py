from collections import defaultdict, deque
from copy import deepcopy
import re


with open("puzzle_input.txt", "r") as puzzle_input:
    puzzle_input = puzzle_input.read().splitlines()

blocks = [list(map(int, re.findall(r"\d+", line))) for line in puzzle_input]
# sort by z ascending
blocks.sort(key=lambda x: x[2])

highest = defaultdict(lambda: (0, -1))
cannot_disintegrate = set()

block_dependence_graph = [set() for _ in range(len(blocks))]

for idx, block in enumerate(blocks):
    supports = set()
    block_support_max_height = -1
    for x in range(block[0], block[3] + 1):
        for y in range(block[1], block[4] + 1):
            if highest[x, y][0] + 1 > block_support_max_height:
                block_support_max_height = highest[x, y][0] + 1
                supports = {highest[x, y][1]}
            elif highest[x, y][0] + 1 == block_support_max_height:
                supports.add(highest[x, y][1])

    for support in supports:
        if support != -1:
            block_dependence_graph[support].add(idx)

    if len(supports) == 1:
        cannot_disintegrate.add(supports.pop())

    block_fall_amount = block[2] - block_support_max_height
    for x in range(block[0], block[3] + 1):
        for y in range(block[1], block[4] + 1):
            highest[x, y] = (block[5] - block_fall_amount, idx)


# -1 to remove the ground
part1_solution = len(blocks) - (len(cannot_disintegrate) - 1)

# Part 1 Solution: 430
print(f"Part 1 Solution: {part1_solution}")

# `counts` holds the number of blocks supported by the block with label idx
counts = [0] * len(blocks)
for idx in range(len(blocks)):
    for supported_block in block_dependence_graph[idx]:
        counts[supported_block] += 1


def count_disintegrated(block_dependence_graph, counts, idx):
    queue = deque([idx])
    count = -1
    while queue:
        count += 1
        i = queue.popleft()
        for supported_block in block_dependence_graph[i]:
            counts[supported_block] -= 1
            if counts[supported_block] == 0:
                queue.append(supported_block)
    return count


part2_solution = sum(
    count_disintegrated(block_dependence_graph, deepcopy(counts), idx)
    for idx in range(len(blocks))
)

# Part 2 Solution: 60558
print(f"Part 2 Solution: {part2_solution}")
