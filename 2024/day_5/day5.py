from collections import defaultdict
import re
from graphlib import TopologicalSorter

with open("puzzle_input.txt", "r") as puzzle_input:
    puzzle_input = puzzle_input.read()

rules, pages = puzzle_input.split("\n\n")
rules, pages = rules.splitlines(), pages.splitlines()

rules = [rule.split("|") for rule in rules]


def middle_el(x):
    return x[len(x) // 2]


# def part1_regex():
#     # initial approach without topological sort
#     # the first number in the rule must appear before the second number. anything can be in between
#     rules_regexes = [f"({rule[0]}).*({rule[1]})" for rule in rules]

#     matching_pages = []
#     for page in pages:
#         if all(re.search(rule, page) for rule, rule_raw in zip(rules_regexes, rules) if rule_raw[0] in page and rule_raw[1] in page):
#             matching_pages.append(page)

#     page_numbers = [list(map(int, page.split(","))) for page in matching_pages]
#     middle_numbers = [page[len(page)//2] for page in page_numbers]

#     part1_solution = sum(middle_numbers)
#     return part1_solution, matching_pages

part1_solution = 0
# part1_solution, matching_pages = part1_regex()
# not_matching_pages = [page for page in pages if page not in matching_pages]

rules_ints = [list(map(int, x)) for x in rules]
rules_dict = defaultdict(set)
for rule in rules_ints:
    rules_dict[rule[1]].add(rule[0])


def sort(numbers):
    rules_dict_filtered = {
        key: {v for v in value if v in numbers}
        for key, value in rules_dict.items()
        if key in numbers
    }
    ts = TopologicalSorter(rules_dict_filtered)
    order = list(ts.static_order())
    return order


part2_solution = 0
page_numbers = [list(map(int, page.split(","))) for page in pages]
for page in page_numbers:
    order = sort(page)
    middle = middle_el(order)
    if order == page:  # correct order
        part1_solution += middle
    else:
        part2_solution += middle

# Part 1 Solution: 5651
print(f"Part 1 Solution: {part1_solution}")

# Part 2 Solution: 4743
print(f"Part 2 Solution: {part2_solution}")
