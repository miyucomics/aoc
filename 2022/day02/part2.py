with open("input.txt", "r") as file:
    games = file.read().splitlines()

lookup = {
    "A": {"X": 3, "Y": 1, "Z": 2},
    "B": {"X": 1, "Y": 2, "Z": 3},
    "C": {"X": 2, "Y": 3, "Z": 1}
}
values = {"X": 0, "Y": 3, "Z": 6}

print(sum(
    lookup[opponent][result] + values[result]
    for game in games
    for opponent, result in [game.split(" ")]
))
