def process_card(card):
    score = 0
    wins = 0

    win_numbers = [int(num) for num in card.split("|")[0].split()]
    my_numbers = [int(num) for num in card.split("|")[1].split()]

    for number in my_numbers:
        if number in win_numbers:
            wins += 1
            if score == 0:
                score = 1
            else:
                score *= 2

    return (score, wins)


def number_of_wins(card):
    win_numbers = [int(num) for num in card.split("|")[0].split()]
    my_numbers = [int(num) for num in card.split("|")[1].split()]

    return len([num for num in my_numbers if num in win_numbers])


with open("input/day04.txt") as f:
    data = [line.split(": ")[1] for line in f.read().splitlines()]

total_score = 0
for idx, card in enumerate(data):
    card_score, card_wins = process_card(card)
    total_score += card_score

card_counts = [1 for _ in range(len(data))]
card_numbers = [(idx, number_of_wins(data[idx])) for idx in range(len(data))]
for idx, wins in card_numbers:
    for idy in range(idx + 1, idx + wins + 1):
        card_counts[idy] += 1 * card_counts[idx]


print(f"Total number of points: {total_score}")
print(f"Total cards: {sum(card_counts)}")
