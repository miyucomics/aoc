with open("input.txt", "r") as file:
    lines = file.read().splitlines()

answer = 0

for card in lines:
    winning_numbers, obtained_numbers = card.replace("  ", " ").split(" | ")
    winning_numbers = winning_numbers.split(": ")[1].split(" ")
    obtained_numbers = obtained_numbers.split(" ")
    won = sum(1 for owned_card in obtained_numbers if owned_card in winning_numbers)
    if won > 0:
        answer += pow(2, won - 1)

print(answer)
