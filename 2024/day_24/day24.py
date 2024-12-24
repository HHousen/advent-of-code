from collections import namedtuple


with open("puzzle_input.txt", "r") as puzzle_input:
    puzzle_input = puzzle_input.read()

wire_values, gates = puzzle_input.split("\n\n")
wire_values, gates = wire_values.splitlines(), gates.splitlines()

wire_values = dict(wire_value.split(": ") for wire_value in wire_values)
wire_values = {key: int(value) for key, value in wire_values.items()}
Gate = namedtuple("Gate", ["in1", "op", "in2", "out"])
gates = [Gate(*gate.replace("->", "").split()) for gate in gates]

all_z_wires = {gate.out for gate in gates if gate.out.startswith("z")}

while True:
    for gate in gates:
        if gate.in1 in wire_values and gate.in2 in wire_values:
            output = None
            match gate.op:
                case "AND":
                    output = wire_values[gate.in1] & wire_values[gate.in2]
                case "OR":
                    output = wire_values[gate.in1] | wire_values[gate.in2]
                case "XOR":
                    output = wire_values[gate.in1] ^ wire_values[gate.in2]
            assert output is not None
            wire_values[gate.out] = output
    if all_z_wires.intersection(wire_values.keys()) == all_z_wires:
        break

all_z_wires = list(sorted(all_z_wires, reverse=True))
binary_answer = "".join(str(wire_values[z_wire]) for z_wire in all_z_wires)
part1_solution = int(binary_answer, 2)

# Part 1 Solution: 65740327379952
print("Part 1 Solution:", part1_solution)

# This circuit is a ripple-carry adder: https://en.wikipedia.org/wiki/Adder_(electronics)#Ripple-carry_adder.
# We can guess this because
# 1) we are told its an adder
# 2) there are only AND, OR, and XOR gates
# 3) Advent of Code is probably going to pick a well-known circuit
# 4) When visualizing the circuit in a graph it looks like a ripple-carry adder
# It starts with a half-adder followed by many one-bit full adders.
# Observe the standard diagram for a full adder: https://en.wikipedia.org/wiki/Adder_(electronics)#/media/File:Full-adder_logic_diagram.svg
# I implemented a bunch of checks based on that diagram to make sure everything
# is connected correctly.

greatest_z = all_z_wires[0]
wrong_wires = set()

Gate2 = namedtuple("Gate", ["in1", "op", "in2", "out", "out_ops"])
gates = [Gate2(*gate, set()) for gate in gates]
for gate in gates:
    for inner_gate in gates:
        if gate.out in [inner_gate.in1, inner_gate.in2]:
            gate.out_ops.add(inner_gate.op)

for gate in gates:
    # All gates that output a z wire must be XOR gates except for the last one
    # (which is the final carry out bit of the adder)
    if gate.out[0] == "z" and gate.op != "XOR" and gate.out != greatest_z:
        wrong_wires.add(gate.out)
    # All XOR gates that take in an x or y wire must output to an XOR or AND gate
    if (
        gate.in1[0] in ["x", "y"]
        and gate.in2[0] in ["x", "y"]
        and gate.op == "XOR"
        and "OR" in gate.out_ops
    ):
        wrong_wires.add(gate.out)
    # XOR gates that do not take an x or y wire must output a z wire
    if (
        gate.op == "XOR"
        and gate.in1[0] not in ["x", "y"]
        and gate.in2[0] not in ["x", "y"]
        and gate.out[0] != "z"
    ):
        wrong_wires.add(gate.out)
    # AND gates must output to an OR gate (except for the one in the half adder
    # which takes in the first x and y wires)
    if (
        gate.op == "AND"
        and "x00" not in [gate.in1, gate.in2]
        and "y00" not in [gate.in1, gate.in2]
        and "OR" not in gate.out_ops
    ):
        wrong_wires.add(gate.out)

part2_solution = ",".join(sorted(wrong_wires))

# Part 2 Solution: bgs,pqc,rjm,swt,wsv,z07,z13,z31
print("Part 2 Solution:", part2_solution)
