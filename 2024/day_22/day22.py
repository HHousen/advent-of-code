from collections import Counter, deque


with open("puzzle_input.txt", "r") as puzzle_input:
    puzzle_input = puzzle_input.read().splitlines()

buyers = list(map(int, puzzle_input))


def next_secret(secret):
    secret = secret ^ secret * 64 % 16777216
    secret = secret ^ secret // 32 % 16777216
    secret = secret ^ secret * 2048 % 16777216
    return secret


def solve(secret):
    window = deque(maxlen=4)
    window_prices = {}
    prev_price = secret % 10
    for _ in range(2000):
        secret = next_secret(secret)
        price = secret % 10
        diff = price - prev_price
        prev_price = price
        window.append(diff)
        if len(window) == 4:
            window_tuple = tuple(window)
            if window_tuple not in window_prices:
                window_prices[window_tuple] = price  # num_bananas
    return secret, window_prices


secrets2000 = []
sequences_num_bananas = Counter()
for initial_num in buyers:
    secret2000, prices = solve(initial_num)
    secrets2000.append(secret2000)
    sequences_num_bananas.update(prices)

part1_solution = sum(secrets2000)

# Part 1 Solution: 12664695565
print("Part 1 Solution:", part1_solution)

# sequence with the most bananas
part2_solution = sequences_num_bananas.most_common(1)[0][-1]

# Part 2 Solution: 1444
print("Part 2 Solution:", part2_solution)
