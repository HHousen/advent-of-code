from collections import Counter

with open("puzzle_input.txt", "r") as puzzle_input:
    puzzle_input = puzzle_input.read().strip()

stones = list(map(int, puzzle_input.split()))

p1_stones = stones.copy()


def solve_naive(stones):
    for _ in range(25):
        new_stones = []
        for stone in stones:
            if stone == 0:
                new_stones.append(1)
            elif len(str(stone)) % 2 == 0:
                digits = str(stone)
                first_half_digits, second_half_digits = (
                    digits[: len(digits) // 2],
                    digits[len(digits) // 2 :],
                )
                new_stones.append(int(first_half_digits))
                new_stones.append(int(second_half_digits))
            else:
                new_stones.append(stone * 2024)
        stones = new_stones
    return stones


def solve_counter(stones):
    stones = Counter(stones)
    p1_ans, p2_ans = 0, 0

    for i in range(75):
        for stone, count in stones.copy().items():
            if stone == 0:
                stones[1] += count
                stones[0] -= count
            elif len(str(stone)) % 2 == 0:
                digits = str(stone)
                first_half_digits, second_half_digits = (
                    digits[: len(digits) // 2],
                    digits[len(digits) // 2 :],
                )
                stones[int(first_half_digits)] += count
                stones[int(second_half_digits)] += count
                stones[stone] -= count
            else:
                stones[stone * 2024] += count
                stones[stone] -= count
        if i == 24:
            p1_ans = sum(stones.values())
    p2_ans = sum(stones.values())
    return p1_ans, p2_ans


part1_solution, part2_solution = solve_counter(p1_stones)

# Part 1 Solution: 203457
print(f"Part 1 Solution: {part1_solution}")

# Part 2 Solution: 241394363462435
print(f"Part 2 Solution: {part2_solution}")
