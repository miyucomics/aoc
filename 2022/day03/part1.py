with open("input.txt", "r") as file:
    rucksacks = file.read().splitlines()

answer = 0
lookup = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
for rucksack in rucksacks:
    first = set(rucksack[:int(len(rucksack) / 2)])
    second = set(rucksack[int(len(rucksack) / 2):])
    for duplicate in first & second:
        answer += lookup.index(duplicate) + 1

print(answer)
