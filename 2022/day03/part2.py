with open("input.txt", "r") as file:
    rucksacks = [set(line) for line in file.read().splitlines()]

answer = 0
lookup = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

print(sum(
    lookup.index(match) + 1
    for first, second, third in zip(rucksacks[::3], rucksacks[1::3], rucksacks[2::3])
    for match in first & second & third
))
