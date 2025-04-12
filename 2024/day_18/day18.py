from collections import deque


with open("puzzle_input.txt", "r") as puzzle_input:
    puzzle_input = puzzle_input.read().splitlines()

nX = 71
nY = 71
grid = [["." for _ in range(nX)] for _ in range(nY)]

for line in puzzle_input[:1024]:
    px, py = map(int, line.split(","))
    grid[py][px] = "#"

neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]

fx, fy = nX - 1, nY - 1


def solve(grid):
    queue = deque([(0, 0, 0)])
    visited = set()
    while queue:
        x, y, count = queue.popleft()
        if x == fx and y == fy:
            return count
        if (x, y) in visited:
            continue
        visited.add((x, y))
        for dx, dy in neighbors:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= nX or ny < 0 or ny >= nY:
                continue
            if grid[ny][nx] == ".":
                queue.append((nx, ny, count + 1))
    return None


part1_solution = solve(grid)

# Part 1 Solution: 288
print(f"Part 1 Solution: {part1_solution}")


# Binary search to find the byte that blocks the path
left = 1024
right = len(puzzle_input)
while left < right:
    num_lines = (left + right) // 2
    grid = [["." for _ in range(nX)] for _ in range(nY)]
    for line in puzzle_input[:num_lines]:
        px, py = map(int, line.split(","))
        grid[py][px] = "#"
    if not solve(grid):
        right = num_lines
    else:
        left = num_lines + 1

part2_solution = puzzle_input[left - 1]

# Part 2 Solution: 52,5
print(f"Part 2 Solution: {part2_solution}")
