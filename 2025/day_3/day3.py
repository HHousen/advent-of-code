with open("puzzle_input.txt", "r") as puzzle_input:
    puzzle_input = puzzle_input.read().splitlines()

def solve(bank, num_picks):
    num_batteries = len(bank)
    pick_idx = -1
    largest = ""
    for idx in range(num_picks):
        end = num_batteries - num_picks + idx + 1
        pick_idx = max(range(pick_idx + 1, end), key=lambda i: bank[i])
        pick = bank[pick_idx]
        largest += pick
    return int(largest)

part1_solution = sum(solve(bank, 2) for bank in puzzle_input)
part2_solution = sum(solve(bank, 12) for bank in puzzle_input)
    
# Part 1 Solution: 17535
print(f"Part 1 Solution: {part1_solution}")

# Part 2 Solution: 173577199527257
print(f"Part 2 Solution: {part2_solution}")
