with open("input.txt") as file:
    world = file.read()
    world_width = world.find("\n")
    world_height = world.count("\n")
    world = world.replace("\n", "")
    world = list(map(lambda x: x == "@", world))

def get(location):
    if location.real < 0 or location.real >= world_width or location.imag < 0 or location.imag >= world_height:
        return False
    return world[int(world_width * location.imag + location.real)]

offsets = {
    y * 1j + x
    for x in range(-1, 2)
    for y in range(-1, 2)
    if not (x == 0 and y == 0)
}

answer = 0
while True:
    removable = [
        y * 1j + x
        for x in range(world_width)
        for y in range(world_height)
        if get(y * 1j + x)
        if sum(get(y * 1j + x + offset) for offset in offsets) < 4
    ]
    if len(removable) == 0:
        break
    for el in removable:
        world[int(el.imag * world_width + el.real)] = False
    answer += len(removable)

print(answer)
