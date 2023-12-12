from functools import cache

with open("puzzle_input.txt", "r") as puzzle_input:
    puzzle_input = puzzle_input.read().splitlines()

data = []
for line in puzzle_input:
    report, groups = line.split()
    groups = tuple(map(int, groups.split(",")))
    data.append((report, groups))


@cache
def work(report, groups, num_broken):
    if len(report) == 0:
        if (num_broken == 0 and len(groups) == 0) or (
            len(groups) == 1 and groups[0] == num_broken
        ):
            return 1
        return 0
    if num_broken > 0 and len(groups) == 0:
        return 0
    num_left = report.count("?") + report.count("#")
    if num_broken == 0 and num_left < sum(groups):
        # early stopping, slight speedup
        return 0
    arrangements = 0
    report0 = report[0]
    if num_broken == 0:
        if report0 in "?#":
            arrangements += work(report[1:], groups, 1)
        if report0 in "?.":
            arrangements += work(report[1:], groups, 0)
    else:
        if report0 == "." and groups[0] != num_broken:
            return 0
        elif report0 in "?." and groups[0] == num_broken:
            arrangements += work(report[1:], groups[1:], 0)
        elif report0 in "#?":
            arrangements += work(report[1:], groups, num_broken + 1)
    return arrangements


part1_solution = sum(work(report, groups, 0) for report, groups in data)

# Part 1 Solution: 7732
print(f"Part 1 Solution: {part1_solution}")

part2_solution = sum(
    work("?".join([report] * 5), groups * 5, 0) for report, groups in data
)

# Part 2 Solution: 4500070301581
print(f"Part 2 Solution: {part2_solution}")
