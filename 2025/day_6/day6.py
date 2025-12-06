import math


with open("puzzle_input.txt", "r") as puzzle_input:
    puzzle_input = puzzle_input.read().splitlines()

number_lines, ops_line = puzzle_input[:-1], puzzle_input[-1].split()
number_lines_ints = [list(map(int, line.split())) for line in number_lines]

def solve_problem(op, nums):
    if op == "*":
        return math.prod(nums)
    else:
        return sum(nums)

part1_solution = sum(solve_problem(op, nums) for op, nums in zip(ops_line, zip(*number_lines_ints)))

# Part 1 Solution: 6417439773370
print(f"Part 1 Solution: {part1_solution}")

problem_nums = []
current_nums = []
for column in zip(*number_lines):
    if all(x == " " for x in column):
        problem_nums.append(current_nums)
        current_nums = []
    else:
        current_nums.append(int("".join(column).strip()))
problem_nums.append(current_nums)

part2_solution = sum(solve_problem(op, nums) for op, nums in zip(ops_line, problem_nums))


# Part 2 Solution: 11044319475191
print(f"Part 2 Solution: {part2_solution}")
