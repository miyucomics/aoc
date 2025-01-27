from collections import defaultdict

with open("input.txt", "r") as file:
    hands = [line.split() for line in file.read().splitlines()]

card_values = "23456789TJQKA"
hand_types = ["11111", "1112", "122", "113", "23", "14", "5"]

def get_strength(hand):
    seen = defaultdict(int)
    sorting_string = ""
    for card in hand[0]:
        sorting_string += str(card_values.index(card)).rjust(2, "0")
        seen[card] += 1

    hand_strength = "".join(str(number) for number in sorted(list(seen.values())))

    return str(hand_types.index(hand_strength)) + sorting_string

hands.sort(key=get_strength)

print(sum(int(hand[1]) * (i + 1) for i, hand in enumerate(hands)))
