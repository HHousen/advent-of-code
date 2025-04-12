with open("puzzle_input.txt", "r") as puzzle_input:
    puzzle_input = puzzle_input.read().splitlines()


def is_strictly_monotone(diff):
    return all(x >= 1 for x in diff) or all(x <= -1 for x in diff)


def is_gradual(diff):
    return all(-3 <= abs(x) <= 3 for x in diff)


def is_safe(report):
    diff = [report[i + 1] - report[i] for i in range(len(report) - 1)]
    return is_strictly_monotone(diff) and is_gradual(diff)


levels = [list(map(int, x.split())) for x in puzzle_input]
part1_solution = sum(is_safe(report) for report in levels)

# Part 1 Solution: 598
print(f"Part 1 Solution: {part1_solution}")


def all_possible_reports(report):
    return [report[:i] + report[i + 1 :] for i in range(len(report))]


part2_solution = sum(
    any(is_safe(report_mod) for report_mod in all_possible_reports(report))
    for report in levels
)

# Part 2 Solution: 634
print(f"Part 2 Solution: {part2_solution}")
