import math
import re

with open("puzzle_input.txt", "r") as puzzle_input:
    puzzle_input = puzzle_input.read()

mul_inst_regex = re.compile(r"mul\((\d+),(\d+)\)")
all_muls = mul_inst_regex.findall(puzzle_input)

part1_solution = sum(math.prod(map(int, x)) for x in all_muls)

# Part 1 Solution: 188116424
print(f"Part 1 Solution: {part1_solution}")

part2_solution = 0

buffer = ""
enable_mul = True
for char in puzzle_input:
    buffer += char
    if "do()" in buffer:
        enable_mul = True
        buffer = ""
    elif "don't()" in buffer:
        enable_mul = False
        buffer = ""
    elif enable_mul and buffer.endswith(")"):
        muls = mul_inst_regex.findall(buffer)
        if muls:
            part2_solution += math.prod(map(int, muls[0]))
            buffer = ""

# Part 2 Solution: 104245808
print(f"Part 2 Solution: {part2_solution}")
