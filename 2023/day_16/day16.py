from collections import deque

with open("puzzle_input.txt", "r") as puzzle_input:
    puzzle_input = puzzle_input.read().splitlines()


def num_energized(start_state):
    queue = deque([start_state])
    visited = set()
    while queue:
        position, direction = queue.popleft()
        while (position, direction) not in visited:
            visited.add((position, direction))
            position = (position[0] + direction[0], position[1] + direction[1])
            if position[0] < 0 or position[1] < 0:
                break
            try:
                item = puzzle_input[position[0]][position[1]]
            except IndexError:
                break
            match item:
                case "/":
                    direction = (-direction[1], -direction[0])
                case "\\":
                    direction = (direction[1], direction[0])
                case "|":
                    if direction[0] == 0:
                        direction = (1, 0)
                        queue.append((position, (-1, 0)))
                case "-":
                    if direction[1] == 0:
                        direction = (0, -1)
                        queue.append((position, (0, 1)))
    return len(set(position for position, _ in visited)) - 1


part1_solution = num_energized(((0, -1), (0, 1)))

# Part 1 Solution: 8323
print(f"Part 1 Solution: {part1_solution}")

h = len(puzzle_input) - 1
w = len(puzzle_input[0]) - 1
states = (
    [((h + 1, x), (-1, 0)) for x in range(w)]
    + [((y, w + 1), (0, -1)) for y in range(h)]
    + [((-1, x), (1, 0)) for x in range(w)]
    + [((y, -1), (0, 1)) for y in range(h)]
)

part2_solution = max(num_energized(state) for state in states)

# Part 2 Solution: 8491
print(f"Part 2 Solution: {part2_solution}")
