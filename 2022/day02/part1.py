with open("input.txt", "r") as file:
    games = file.read().splitlines()

lookup = {
    "A": {"X": 3, "Y": 6, "Z": 0},
    "B": {"X": 0, "Y": 3, "Z": 6},
    "C": {"X": 6, "Y": 0, "Z": 3}
}
values = {"X": 1, "Y": 2, "Z": 3}

print(sum(
    lookup[opponent][you] + values[you]
    for game in games
    for opponent, you in [game.split(" ")]
))
