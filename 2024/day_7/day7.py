from itertools import product

with open("puzzle_input.txt", "r") as puzzle_input:
    puzzle_input = puzzle_input.read().splitlines()

equations = [x.split(": ") for x in puzzle_input]
equations = [
    (int(solution), list(map(int, numbers.split(" "))))
    for solution, numbers in equations
]


def solve(p2=False):
    total = 0
    for solution, numbers in equations:
        prod = product("*+|" if p2 else "*+", repeat=len(numbers) - 1)
        for op in prod:
            result = numbers[0]
            for number, sop in zip(numbers[1:], op):
                if sop == "+":
                    result += number
                elif sop == "*":
                    result *= number
                else:
                    result = int(str(result) + str(number))
                if result > solution:
                    break
            if result == solution:
                total += result
                break
    return total


part1_solution = solve()

# Part 1 Solution: 14711933466277
print(f"Part 1 Solution: {part1_solution}")

part2_solution = solve(p2=True)

# Part 2 Solution: 286580387663654
print(f"Part 2 Solution: {part2_solution}")
