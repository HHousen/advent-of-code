from collections import defaultdict, deque
from queue import PriorityQueue

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

dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]


def neighbors(x, y, direction):
    # Get the coordinates of neighboring items in the grid:
    # 1. moving forward in the current direction
    # 2. turning right and moving forward
    # 3. turning left and moving forward
    for score, new_direction in [
        (1, direction),
        (1001, (direction + 1) % 4),
        (1001, (direction - 1) % 4),
    ]:
        dx, dy = dirs[new_direction]
        new_x, new_y = (x + dx, y + dy)
        if 0 <= new_x < nX and 0 <= new_y < nY and grid[new_x][new_y] != "#":
            yield (new_x, new_y), score, new_direction


def dijkstra(source, destination):
    queue = PriorityQueue()
    # Start with only the source in the `queue` and in the `min_costs` dictionary.
    # The source has a distance of 0 and is moving in direction 0. The coords
    # for direction 0 are dirs[0] = (0, 1).
    queue.put((0, (source, 0)))
    min_costs = defaultdict(lambda: float("inf"))
    min_costs[(source, 0)] = 0
    visited = set()

    p2 = True
    p1_solution = None
    if p2:
        sources = defaultdict(set)

    while not queue.empty():
        # Get the node with the lowest cost/distance from the `source` node.
        distance, node_direction = queue.get()
        node, direction = node_direction

        # If the node with the shortest distance is the `destination` node,
        # then we have the answer (the total distance/cost from the `source` node
        # to the `destination` node).
        if node == destination:
            p1_solution = distance

        # If the node has already been visited, then skip it and test the next node.
        if node_direction in visited:
            continue

        # We have now visited this node so we will add it to the visited set.
        visited.add(node_direction)
        x, y = node

        # for each neighboring node...
        for neighbor, score, new_direction in neighbors(x, y, direction):
            # If this neighbor has already been visited, then skip it and try the next
            # neighbor.
            if (neighbor, new_direction) in visited:
                continue

            # The `new_cost` is the total distance from the `source` to this neighbor.
            new_cost = distance + score
            old_cost = min_costs[(neighbor, new_direction)]

            # If the `new_cost` is less than the previous minimum cost to reach this
            # neighbor, then update the neighbor's minimum cost to the `new_cost`.
            # Add this distance and neighbor to the queue since we have found a better
            # path.
            if new_cost < old_cost:
                min_costs[(neighbor, new_direction)] = new_cost
                queue.put((new_cost, (neighbor, new_direction)))
                if p2:
                    # Since this is the shortest path to the neighbor, we will update the
                    # sources dictionary with the current node to keep track of the
                    # new best way to get to this node.
                    sources[(neighbor, new_direction)] = {(node, direction)}
            elif p2 and new_cost == old_cost:
                # We have found an alternative path to this neighbor with the same cost.
                sources[(neighbor, new_direction)].add((node, direction))

    if p2:
        return sources, p1_solution
    else:
        # Return infinity if there is no path from the `source` to the `destination`.
        return float("inf")


sources, part1_solution = dijkstra(source=start, destination=end)

# Part 1 Solution: 101492
print(f"Part 1 Solution: {part1_solution}")

queue = deque([x for x in sources if x[0] == end])
good_nodes = set()
# Backtrack from the destination node to the source node to find all the nodes that
# are part of all the shortest paths.
while queue:
    node = queue.popleft()
    good_nodes.add(node)
    for source in sources[node]:
        if source not in good_nodes:
            queue.append(source)

part2_solution = len(set(node for node, _ in good_nodes))

# Part 2 Solution: 543
print(f"Part 2 Solution: {part2_solution}")
