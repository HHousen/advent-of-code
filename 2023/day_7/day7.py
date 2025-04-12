from collections import Counter
from itertools import groupby, chain, combinations_with_replacement

with open("puzzle_input.txt", "r") as puzzle_input:
    puzzle_input = puzzle_input.read().splitlines()

hands = [line.split() for line in puzzle_input]
hands = [(hand, int(score)) for hand, score in hands]

card_types = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]


def get_hand_type(hand):
    c = Counter(hand)
    if any([c[card] == 5 for card in c]):  # five of a kind
        hand_type = 1
    elif any([c[card] == 4 for card in c]):  # four of a kind
        hand_type = 2
    elif any([c[card] == 3 for card in c]) and any([c[card] == 2 for card in c]):  # full house
        hand_type = 3
    elif any([c[card] == 3 for card in c]) and not any([c[card] == 2 for card in c]):  # three of a kind
        hand_type = 4
    elif sum([c[card] == 2 for card in c]) == 2:  # two pairs
        hand_type = 5
    elif sum([c[card] == 2 for card in c]) == 1 and not any([c[card] == 3 for card in c]):  # one pair
        hand_type = 6
    elif all([c[card] == 1 for card in c]):  # high card
        hand_type = 7
    return hand_type


def better_hand(hand1, hand2, non_digit_mapping):
    hand1 = [int(x) if x.isdigit() else non_digit_mapping[x] for x in list(hand1)]
    hand2 = [int(x) if x.isdigit() else non_digit_mapping[x] for x in list(hand2)]
    for card1, card2 in zip(hand1, hand2):
        if card1 > card2:
            return True
        elif card1 < card2:
            return False


def solve(p2=False):
    hands_by_type = []
    for hand, score in hands:
        if "J" in hand and p2:
            possible_hand_types = set()
            J_positions = [idx for idx, card in enumerate(hand) if card == "J"]
            combinations_of_J = combinations_with_replacement(
                card_types, len(J_positions)
            )
            for cards in combinations_of_J:
                new_hand = list(hand)
                for idx, card in zip(J_positions, cards):
                    new_hand[idx] = card
                hand_type = get_hand_type(new_hand)
                possible_hand_types.add(hand_type)
            hand_type = min(possible_hand_types)
        else:
            hand_type = get_hand_type(hand)
        hands_by_type.append((hand, score, hand_type))

    hands_by_type = sorted(hands_by_type, key=lambda x: x[2])

    hands_by_type = [list(g) for _, g in groupby(hands_by_type, lambda x: x[2])]

    non_digit_mapping = {
        "A": 14,
        "K": 13,
        "Q": 12,
        "J": 11,
        "T": 10,
    }
    if p2:
        non_digit_mapping["J"] = 1

    for hand_grouping in hands_by_type:
        if len(hand_grouping) <= 1:
            continue
        done_sorting = False
        while not done_sorting:
            done_sorting = True
            for idx in range(len(hand_grouping)):
                if idx == len(hand_grouping) - 1:
                    break
                current_hand = hand_grouping[idx]
                next_hand = hand_grouping[idx + 1]
                if better_hand(next_hand[0], current_hand[0], non_digit_mapping):
                    hand_grouping[idx] = next_hand
                    hand_grouping[idx + 1] = current_hand
                    done_sorting = False

    hands_by_type = list(chain.from_iterable(hands_by_type))

    total_winnings = 0
    for rank, hand in zip(range(len(hands_by_type), -1, -1), hands_by_type):
        bid = hand[1]
        total_winnings += bid * rank
    return total_winnings


part1_solution = solve(p2=False)

# Part 1 Solution: 251216224
print(f"Part 1 Solution: {part1_solution}")

part2_solution = solve(p2=True)

# Part 2 Solution: 250825971
print(f"Part 2 Solution: {part2_solution}")
