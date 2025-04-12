from collections import deque

with open("puzzle_input.txt", "r") as puzzle_input:
    puzzle_input = puzzle_input.read().splitlines()

grid = [list(map(int, line)) for line in puzzle_input]
nX = len(grid)
nY = len(grid[0])

neighbors = [(-1, 0), (0, -1), (0, 1), (1, 0)]


def solve(p2=False):
    total_score = 0
    trail_heads = [(i, j) for j in range(nY) for i in range(nX) if grid[i][j] == 0]
    for i, j in trail_heads:
        score = 0
        visited = set()
        queue = deque([(i, j)])
        while queue:
            x, y = queue.pop()
            if not p2 and (x, y) in visited:
                continue
            val = grid[x][y]
            if val == 9:
                score += 1
                if not p2:
                    visited.add((x, y))
                continue
            for dx, dy in neighbors:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < nX and 0 <= ny < nY and grid[nx][ny] == val + 1:
                    queue.append((nx, ny))
            if not p2:
                visited.add((x, y))
        total_score += score
    return total_score


part1_solution = solve()

# Part 1 Solution: 778
print(f"Part 1 Solution: {part1_solution}")


part2_solution = solve(p2=True)

# Part 2 Solution: 1925
print(f"Part 2 Solution: {part2_solution}")
