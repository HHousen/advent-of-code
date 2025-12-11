from functools import cache

with open("puzzle_input.txt", "r") as puzzle_input:
    puzzle_input = puzzle_input.read().splitlines()

machine_connections = {"out": []}
for line in puzzle_input:
    machine, connections = line.split(": ")
    machine_connections[machine] = connections.split()

@cache
def solve(machine, destination):
    if machine == destination:
        return 1
    return sum(solve(conn, destination) for conn in machine_connections[machine])

part1_solution = solve("you", "out")

# Part 1 Solution: 566
print(f"Part 1 Solution: {part1_solution}")

part2_solution = (
    solve("svr", "dac") * solve("dac", "fft") * solve("fft", "out") +
    solve("svr", "fft") * solve("fft", "dac") * solve("dac", "out")
)

# Part 2 Solution: 331837854931968
print(f"Part 2 Solution: {part2_solution}")
