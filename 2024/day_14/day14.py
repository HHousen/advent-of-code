import math
import re


with open("puzzle_input.txt", "r") as puzzle_input:
    puzzle_input = puzzle_input.read().splitlines()

nX = 101
nY = 103

robots = [list(map(int, re.findall(r"-?\d+", robot))) for robot in puzzle_input]

for step in range(100):
    for robot in robots:
        robot[0] = (robot[0] + robot[2]) % nX
        robot[1] = (robot[1] + robot[3]) % nY

num_quadrants = [0, 0, 0, 0]
for robot in robots:
    px, py = robot[0], robot[1]
    if px < nX // 2 and py < nY // 2:
        num_quadrants[0] += 1
    elif px > nX // 2 and py < nY // 2:
        num_quadrants[1] += 1
    elif px < nX // 2 and py > nY // 2:
        num_quadrants[2] += 1
    elif px > nX // 2 and py > nY // 2:
        num_quadrants[3] += 1

part1_solution = math.prod(num_quadrants)

# Part 1 Solution: 218619120
print(f"Part 1 Solution: {part1_solution}")

idx = 100  # start at 100 because we already did 100 steps for part 1
robot_coords = [(0, 0), (0, 0)]
while len(set(robot_coords)) != len(robot_coords):
    for robot in robots:
        robot[0] = (robot[0] + robot[2]) % nX
        robot[1] = (robot[1] + robot[3]) % nY
    robot_coords = [(robot[0], robot[1]) for robot in robots]
    idx += 1

# Visualize the tree :)
# grid = [["." for _ in range(nX)] for _ in range(nY)]
# for robot in p2_robots:
#     grid[robot[1]][robot[0]] = "#"

# for x in grid:
#     print("".join(x))

part2_solution = idx

# Part 2 Solution: 7055
print(f"Part 2 Solution: {part2_solution}")
