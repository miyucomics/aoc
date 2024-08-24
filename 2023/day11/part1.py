with open("input.txt") as file:
    universe = file.read().splitlines()

galaxies = []

y_offset = 0
for y, row in enumerate(universe):
    if "#" not in row:
        y_offset += 1
        continue
    for x, char in enumerate(row):
        if char == "#":
            galaxies.append((x, y + y_offset))

universe = list(zip(*universe))  # transpose the universe

x_offset = 0
for x, row in enumerate(universe):
    if "#" not in row:
        temp = []
        for galaxy in galaxies:
            if galaxy[0] > x + x_offset:
                temp.append((galaxy[0] + 1, galaxy[1]))
            else:
                temp.append(galaxy)
        galaxies = temp
        x_offset += 1

answer = 0
for i, a in enumerate(galaxies):
    for b in galaxies[:i]:
        answer += abs(a[0] - b[0]) + abs(a[1] - b[1])
print(answer)
