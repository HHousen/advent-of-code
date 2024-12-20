from collections import deque

with open("puzzle_input.txt", "r") as puzzle_input:
    puzzle_input = puzzle_input.read().splitlines()

grid = [list(row) for row in puzzle_input]
nX = len(grid)
nY = len(grid[0])

for x in range(nX):
    for y in range(nY):
        if grid[x][y] == "S":
            start = x, y
            grid[x][y] = "."
        elif grid[x][y] == "E":
            end = x, y
            grid[x][y] = "."

neighbors4 = [(0, 1), (-1, 0), (0, -1), (1, 0)]


def neighbors(x, y):
    for dx, dy in neighbors4:
        new_x, new_y = (x + dx, y + dy)
        if 0 <= new_x < nX and 0 <= new_y < nY and grid[new_x][new_y] != "#":
            yield (new_x, new_y)


def bfs(start, end):
    queue = deque([start])
    visited = set()
    visited.add(start)
    came_from = {start: None}

    while queue:
        current = queue.popleft()
        if current == end:
            break

        for neighbor in neighbors(*current):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                came_from[neighbor] = current

    if end not in came_from:
        return None

    path = []
    current = end
    while current is not None:
        path.append(current)
        current = came_from[current]
    path.reverse()
    return path


path = bfs(start, end)

p1_cheats = 0
p2_cheats = 0
for start_idx in range(len(path)):
    start_x, start_y = path[start_idx]
    for end_idx in range(start_idx + 102, len(path)):
        end_x, end_y = path[end_idx]
        distance = abs(start_x - end_x) + abs(start_y - end_y)
        original_time = end_idx - start_idx
        time_saved = original_time - distance
        if distance == 2:
            p1_cheats += 1
        if distance <= 20 and time_saved >= 100:
            p2_cheats += 1

part1_solution = p1_cheats

# Part 1 Solution: 1511
print("Part 1 Solution:", part1_solution)

part2_solution = p2_cheats

# Part 2 Solution: 1020507
print("Part 2 Solution:", part2_solution)
