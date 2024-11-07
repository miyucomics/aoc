with open("input.txt") as file:
    world = file.read()
    world_width = len(world.split("\n")[0])
    world_height = world.count("\n")
    world = world.replace("\n", "")

def get(x, y):
    if x < 0 or x >= world_width or y < 0 or y >= world_height:
        return 0
    return int(world[y * world_width + x])

def is_visible(x, y):
    tree_height = get(x, y)
    return any([
        all(get(x, dy) < tree_height for dy in range(y)),  # top
        all(get(x, dy) < tree_height for dy in range(y + 1, world_height)),  # bottom
        all(get(dx, y) < tree_height for dx in range(x)),  # left
        all(get(dx, y) < tree_height for dx in range(x + 1, world_width)),  # right
    ])

print((world_height + world_width - 2) * 2 + sum(
    is_visible(x, y)
    for x in range(1, world_width - 1)
    for y in range(1, world_height - 1)
))
