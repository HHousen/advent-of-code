from collections import namedtuple
import re

with open("puzzle_input.txt", "r") as puzzle_input:
    puzzle_input = puzzle_input.read()

raw_games = puzzle_input.split("\n\n")
Game = namedtuple("Game", ["ax", "ay", "bx", "by", "prize_x", "prize_y"])
the_games = [Game(*list(map(int, re.findall(r"\d+", game)))) for game in raw_games]
p2_games = [
    Game(
        game.ax,
        game.ay,
        game.bx,
        game.by,
        game.prize_x + 10000000000000,
        game.prize_y + 10000000000000,
    )
    for game in the_games
]


def solve_numpy(p2=False):
    import numpy as np

    games = p2_games if p2 else the_games
    score = 0
    for game in games:
        a = np.array([[game.ax, game.bx], [game.ay, game.by]])
        b = np.array([game.prize_x, game.prize_y])
        res = np.linalg.solve(a, b)
        a, b = res
        if not (
            np.isclose(a, round(a), atol=1e-20, rtol=1e-14)
            and np.isclose(b, round(b), atol=1e-20, rtol=1e-14)
        ):
            continue
        score += 3 * a + b
    return int(score)


def solve_python(p2=False):
    games = p2_games if p2 else the_games
    score = 0
    for game in games:
        a = (game.prize_x * game.by - game.bx * game.prize_y) // (
            game.ax * game.by - game.bx * game.ay
        )
        b = (game.prize_y - game.ay * a) // game.by
        if (
            game.ax * a + game.bx * b != game.prize_x
            or game.ay * a + game.by * b != game.prize_y
        ):
            continue
        score += 3 * a + b
    return score


part1_solution = solve_python()

# Part 1 Solution: 28753
print(f"Part 1 Solution: {part1_solution}")

part2_solution = solve_python(p2=True)

# Part 2 Solution: 102718967795500
print(f"Part 2 Solution: {part2_solution}")
