from functools import cache

with open("puzzle_input.txt", "r") as puzzle_input:
    puzzle_input = puzzle_input.read().splitlines()

keypad = {
    "7": (0, 0),
    "8": (0, 1),
    "9": (0, 2),
    "4": (1, 0),
    "5": (1, 1),
    "6": (1, 2),
    "1": (2, 0),
    "2": (2, 1),
    "3": (2, 2),
    "0": (3, 1),
    "A": (3, 2),
}

d_keypad = {
    "^": (0, 1),
    "A": (0, 2),
    "<": (1, 0),
    "v": (1, 1),
    ">": (1, 2),
}


@cache
def solve1(code, cur_char, keys="pad", left_first=False):
    if keys == "pad":
        keys_dict = keypad
    else:
        keys_dict = d_keypad
    if not code:
        return []
    all_moves = set()
    moves = []
    cur_char_x, cur_char_y = keys_dict[cur_char]
    dest_char = code[0]
    dest_char_x, dest_char_y = keys_dict[dest_char]
    dx, dy = dest_char_x - cur_char_x, dest_char_y - cur_char_y
    up_down_first = (cur_char in {"^", "A"} and dest_char == "<") or (
        cur_char in {"0", "A"} and dest_char in {"7", "4", "1"}
    )
    if (not up_down_first) and (
        left_first
        or (cur_char in {"7", "4", "1"} and dest_char in {"0", "A"})
        or (cur_char == "<" and dest_char in {"^", "A"})
    ):
        if dy > 0:
            moves.append(">" * dy)
        elif dy < 0:
            moves.append("<" * -dy)
        if dx > 0:
            moves.append("v" * dx)
        elif dx < 0:
            moves.append("^" * -dx)
    else:
        if dx > 0:
            moves.append("v" * dx)
        elif dx < 0:
            moves.append("^" * -dx)
        if dy > 0:
            moves.append(">" * dy)
        elif dy < 0:
            moves.append("<" * -dy)
    moves.append("A")
    moves = tuple(moves)
    if len(code) > 1:
        if not left_first:
            rest_moves = solve1(code, cur_char, keys, left_first=True)
            all_moves |= rest_moves
        rest_moves = solve1(code[1:], dest_char, keys, left_first=False)
        rest_moves = set(tuple(moves + rm) for rm in rest_moves)
        all_moves |= rest_moves
    else:
        all_moves.add(moves)
    return all_moves


part1_solution = 0
for code in puzzle_input:
    overall_smallest = 10000
    instance = None
    for code1 in solve1(code, "A", "pad"):
        code1 = "".join(code1)
        for code2 in solve1(code1, "A", "dpad"):
            code2 = "".join(code2)
            for code3 in solve1(code2, "A", "dpad"):
                code3 = "".join(code3)
                if len(code3) <= overall_smallest:
                    overall_smallest = len(code3)
                    instance = code3
    print(code, overall_smallest, instance)
    nums_in_code = code[:3]
    part1_solution += overall_smallest * int(nums_in_code)


# Part 1 Solution: 231564
print("Part 1 Solution:", part1_solution)
