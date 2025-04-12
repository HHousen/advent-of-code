with open("puzzle_input.txt", "r") as puzzle_input:
    puzzle_input = puzzle_input.read().splitlines()

grid = list(map(list, puzzle_input))
gX = len(grid)
gY = len(grid[0])


def get_guard_location(grid):
    for x in range(gX):
        for y in range(len(grid[x])):
            if grid[x][y] not in ["#", "."]:
                return x, y


def out_of_bounds(x, y):
    return x < 0 or x >= gX or y < 0 or y >= gY


og_guard_x, og_guard_y = get_guard_location(grid)
og_guard = grid[og_guard_x][og_guard_y]
grid[og_guard_x][og_guard_y] = "."

turn_right = {"<": "^", "^": ">", ">": "v", "v": "<"}
jump_table = {}


def solver(grid, grid_change_coords=None, p2=False):
    global jump_table
    guard = og_guard
    guard_x, guard_y = og_guard_x, og_guard_y
    if not p2:
        guard_positions = set([(og_guard_x, og_guard_y)])
        prev_jump_state = (guard_x, guard_y, guard)
    else:
        guard_states = set([(og_guard_x, og_guard_y, og_guard)])
        grid_change_x, grid_change_y = grid_change_coords
    while not out_of_bounds(guard_x, guard_y):
        ngx, ngy = guard_x, guard_y
        if guard == "<":
            ngy -= 1
        elif guard == ">":
            ngy += 1
        elif guard == "^":
            ngx -= 1
        elif guard == "v":
            ngx += 1

        if out_of_bounds(ngx, ngy):
            break

        try:
            obstacle_in_front = grid[ngx][ngy] == "#"
        except IndexError:
            break
        if obstacle_in_front:
            guard = turn_right[guard]
            if not p2:
                new_state = (guard_x, guard_y, guard)
                jump_table[prev_jump_state] = new_state
                prev_jump_state = new_state
        else:
            guard_x, guard_y = ngx, ngy
            if not p2:
                guard_positions.add((guard_x, guard_y))
        if p2:
            guard_state = (guard_x, guard_y, guard)
            if guard_state in guard_states:
                return True
            if guard_state in jump_table:
                jt_state = jump_table[guard_state]
                if jt_state[0] != grid_change_x and jt_state[1] != grid_change_y:
                    guard_x, guard_y, guard = jt_state
            guard_states.add(guard_state)
    if not p2:
        return guard_positions
    return False


guard_positions = solver(grid)
part1_solution = len(guard_positions)

# Part 1 Solution: 4711
print(f"Part 1 Solution: {part1_solution}")

possible_obstacle_positions = guard_positions.copy() - set([(og_guard_x, og_guard_y)])

num_loops = 0
for popx, popy in possible_obstacle_positions:
    if grid[popx][popy] == "#":
        continue
    new_grid = [row.copy() for row in grid]
    new_grid[popx][popy] = "#"

    if solver(new_grid, grid_change_coords=(popx, popy), p2=True):
        num_loops += 1

part2_solution = num_loops

# Part 2 Solution: 1562
print(f"Part 2 Solution: {part2_solution}")
