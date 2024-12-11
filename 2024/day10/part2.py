with open("input.txt") as file:
    world = file.read()
    world_width = world.find("\n")
    world_height = world.count("\n")
    world = world.replace("\n", "")
    world = list(map(int, world))

    trailheads = [
        i % world_width + i // world_width * 1j
        for i, height in enumerate(world)
        if height == 0
    ]

def get(location):
    if location.real < 0 or location.real >= world_width or location.imag < 0 or location.imag >= world_height:
        return 0
    return world[int(world_width * location.imag + location.real)]

def explore(location, height):
    if height == 9:
        return 1

    return sum(
        explore(location + displacement, height + 1)
        for displacement in [-1, 1, -1j, 1j]
        if get(location + displacement) == height + 1
    )

print(sum(
    explore(trailhead, 0)
    for trailhead in trailheads
))
