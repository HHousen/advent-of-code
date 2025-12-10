import re
from collections import deque, namedtuple
from typing import Sequence
from scipy.optimize import linprog


with open("puzzle_input.txt", "r") as puzzle_input:
    puzzle_input = puzzle_input.read().splitlines()

Machine = namedtuple("Machine", ["lights", "buttons", "buttons_mask", "joltages"])

def find_ints(s: str) -> Sequence[int]:
    return list(map(int, re.findall(r"-?\d+", s)))

def parse_line(line):
    lights, *buttons, joltages = line.split()
    # Convert lights and buttons to bitmasks
    lights = sum(1 << idx for idx, x in enumerate(lights[1:-1]) if x == "#")
    joltages = list(map(int, joltages[1:-1].split(",")))
    buttons = [find_ints(b) for b in buttons]
    buttons_mask = [sum(1 << x for x in b) for b in buttons]
    return Machine(lights, buttons, buttons_mask, joltages)

machines = [parse_line(line) for line in puzzle_input]

def solve_p1(machine: Machine) -> int:
    queue = deque([(0, 0)])
    visited = set()
    while queue:
        lights, steps = queue.popleft()
        if lights == machine.lights:
            return steps
        for button in machine.buttons_mask:
            new_lights = lights ^ button
            if new_lights not in visited:
                visited.add(new_lights)
                queue.append((new_lights, steps + 1))

part1_solution = sum(solve_p1(machine) for machine in machines)

# Part 1 Solution: 457
print(f"Part 1 Solution: {part1_solution}")

def solve_p2(machine: Machine) -> int:
    # Goal: Minimize c @ x subject to A_eq @ x == b_eq and x integers >= 0.
    # In other words, minimize the sum of x (number of presses of each button)
    # such that the total effect of the button presses equals the target joltages.
    # c is the coefficients. All 1s since we want to sum the number of presses
    # of each button.
    c = [1] * len(machine.buttons)
    # matrix[i, j] = 1 if button j affects joltage i, else 0
    matrix = [[int(idx in b) for b in machine.buttons] for idx in range(len(machine.joltages))]
    # integrality=1 enforces integer solutions
    # https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.linprog.html
    result = linprog(c, A_eq=matrix, b_eq=machine.joltages, integrality=1)
    # Floating point weirdness™ results in 114.99999999999999 so round.
    return round(result.fun)

part2_solution = sum(solve_p2(machine) for machine in machines)

# Part 2 Solution: 17576
print(f"Part 2 Solution: {part2_solution}")
