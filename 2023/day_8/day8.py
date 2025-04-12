from math import lcm

with open("puzzle_input.txt", "r") as puzzle_input:
    puzzle_input = puzzle_input.read()

instructions, network_text = puzzle_input.split("\n\n")

network = {}
for line in network_text.strip().split("\n"):
    start, options = line.split(" = ")
    options = options.split(", ")
    network[start] = (options[0][1:], options[1][:-1])


def solve(options, p2=False):
    done = False
    num_steps = 0
    while not done:
        for instruction in instructions:
            num_steps += 1
            choice = "LR".index(instruction)
            next_location = options[choice]
            if next_location[-1] == "Z" if p2 else next_location == "ZZZ":
                done = True
                break
            options = network[next_location]
    return num_steps


part1_solution = solve(network["AAA"], p2=False)

# Part 1 Solution: 17621
print(f"Part 1 Solution: {part1_solution}")

options = [value for key, value in network.items() if key[-1] == "A"]
steps_for_all_paths = [solve(starting_point, p2=True) for starting_point in options]

part2_solution = lcm(*steps_for_all_paths)

# Part 2 Solution: 20685524831999
print(f"Part 2 Solution: {part2_solution}")
