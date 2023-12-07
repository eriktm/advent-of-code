from collections import Counter


cards = "23456789TJQKA"
hand_type_map = {
    (5,): 0,
    (4, 1): 1,
    (3, 2): 2,
    (3, 1, 1): 3,
    (2, 2, 1): 4,
    (2, 1, 1, 1): 5,
    (1, 1, 1, 1, 1): 6,
}


if __name__ == "__main__":
    with open("input/day07.txt") as f:
        data = f.read().splitlines()
        data = [tuple(line.split()) for line in data]
        hands, bids = zip(*data)

    parsed_hands = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: []}
    for idx, hand in enumerate(hands):
        c = Counter(hand)
        items, counts = list(zip(*c.items()))
        parsed_hands[hand_type_map[tuple(sorted(counts)[::-1])]].append(hand)
    for category in parsed_hands:
        parsed_hands[category] = sorted(
            parsed_hands[category],
            key=lambda x: [cards.index(c) for c in x],
            reverse=True,
        )
    full_sorted_hands = []
    for category in parsed_hands:
        full_sorted_hands.extend(parsed_hands[category])

    base_scoring = list(range(1, len(hands) + 1))[::-1]
    score = 0
    for idx, hand in enumerate(full_sorted_hands):
        score += int(bids[hands.index(hand)]) * base_scoring[idx]

    print("Part 1:", score)
