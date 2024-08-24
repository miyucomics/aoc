with open("input.txt") as file:
    lines = file.read().splitlines()

cache = {}
answer = len(lines)

for index, card in list(enumerate(lines))[::-1]:
    raw = card.replace("  ", " ").split(" | ")
    winning = raw[0].split(": ")[1].split(" ")
    new_cards = sum(1 for number in raw[1].split(" ") if number in winning)
    chain_effect = new_cards + sum(cache[i] for i in range(index + 1, index + new_cards + 1))
    cache[index] = chain_effect
    answer += chain_effect

print(answer)
