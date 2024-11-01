with open("input.txt", "r") as file:
    world = file.read()
    world_width = len(world.split("\n")[0])
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
        return None
    return world[y * world_width + x]

beams = [(0, 0, 1, 0)]
energized_tiles = set()
cache = set()

while beams:
    x, y, dx, dy = beams.pop()
    while get(x, y) is not None:
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

print(len(energized_tiles))
