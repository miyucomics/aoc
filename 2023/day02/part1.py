with open("input.txt", "r") as file:
    input_text = file.read().splitlines()

def is_possible(game):
    counts = {"red": 0, "green": 0, "blue": 0}
    for pair in game.split(": ")[1].replace("; ", ", ").split(", "):
        number, color = pair.split(" ")
        counts[color] = max(counts[color], int(number))
        if counts["red"] > 12 or counts["green"] > 13 or counts["blue"] > 14:
            return False
    return True

print(sum(i + 1 for i, game in enumerate(input_text) if is_possible(game)))
