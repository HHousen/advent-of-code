from collections import defaultdict
from queue import PriorityQueue


with open("puzzle_input.txt", "r") as puzzle_input:
    puzzle_input = puzzle_input.read().splitlines()


def neighbors_with_restrictions(node, height, width, p2=False):
    x, y, direction, num_straight = node
    for new_direction in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        dx, dy = new_direction
        if p2 and num_straight < 4 and new_direction != direction:
            continue
        if new_direction == (-direction[0], -direction[1]):
            continue
        num_straight_limit = 10 if p2 else 3
        if num_straight >= num_straight_limit and new_direction == direction:
            continue
        new_x, new_y = (x + dx, y + dy)
        if 0 <= new_x < height and 0 <= new_y < width:
            new_num_straight = num_straight + 1 if new_direction == direction else 1
            yield new_x, new_y, new_direction, new_num_straight


def dijkstra(
    grid, sources=[(0, 0, (0, 1), 0), (0, 0, (1, 0), 0)], destination=None, p2=False
):
    # Forked from https://github.com/HHousen/advent-of-code-2021/blob/master/day_15/day15.py
    grid_height, grid_width = len(grid), len(grid[0])
    if not destination:
        destination = (grid_height - 1, grid_width - 1)

    queue = PriorityQueue()
    min_costs = defaultdict(lambda: float("inf"))
    for source in sources:
        queue.put((0, source))
        min_costs[source] = 0
    visited = set()

    while not queue.empty():
        distance, node = queue.get()

        if (node[0], node[1]) == destination:
            return distance

        if node in visited:
            continue

        visited.add(node)
        for neighbor in neighbors_with_restrictions(node, grid_height, grid_width, p2):
            if neighbor in visited:
                continue

            new_x, new_y, _, _ = neighbor
            new_cost = distance + grid[new_x][new_y]
            old_cost = min_costs[neighbor]

            if new_cost < old_cost:
                min_costs[neighbor] = new_cost
                queue.put((new_cost, neighbor))

    return float("inf")


grid = [[int(x) for x in line] for line in puzzle_input]
part1_solution = dijkstra(grid)

# Part 1 Solution: 1065
print(f"Part 1 Solution: {part1_solution}")

part2_solution = dijkstra(grid, p2=True)

# Part 2 Solution: 1249
print(f"Part 2 Solution: {part2_solution}")
