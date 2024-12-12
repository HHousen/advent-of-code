from collections import deque


with open("puzzle_input.txt", "r") as puzzle_input:
    puzzle_input = puzzle_input.read().splitlines()

grid = [list(row) for row in puzzle_input]
nX = len(grid)
nY = len(grid[0])


def ggrid(x, y):
    if 0 <= x < nX and 0 <= y < nY:
        return grid[x][y]
    return "#"


neighbors4 = [(-1, 0), (0, -1), (0, 1), (1, 0)]
regions = []

already_in_region = set()
for gx in range(nX):
    for gy in range(nY):
        if (gx, gy) in already_in_region:
            continue
        plant = grid[gx][gy]
        queue = deque([(gx, gy)])
        visited = set()
        side_mod = 0
        num_edges = 0
        while queue:
            x, y = queue.pop()
            if (x, y) in visited:
                continue
            visited.add((x, y))
            for dx, dy in neighbors4:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < nX and 0 <= ny < nY and grid[nx][ny] == plant:
                    queue.append((nx, ny))
            for dx, dy in neighbors4:
                nx = x + dx
                ny = y + dy
                if ggrid(nx, ny) != plant:
                    num_edges += 1
                    if (
                        (dx, dy) == (1, 0)
                        and ggrid(x, y + 1) == plant
                        and ggrid(x + 1, y + 1) != plant
                        or (dx, dy) == (-1, 0)
                        and ggrid(x, y + 1) == plant
                        and ggrid(x - 1, y + 1) != plant
                        or (dx, dy) == (0, 1)
                        and ggrid(x + 1, y) == plant
                        and ggrid(x + 1, y + 1) != plant
                        or (dx, dy) == (0, -1)
                        and ggrid(x + 1, y) == plant
                        and ggrid(x + 1, y - 1) != plant
                    ):
                        side_mod += 1
        regions.append((len(visited), num_edges, num_edges - side_mod))
        already_in_region |= visited

part1_solution = sum([area * perimeter for area, perimeter, _ in regions])
part2_solution = sum([area * sides for area, _, sides in regions])

# Part 1 Solution: 1522850
print(f"Part 1 Solution: {part1_solution}")

# Part 2 Solution: 953738
print(f"Part 2 Solution: {part2_solution}")
