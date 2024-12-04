with open("input.txt", "r") as file:
    world = file.read()
    world_width = world.find("\n")
    world_height = world.count("\n")
    world = world.replace("\n", "")

mirrors = {
    "/": {(1, 0): (0, -1), (-1, 0): (0, 1), (0, 1): (-1, 0), (0, -1): (1, 0)},
    "\\": {(1, 0): (0, 1), (-1, 0): (0, -1), (0, 1): (1, 0), (0, -1): (-1, 0)}
}
splitters = {
    "|": {(1, 0): [(0, -1), (0, 1)], (-1, 0): [(0, -1), (0, 1)], (0, 1): [(0, 1)], (0, -1): [(0, -1)]},
    "-": {(1, 0): [(1, 0)], (-1, 0): [(-1, 0)], (0, 1): [(1, 0), (-1, 0)], (0, -1): [(1, 0), (-1, 0)]}
}

def get(x, y):
    if x < 0 or x >= world_width or y < 0 or y >= world_height:
        return ""
    return world[y * world_width + x]

useless_exits = set()

def evaluate_position(x, y, dx, dy):
    if (x, y) in useless_exits:
        return 0

    beams = [(x, y, dx, dy)]
    energized_tiles = set()
    cache = set()

    while beams:
        x, y, dx, dy = beams.pop()
        while get(x, y) != "":
            energized_tiles.add((x, y))

            iota = get(x, y)
            if iota in mirrors:
                dx, dy = mirrors[iota][(dx, dy)]
            elif iota in splitters:
                if (x, y, dx, dy) in cache:
                    break
                cache.add((x, y, dx, dy))
                new_beams = splitters[iota][(dx, dy)]
                dx, dy = new_beams[0]
                if len(new_beams) == 2:
                    beams.insert(0, (x, y, new_beams[1][0], new_beams[1][1]))

            x += dx
            y += dy
            if get(x, y) == "":
                useless_exits.add((x - dx, y - dy))

    return len(energized_tiles)


answer = 0
for i in range(world_width):
    answer = max(answer, evaluate_position(i, 0, 0, 1))
    answer = max(answer, evaluate_position(i, world_width - 1, 0, -1))
for i in range(world_height):
    answer = max(answer, evaluate_position(0, i, 1, 0))
    answer = max(answer, evaluate_position(world_width - 1, i, -1, 0))

print(answer)
