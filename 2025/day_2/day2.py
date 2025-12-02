with open("puzzle_input.txt", "r") as puzzle_input:
    puzzle_input = puzzle_input.read().strip()

id_ranges = [tuple(map(int, r.split("-"))) for r in puzzle_input.split(",")]

part1_solution = 0
part2_solution = 0

for start, end in id_ranges:
    for id_num in range(start, end + 1):
        id_str = str(id_num)
        id_len = len(id_str)
        half = id_len // 2

        # Part 1: number repeats exactly twice
        if id_len % 2 == 0 and id_str[:half] == id_str[half:]:
            part1_solution += id_num
        
        # Part 2: number repeats two or more times
        for end in range(1, id_len//2+1):
            if id_len % end != 0:  # not evenly divisible
                continue
            num_repeat = id_len // end
            if id_str[:end] * num_repeat == id_str:
                part2_solution += id_num
                break
        
# Part 1 Solution: 37314786486
print(f"Part 1 Solution: {part1_solution}")

# Part 2 Solution: 47477053982
print(f"Part 2 Solution: {part2_solution}")
