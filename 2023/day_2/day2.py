from collections import defaultdict
import math


with open("puzzle_input.txt", "r") as puzzle_input:
    puzzle_input = puzzle_input.read().splitlines()

games = {}
for line in puzzle_input:
    game_num, rounds = line.split(": ")
    game_num = int(game_num.split()[-1])
    current_game = []
    for round in rounds.split("; "):
        colors = round.split(", ")
        color_dict = {"red": 0, "green": 0, "blue": 0}
        for color in colors:
            num, col = color.split()
            color_dict[col] = int(num)
        current_game.append(color_dict)
    games[game_num] = current_game

p1_total = 0
p2_total = 0
for game_idx, game in games.items():
    broken = False
    maximums = defaultdict(int)
    for round in game:
        for color in ["red", "green", "blue"]:
            maximums[color] = max(maximums[color], round[color])
        if round["red"] > 12 or round["green"] > 13 or round["blue"] > 14:
            broken = True
    if not broken:
        p1_total += game_idx
    p2_total += math.prod(maximums.values())

part1_solution = p1_total
part2_solution = p2_total

# Part 1 Solution: 2679
print(f"Part 1 Solution: {part1_solution}")

# Part 2 Solution: 77607
print(f"Part 2 Solution: {part2_solution}")
