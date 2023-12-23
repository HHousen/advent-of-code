from collections import defaultdict, deque

with open("puzzle_input.txt", "r") as puzzle_input:
    puzzle_input = puzzle_input.read().splitlines()

grid = list(map(list, puzzle_input))
H = len(grid)
W = len(grid[0])

start_coords = [(0, y) for y in range(W) if grid[0][y] == "."][0]
dest_coords = [(H - 1, y) for y in range(W) if grid[H - 1][y] == "."][0]


def get_adjacent(grid, x, y, ignore_slopes=False):
    current_item = grid[x][y]
    if not ignore_slopes and current_item in "<>^v":
        dxdy = {">": [(0, 1)], "<": [(0, -1)], "^": [(-1, 0)], "v": [(1, 0)]}[
            current_item
        ]
    else:
        dxdy = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for dx, dy in dxdy:
        new_x = x + dx
        new_y = y + dy
        if 0 <= new_x < H and 0 <= new_y < W and grid[new_x][new_y] != "#":
            yield (new_x, new_y)


def find_longest_path(grid, start_coords, dest_coords, part2=False):
    queue = deque([(start_coords, 0)])
    visited = set()
    longest_path_length = 0
    distance_delta = 1
    while queue:
        current_xy, distance = queue.pop()
        if distance == -1:
            visited.remove(current_xy)
            continue
        if current_xy == dest_coords:
            longest_path_length = max(longest_path_length, distance)
            continue
        queue.append((current_xy, -1))
        visited.add(current_xy)
        neighbors = grid[current_xy] if part2 else get_adjacent(grid, *current_xy)
        for neighbor_xy in neighbors:
            if part2:
                neighbor_xy, distance_delta = neighbor_xy
            if neighbor_xy in visited:
                continue
            queue.append((neighbor_xy, distance + distance_delta))
    return longest_path_length


part1_solution = find_longest_path(grid, start_coords, dest_coords)

# Part 1 Solution: 2106
print(f"Part 1 Solution: {part1_solution}")

edges = defaultdict(list)
for x in range(H):
    for y in range(W):
        if grid[x][y] != "#":
            edges[x, y] = [
                (coords, 1)
                for coords in list(get_adjacent(grid, x, y, ignore_slopes=True))
            ]

only_two_edges = True
while only_two_edges:
    only_two_edges = False
    for coords, edge_list in edges.items():
        if len(edge_list) == 2:
            only_two_edges = True
            a, b = edge_list
            edges[a[0]].remove((coords, a[1]))
            edges[b[0]].remove((coords, b[1]))
            edges[a[0]].append((b[0], a[1] + b[1]))
            edges[b[0]].append((a[0], a[1] + b[1]))
            del edges[coords]
            break

part2_solution = find_longest_path(edges, start_coords, dest_coords, part2=True)

# Part 2 Solution: 6350
print(f"Part 2 Solution: {part2_solution}")
