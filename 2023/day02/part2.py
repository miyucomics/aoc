with open("input.txt", "r") as file:
    input_text = file.read().splitlines()

answer = 0

for i, game in enumerate(input_text):
    counts = {"red": 0, "green": 0, "blue": 0}
    for pair in game.split(": ")[1].replace("; ", ", ").split(", "):
        number, color = pair.split(" ")
        counts[color] = max(counts[color], int(number))
    answer += counts["red"] * counts["green"] * counts["blue"]

print(answer)
