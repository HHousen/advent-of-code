from collections import deque
from copy import deepcopy


with open("puzzle_input.txt", "r") as puzzle_input:
    puzzle_input = puzzle_input.read()

grid, moves = puzzle_input.split("\n\n")

grid = [list(row) for row in grid.splitlines()]
p2_grid = deepcopy(grid)
nX = len(grid)
nY = len(grid[0])
moves = moves.replace("\n", "")

for x in range(nX):
    for y in range(nY):
        if grid[x][y] == "@":
            rx, ry = x, y

move_to_coords = {
    "^": (-1, 0),
    "v": (1, 0),
    "<": (0, -1),
    ">": (0, 1),
}

for move in moves:
    dx, dy = move_to_coords[move]
    nx, ny = rx + dx, ry + dy
    bx, by = nx, ny
    boxes = []
    while grid[bx][by] == "O":
        boxes.append((bx, by))
        bx += dx
        by += dy
    if grid[bx][by] != "#":
        boxes.append((bx, by))
        for box_x, box_y in boxes[1:]:
            grid[box_x][box_y] = "O"
        grid[nx][ny] = "."
        rx, ry = nx, ny

part1_solution = 0
for x in range(nX):
    for y in range(nY):
        if grid[x][y] == "O":
            part1_solution += 100 * x + y


# Part 1 Solution: 1406628
print(f"Part 1 Solution: {part1_solution}")


grid2 = [["."] * nY * 2 for _ in range(nX)]
nX2 = nX
nY2 = nY * 2
for x in range(nX):
    for y in range(nY):
        pre_tile = p2_grid[x][y]
        if pre_tile in ["#", "."]:
            grid2[x][y * 2] = pre_tile
            grid2[x][y * 2 + 1] = pre_tile
        elif pre_tile == "O":
            grid2[x][y * 2] = "["
            grid2[x][y * 2 + 1] = "]"
        elif pre_tile == "@":
            grid2[x][y * 2] = "@"
            grid2[x][y * 2 + 1] = "."

for x in range(nX2):
    for y in range(nY2):
        if grid2[x][y] == "@":
            rx, ry = x, y

neighbors_lookup = {
    "^": [(-1, 0), (0, -1), (0, 1)],
    "v": [(1, 0), (0, -1), (0, 1)],
    "<": [(0, -1), (-1, 0), (1, 0)],
    ">": [(0, 1), (-1, 0), (1, 0)],
}
for move in moves:
    dx, dy = move_to_coords[move]
    nx, ny = rx + dx, ry + dy
    bx, by = nx, ny
    boxes = set()
    neighbors = neighbors_lookup[move]
    if move in ["^", "v"]:
        if grid2[bx][by] in ["[", "]"]:
            queue = deque([(bx, by)])
            move = True
            while queue:
                bx, by = queue.popleft()
                if (bx, by) in boxes:
                    continue
                if grid2[bx][by] == "[":
                    boxes.add((bx, by, "["))
                    boxes.add((bx, by + 1, "]"))
                    queue.append((bx + dx, by + dy))
                    queue.append((bx + dx, by + dy + 1))
                elif grid2[bx][by] == "]":
                    boxes.add((bx, by, "]"))
                    boxes.add((bx, by - 1, "["))
                    queue.append((bx + dx, by + dy))
                    queue.append((bx + dx, by + dy - 1))
                elif grid2[bx][by] == "#":
                    move = False
                    break
            if move:
                for box_x, box_y, box_type in boxes:
                    grid2[box_x][box_y] = "."
                for box_x, box_y, box_type in boxes:
                    grid2[box_x + dx][box_y + dy] = box_type
                grid2[nx][ny] = "."
            else:
                continue
        elif grid2[bx][by] == "#":
            continue
        grid2[nx][ny] = "@"
        grid2[rx][ry] = "."
        rx, ry = nx, ny
    else:
        boxes = []
        while grid2[bx][by] in ["[", "]"]:
            boxes.append((bx, by, grid2[bx][by]))
            bx += dx
            by += dy
        if grid2[bx][by] != "#":
            for box_x, box_y, box_type in boxes[1:]:
                grid2[box_x][box_y] = "[" if box_type == "]" else "]"
            if boxes:
                grid2[box_x + dx][box_y + dy] = box_type
            grid2[nx][ny] = "@"
            grid2[rx][ry] = "."
            rx, ry = nx, ny

part2_solution = 0
for x in range(nX2):
    for y in range(nY2):
        if grid2[x][y] == "[":
            part2_solution += 100 * x + y


# Part 2 Solution: 1432781
print(f"Part 2 Solution: {part2_solution}")
