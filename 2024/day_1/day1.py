from collections import Counter


with open("puzzle_input.txt", "r") as puzzle_input:
    puzzle_input = list(map(int, puzzle_input.read().split()))

nums1, nums2 = puzzle_input[0::2], puzzle_input[1::2]
part1_solution = sum(
    abs(num1 - num2) for num1, num2 in zip(sorted(nums1), sorted(nums2))
)

# Part 1 Solution: 1660292
print(f"Part 1 Solution: {part1_solution}")

c = Counter(nums2)
part2_solution = sum(c[num1] * num1 for num1 in nums1)

# Part 2 Solution: 22776016
print(f"Part 2 Solution: {part2_solution}")
