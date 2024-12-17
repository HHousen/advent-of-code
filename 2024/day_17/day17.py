with open("puzzle_input.txt", "r") as puzzle_input:
    puzzle_input = puzzle_input.read().splitlines()

a = int(puzzle_input[0].split(": ", 1)[-1])
b = int(puzzle_input[1].split(": ", 1)[-1])
c = int(puzzle_input[2].split(": ", 1)[-1])

program = list(map(int, puzzle_input[4].split(": ", 1)[-1].split(",")))


def run(a, b, c, terminate_on_output=False):
    pc = 0
    all_outs = []
    while pc < len(program):
        opcode = program[pc]
        operand = program[pc + 1]
        combo_operand = operand
        if combo_operand == 4:
            combo_operand = a
        elif combo_operand == 5:
            combo_operand = b
        elif combo_operand == 6:
            combo_operand = c
        if opcode == 0:  # adv
            a = int(a / (2**combo_operand))
        elif opcode == 1:  # bxl
            b = b ^ operand
        elif opcode == 2:  # bst
            b = combo_operand % 8
        elif opcode == 3:  # jnz
            if a != 0:
                pc = operand
                continue
        elif opcode == 4:  # bxc
            b = b ^ c
        elif opcode == 5:  # out
            out = combo_operand % 8
            if terminate_on_output:
                return out
            all_outs.append(out)
        elif opcode == 6:  # bdv
            b = int(a / (2**combo_operand))
        elif opcode == 7:  # cdv
            c = int(a / (2**combo_operand))
        pc += 2
    return all_outs


all_outs = run(a, b, c)
part1_solution = ",".join(map(str, all_outs))

# Part 1 Solution: 4,1,7,6,4,1,0,2,7
print(f"Part 1 Solution: {part1_solution}")

# Reversed program:
# def program(a, b, c):
#     b = a & 7
#     b = b ^ 1
#     c = a >> b
#     b = b ^ 5
#     b = b ^ c
#     out = b & 7
#     a = int(a / 8)
#     # then loop to the beginning

# Each iteration is mostly independent of the other iterations. Each iteration only depends
# on the last 3 bits of a and the last 3 bits of a >> b. a is used in two places (besides
# being divided by 8 for the next iteration):
# 1. b is set to the last 3 bits of a
# 2. c is set to a >> b but c is only used to compute the output, which simplifies to
#    out = (b ^ (a >> b)) & 7 with the lines substituted that depend on c. Since b just
#    depends on the last 3 bits of a, the `& 7` means the output depends only on the last
#    3 bits of a >> b (and 1 above).
# Ignoring 2 above (aka just fixing 3 bits at a time) doesn't work. b can be at most 7
# when evaluating a >> b.

# Solution 1: Loop through the program in reverse and find the value of a that produces the
# correct output in that position. Since values past 7 have the potential to change
# future values that the program outputs, we check the entire program output at every
# iteration and make sure to keep looping in case one of the smaller choices that produces
# the value at the current index would change a value later on in the program (which
# is a value we already calculated since we are running in reverse). This is enough
# to solve the puzzle basically instantly.


def solve_loop():
    final_a = 0
    for idx in range(1, len(program) + 1):
        while run(final_a, b, c) != program[-idx:]:
            final_a += 1
        if idx != len(program):
            final_a = final_a << 3
    return final_a


# Solution 2: Recursion. Go through the program in reverse as a graph. Find the value
# that produces the correct output at the current position and then recurse to the
# previous position. If the previous position can't find a value that produces the
# correct output (because the value chosen for the current position modifies a << b
# and makes finding a correct value for the previous position impossible), backtrack and
# try a different value at the current position.


def solve(p, r):
    if p < 0:
        return r
    for d in range(8):
        a = r << 3 | d
        w = run(a, 0, 0, terminate_on_output=True)
        if w == program[p] and (out := solve(p - 1, a)):
            return out
    return False


final_a_loop = solve_loop()
final_a_recursive = solve(len(program) - 1, 0)
assert final_a_loop == final_a_recursive, f"{final_a_loop} != {final_a_recursive}"

test_run_out = run(final_a_recursive, b, c)
assert test_run_out == program, f"{test_run_out} != {program}"

part2_solution = final_a_recursive

# Part 2 Solution: 164279024971453
print(f"Part 2 Solution: {part2_solution}")
