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

moves = set()
for x in range(0, 21):
    for y in range(0, 21 - x):
        moves.add(-x - y * 1j)
        moves.add(-x + y * 1j)
        moves.add(x - y * 1j)
        moves.add(x + y * 1j)

print(sum(
    pos + move in distances and distances[pos + move] - steps - (abs(move.real) + abs(move.imag)) >= 100
    for pos, steps in distances.items()
    for move in moves
))
