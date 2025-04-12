from copy import deepcopy
import math
import re


with open("puzzle_input.txt", "r") as puzzle_input:
    puzzle_input = puzzle_input.read()

workflows, parts = map(str.split, puzzle_input.split("\n\n"))
workflows = dict(workflow.split("{") for workflow in workflows)
workflows = {x: y[:-1].split(",") for x, y in workflows.items()}
parts = [list(map(int, re.findall(r"\d+", part))) for part in parts]


def part_accepted(part, workflow_name):
    if workflow_name == "R":
        return False
    elif workflow_name == "A":
        return True
    workflow = workflows[workflow_name]
    for condition in workflow:
        if ":" in condition:
            cond, outcome = condition.split(":")
            x, m, a, s = part
            if eval(cond):
                return part_accepted(part, outcome)
        else:
            return part_accepted(part, condition)


part1_solution = sum(sum(part) for part in parts if part_accepted(part, "in"))

# Part 1 Solution: 331208
print(f"Part 1 Solution: {part1_solution}")


def update_greater_than(part, rating_name, rating_value):
    rating_value = int(rating_value)
    new_part = deepcopy(part)
    current_range = part[rating_name]
    if current_range.stop < rating_value:
        new_part[rating_name] = range(0)
    elif current_range.start <= rating_value:
        part[rating_name] = range(current_range.start, rating_value + 1)
        new_part[rating_name] = range(rating_value + 1, current_range.stop)
    else:
        part[rating_name] = range(0)
    return part, new_part


def update_less_than(part, rating_name, rating_value):
    rating_value = int(rating_value)
    new_part = deepcopy(part)
    current_range = part[rating_name]
    if current_range.start > rating_value:
        new_part[rating_name] = range(0)
    elif current_range.stop > rating_value:
        new_part[rating_name] = range(current_range.start, rating_value)
        part[rating_name] = range(rating_value, current_range.stop)
    else:
        part[rating_name] = range(0)
    return part, new_part


def num_combinations(part, workflow_name):
    range_lengths = [len(x) for x in part.values()]
    if workflow_name == "R":
        return 0
    elif workflow_name == "A":
        return math.prod(range_lengths)
    total_combinations = 0
    workflow = workflows[workflow_name]
    for condition in workflow:
        if ":" in condition:
            cond, outcome = condition.split(":")
            if ">" in cond:
                rating_name, rating_value = cond.split(">")
                part, new_part = update_greater_than(part, rating_name, rating_value)
                total_combinations += num_combinations(new_part, outcome)
            elif "<" in cond:
                rating_name, rating_value = cond.split("<")
                part, new_part = update_less_than(part, rating_name, rating_value)
                total_combinations += num_combinations(new_part, outcome)
        else:
            total_combinations += num_combinations(part, condition)
    return total_combinations


part2_solution = num_combinations(
    {
        "x": range(1, 4001),
        "m": range(1, 4001),
        "a": range(1, 4001),
        "s": range(1, 4001),
    },
    "in",
)

# Part 2 Solution: 121464316215623
print(f"Part 2 Solution: {part2_solution}")
assert part2_solution == 121464316215623
