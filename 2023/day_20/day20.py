from collections import deque
from copy import deepcopy
from math import lcm

with open("puzzle_input.txt", "r") as puzzle_input:
    puzzle_input = puzzle_input.read().splitlines()

modules = {}
flipflop_status = {}
conjunction_memory = {}
for line in puzzle_input:
    source, destinations = line.split(" -> ")
    destinations = destinations.split(", ")
    if source.startswith("%"):
        source = source[1:]
        flipflop_status[source] = 0
    elif source.startswith("&"):
        source = source[1:]
        conjunction_memory[source] = {}
    modules[source] = destinations

for source, destinations in modules.items():
    for destination in destinations:
        if destination in conjunction_memory:
            conjunction_memory[destination][source] = 0


def propagate_pulse(
    modules, flipflop_status, conjunction_memory, sender, receiver, pulse
):
    if receiver in flipflop_status:
        if pulse:
            return
        else:
            next_pulse = flipflop_status[receiver] = not flipflop_status[receiver]
    elif receiver in conjunction_memory:
        conjunction_memory[receiver][sender] = pulse
        next_pulse = not all(conjunction_memory[receiver].values())
    elif receiver in modules:
        next_pulse = pulse
    else:
        return

    for destination in modules[receiver]:
        yield receiver, destination, next_pulse


def step(modules, flipflop_status, conjunction_memory):
    low_pulses = high_pulses = 0
    queue = deque([("button", "broadcaster", 0)])
    while queue:
        sender, receiver, pulse = queue.popleft()
        low_pulses += not pulse
        high_pulses += pulse
        queue.extend(
            propagate_pulse(
                modules, flipflop_status, conjunction_memory, sender, receiver, pulse
            )
        )

    return low_pulses, high_pulses


total_low = total_high = 0
p1_flipflop_status = deepcopy(flipflop_status)
p2_conjunction_memory = deepcopy(conjunction_memory)
for _ in range(1000):
    low_pulses, high_pulses = step(modules, p1_flipflop_status, p2_conjunction_memory)
    total_low += low_pulses
    total_high += high_pulses

part1_solution = total_low * total_high

# Part 1 Solution: 800830848
print(f"Part 1 Solution: {part1_solution}")

# Part 2 solution based on https://www.reddit.com/r/adventofcode/comments/18mmfxb/comment/ke5f13d/:
# "Assume the only module (let's call it A) sending a pulse to rx is a conjunction module, and the
# only modules (B1, B2, ..., Bn) sending a pulse to that one are also conjunction modules.
# We know that A will send a low pulse to rx the first time the remembered state is high for all
# its inputs. Module A can receive high pulses from each Bi, and each Bi will send a high pulse to
# A any time it receives a low pulse. When all Bi modules receive a low pulse in the same iteration,
# they will all send a high pulse to A, which will finally send a low pulse to rx. Assume that this
# happens periodically."


def detect_cycle(modules, flipflop_status, conjunction_memory):
    final_conjunctions = set()
    for source, destinations in modules.items():
        if destinations == ["rx"]:
            rx_source = source
            assert rx_source in conjunction_memory
    for source, destinations in modules.items():
        if rx_source in destinations:
            final_conjunctions.add(source)
            assert source in conjunction_memory

    idx = 1
    cycle_indexes = []
    while True:
        queue = deque([("button", "broadcaster", 0)])
        while queue:
            sender, receiver, pulse = queue.popleft()
            if not pulse and receiver in final_conjunctions:
                cycle_indexes.append(idx)
                final_conjunctions.remove(receiver)
                if not final_conjunctions:
                    return cycle_indexes
            queue.extend(
                propagate_pulse(
                    modules,
                    flipflop_status,
                    conjunction_memory,
                    sender,
                    receiver,
                    pulse,
                )
            )
        idx += 1


part2_solution = lcm(*detect_cycle(modules, flipflop_status, conjunction_memory))

# Part 2 Solution: 244055946148853
print(f"Part 2 Solution: {part2_solution}")
