with open("input.txt") as file:
    world = file.read()
    world_width = len(world.split("\n")[0])
    world_height = world.count("\n")
    world = world.replace("\n", "")

def get(x, y):
    if x < 0 or x >= world_width or y < 0 or y >= world_height:
        return 0
    return int(world[y * world_width + x])

def calculate_scenic_view(x, y):
    scenic_view = 1
    tree_height = get(x, y)

    distance = 0
    for i in reversed(range(x)):
        distance += 1
        if get(i, y) >= tree_height:
            break
    scenic_view *= distance

    distance = 0
    for i in range(x + 1, world_width):
        distance += 1
        if get(i, y) >= tree_height:
            break
    scenic_view *= distance

    distance = 0
    for i in reversed(range(y)):
        distance += 1
        if get(x, i) >= tree_height:
            break
    scenic_view *= distance

    distance = 0
    for i in range(y + 1, world_height):
        distance += 1
        if get(x, i) >= tree_height:
            break
    scenic_view *= distance

    return scenic_view

print(max(
    calculate_scenic_view(x, y)
    for x in range(1, world_width - 1)
    for y in range(1, world_height - 1)
))
