from collections import defaultdict

map = defaultdict(list)

with open("input.txt") as file:
    world = file.read()
    world_width = world.find("\n")
    world_height = world.count("\n")
    world = world.replace("\n", "")

    for i, char in enumerate(world):
        if char != ".":
            y, x = divmod(i, world_width)
            map[char].append(x + y * 1j)

antinodes = set()
def add_antinode(position):
    if position.real < 0 or position.real >= world_width or position.imag < 0 or position.imag >= world_height:
        return
    antinodes.add(position)

for positions in map.values():
    for i in range(len(positions)):
        for j in range(i + 1, len(positions)):
            displacement = positions[j] - positions[i]
            add_antinode(positions[i] - displacement)
            add_antinode(positions[j] + displacement)

print(len(antinodes))
