with open("input.txt") as file:
    world = file.read()
    world_width = world.find("\n")
    world_height = world.count("\n")
    world = world.replace("\n", "")
    world = list(map(int, world))

    trailheads = [
        i % world_width + i // world_width * 1j
        for i, char in enumerate(world)
        if char == 0
    ]

def get(location):
    if location.real < 0 or location.real >= world_width or location.imag < 0 or location.imag >= world_height:
        return 0
    return world[int(world_width * location.imag + location.real)]

locations = set()
def explore(location, height):
    if height == 9:
        locations.add(location)

    for displacement in [-1, 1, -1j, 1j]:
        new = location + displacement
        if get(new) == height + 1:
            explore(new, height + 1)

    return len(locations)

answer = 0
for trailhead in trailheads:
    answer += explore(trailhead, 0)
    locations.clear()

print(answer)
