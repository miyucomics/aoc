with open("input.txt") as file:
    red_tiles = []
    for line in file.readlines():
        a, b = line.split(",")
        red_tiles.append(int(a) + int(b) * 1j)

answer = 0
for i, a in enumerate(red_tiles):
    for j in range(i + 1, len(red_tiles)):
        b = red_tiles[j]
        offset = a - b
        answer = max(answer, abs((offset.real + 1) * (offset.imag + 1)))

print(int(answer))
