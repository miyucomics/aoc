with open("input.txt") as file:
    world = file.read()
    world_width = world.find("\n")
    world_height = world.count("\n")
    world = world.replace("\n", "")
    world = list(map(lambda x: x == "@", world))

def idx(pos):
    return int(world_width * pos.imag + pos.real)

def get_world(location):
    if location.real < 0 or location.real >= world_width or location.imag < 0 or location.imag >= world_height:
        return False
    return world[idx(location)]

neighbor_map = [0] * world_width * world_height
def modify_neighbors(location, change):
    if location.real < 0 or location.real >= world_width or location.imag < 0 or location.imag >= world_height:
        return False
    neighbor_map[idx(location)] += change

offsets = {
    y * 1j + x
    for x in range(-1, 2)
    for y in range(-1, 2)
    if not (x == 0 and y == 0)
}

actives = {y * 1j + x for x in range(world_width) for y in range(world_height) if get_world(y * 1j + x)}
for active in actives:
    for offset in offsets:
        modify_neighbors(active + offset, 1)

print(sum(1 for pos in actives if neighbor_map[idx(pos)] < 4))
