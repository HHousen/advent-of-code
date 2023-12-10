from collections import deque

with open("puzzle_input.txt", "r") as puzzle_input:
    puzzle_input = puzzle_input.read().splitlines()

grid = puzzle_input
height = len(grid)
width = len(grid[0])

starting_coords = [
    (x, y) for x in range(height) for y in range(width) if grid[x][y] == "S"
][0]

S_type = None


def set_S_type(S_x, neighbors_x):
    global S_type
    if S_x - 1 in neighbors_x:  # S is |, J, or L
        S_type = True
    else:
        S_type = False


def get_neighbors(grid, x, y):
    item = grid[x][y]
    match item:
        case "|":
            neighbors = [(x - 1, y), (x + 1, y)]
        case "-":
            neighbors = [(x, y - 1), (x, y + 1)]
        case "L":
            neighbors = [(x - 1, y), (x, y + 1)]
        case "J":
            neighbors = [(x - 1, y), (x, y - 1)]
        case "7":
            neighbors = [(x + 1, y), (x, y - 1)]
        case "F":
            neighbors = [(x, y + 1), (x + 1, y)]
        case "S":
            neighbors4 = [(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)]
            neighbors = [
                (i, j) for i, j in neighbors4 if (x, y) in get_neighbors(grid, i, j)
            ]
            set_S_type(x, [x[0] for x in neighbors])

    for neighbor_x, neighbor_y in neighbors:
        if (0 <= neighbor_x < height) and (0 <= neighbor_y < width):
            yield neighbor_x, neighbor_y


pipe = set()
queue = deque([starting_coords])
while queue:
    x, y = queue.popleft()
    for neighbor_coords in get_neighbors(grid, x, y):
        if neighbor_coords not in pipe:
            queue.append(neighbor_coords)
            pipe.add(neighbor_coords)

part1_solution = len(pipe) // 2

# Part 1 Solution: 6738
print(f"Part 1 Solution: {part1_solution}")

inside_space = 0
for x in range(height):
    currently_inside = False
    for y in range(width):
        if (x, y) in pipe:
            # scan each line and keep track of vertical bars that are passed.
            # we are inside the pipe if the number of bars we have passed in
            # this line is odd. `S_type` is true if S is |, J, or L.
            if grid[x][y] in "|JL" or (grid[x][y] == "S" and S_type):
                currently_inside = not currently_inside
        else:
            inside_space += currently_inside

part2_solution = inside_space

# Part 2 Solution: 579
print(f"Part 2 Solution: {part2_solution}")
