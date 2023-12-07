import math


with open("puzzle_input.txt", "r") as puzzle_input:
    puzzle_input = puzzle_input.read().splitlines()

first_line = puzzle_input[0].split(": ")[-1]
second_line = puzzle_input[1].split(": ")[-1]

times = map(int, first_line.split())
distances = map(int, second_line.split())

num_winning = []
for time, distance in zip(times, distances):
    num_ways = 0
    for speed_per_ms in range(time):
        our_distance = (time - speed_per_ms) * speed_per_ms
        if our_distance > distance:
            num_ways += 1
    num_winning.append(num_ways)


part1_solution = math.prod(num_winning)

# Part 1 Solution: 512295
print(f"Part 1 Solution: {part1_solution}")

time = int(first_line.replace(" ", ""))
distance = int(second_line.strip().replace(" ", ""))

num_ways = 0
for speed_per_ms in range(time):
    our_distance = (time - speed_per_ms) * speed_per_ms
    if our_distance > distance:
        num_ways += 1

part2_solution = num_ways

# Part 2 Solution: 36530883
print(f"Part 2 Solution: {part2_solution}")
