from functools import cache

with open("puzzle_input.txt", "r") as puzzle_input:
    puzzle_input = puzzle_input.read().splitlines()

keypad = {
    "7": (0, 0),
    "8": (1, 0),
    "9": (2, 0),
    "4": (0, 1),
    "5": (1, 1),
    "6": (2, 1),
    "1": (0, 2),
    "2": (1, 2),
    "3": (2, 2),
    "0": (1, 3),
    "A": (2, 3),
}

d_keypad = {
    "^": (1, 0),
    "A": (2, 0),
    "<": (0 ,1),
    "v": (1, 1),
    ">": (2, 1),
}

# Key observations
# 1. Can solve in chunks via dynamic programming because all robots (except the
# one controlling the numeric keypad) must return to A after each press.
# 2. There is a best shortest path between any two buttons. Here, best means
# the path will result in the shortest path for all future robots. The `path`
# function below computes this path between a `start` and `end` button with a
# certain keypad.
#  - The path with the fewest turns is always better. It's always better to
#    go <<^ than to go <^<. Both path result in the same number of moves at
#    the current level (9), but the former path results in fewer moves at
#    deeper levels.
#  - Robots should prioritize moving left before up before down before right.
#    This is because left is the most expensive for future robots since they
#    must press left to reach it. However, once a robot is at the left
#    key, it only needs to go right and up to press any other key, which are
#    the cheapest moves for future robots (since they are right next to the A
#    key).
#  - The only problem here is we need to deal with the gap on each keypad. To
#    do this, we prioritize moving up, down, or right in that order on top of
#    the aforementioned priorities IF the start and end key are part of
#    a specific set of keys. Essentially, if the normal priorities would result
#    in crossing the gap, we reorder the priorities to avoid the gap.


def path(keys, start, end):
    sx, sy = keys[start]
    ex, ey = keys[end]

    priorities = ["<", "^", "v", ">"]

    if start in {"^", "A"} and end == "<":
        priorities.insert(0, "v")
    if (start == "<" and end in {"^", "A"}) or (
        start in {"7", "4", "1"} and end in {"0", "A"}
    ):
        priorities.insert(0, ">")
    if start in {"0", "A"} and end in {"7", "4", "1"}:
        priorities.insert(0, "^")

    final_path = ""
    dx, dy = abs(ex - sx), abs(ey - sy)
    x, y = sx, sy
    for direction in priorities:
        if direction == "<" and ex < x:
            x -= dx
            final_path += "<" * dx
        elif direction == "^" and ey < y:
            y -= dy
            final_path += "^" * dy
        elif direction == "v" and ey > y:
            y += dy
            final_path += "v" * dy
        elif direction == ">" and ex > x:
            x += dx
            final_path += ">" * dx
    final_path += "A"
    return final_path


@cache
def solve(code, final_level, level=0):
    if level > final_level:
        return len(code)
    ans = sum(
        solve(path(d_keypad if level else keypad, start, end), final_level, level + 1)
        for start, end in zip("A" + code, code)
    )
    return ans


def sum_complexities(codes, solutions):
    ans = 0
    for code, solution in zip(codes, solutions):
        nums_in_code = code[:3]
        ans += solution * int(nums_in_code)
    return ans


part1_solution = sum_complexities(
    puzzle_input, [solve(code, 2) for code in puzzle_input]
)

# Part 1 Solution: 231564
print("Part 1 Solution:", part1_solution)

part2_solution = sum_complexities(
    puzzle_input, [solve(code, 25) for code in puzzle_input]
)

# Part 2 Solution: 281212077733592
print("Part 2 Solution:", part2_solution)
