from collections import namedtuple
import string


with open("puzzle_input.txt", "r") as puzzle_input:
    puzzle_input = puzzle_input.read().splitlines()

grid = list(map(list, puzzle_input))

nX = len(grid)
nY = len(grid[0])

antenna = namedtuple("antenna", ["freq", "x", "y"])

antennas = []
possible_freqs = string.digits + string.ascii_letters

for x in range(nX):
    for y in range(nY):
        if grid[x][y] in possible_freqs:
            antennas.append(antenna(grid[x][y], x, y))


def solve(p2=False):
    antinode_positions = set()
    for i in range(len(antennas)):
        for j in range(i + 1, len(antennas)):
            if antennas[i].freq == antennas[j].freq:
                x1, y1 = antennas[i].x, antennas[i].y
                x2, y2 = antennas[j].x, antennas[j].y

                dx = x2 - x1
                dy = y2 - y1

                if p2:
                    antinode_positions.add((x1, y1))
                    antinode_positions.add((x2, y2))
                    xx1, yy1 = x1 - dx, y1 - dy
                    xx2, yy2 = x2 + dx, y2 + dy

                if p2:
                    while 0 <= xx1 < nX and 0 <= yy1 < nY:
                        antinode_positions.add((xx1, yy1))
                        xx1 -= dx
                        yy1 -= dy
                    while 0 <= xx2 < nX and 0 <= yy2 < nY:
                        antinode_positions.add((xx2, yy2))
                        xx2 += dx
                        yy2 += dy
                else:
                    if 0 <= x1 - dx < nX and 0 <= y1 - dy < nY:
                        antinode_positions.add((x1 - dx, y1 - dy))
                    if 0 <= x2 + dx < nX and 0 <= y2 + dy < nY:
                        antinode_positions.add((x2 + dx, y2 + dy))
    return len(antinode_positions)


part1_solution = solve()

# Part 1 Solution: 222
print(f"Part 1 Solution: {part1_solution}")


part2_solution = solve(p2=True)

# Part 2 Solution: 884
print(f"Part 2 Solution: {part2_solution}")
