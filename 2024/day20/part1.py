with open("input.txt") as file:
    world = file.read()

    world_width = world.find("\n")
    world_height = world.count("\n")
    world = world.replace("\n", "")

    start = world.find("S")
    start = start % world_width + start // world_width * 1j

def get(location):
    return world[int(world_width * location.imag + location.real)]

cursor = start
previous = start
distances = {start: 0}

while get(cursor) != "E":
    for displacement in (-1, 1, -1j, 1j):
        new = cursor + displacement
        if new == previous:
            continue
        if get(new) == "#":
            continue
        previous = cursor
        distances[new] = distances[cursor] + 1
        cursor = new
        break

print(sum(
    pos + move in distances and distances[pos + move] - steps >= 102
    for pos, steps in distances.items()
    for move in (2, 1 + 1j, 2j, -1 + 1j, -2, -1 - 1j, -2j, 1 - 1j)
))
