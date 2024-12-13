with open("input.txt") as file:
    world = file.read()
    world_width = world.find("\n")
    world_height = world.count("\n")
    world = world.replace("\n", "")

def get(location):
    if location.real < 0 or location.real >= world_width or location.imag < 0 or location.imag >= world_height:
        return "."
    return world[int(world_width * location.imag + location.real)]

corner_offsets = (-0.5 - 0.5j, 0.5 - 0.5j, 0.5 + 0.5j, -0.5 + 0.5j)

answer = 0
visited = set()
for i, plant_type in enumerate(world):
    y, x = divmod(i, world_width)
    position = x + y * 1j
    if position in visited:
        continue

    region = set()
    stack = [position]
    visited.add(position)

    while stack:
        pos = stack.pop()
        region.add(pos)
        for offset in (-1, 1, -1j, 1j):
            new = pos + offset
            if new not in visited and get(new) == plant_type:
                stack.append(new)
                visited.add(new)

    sides = 0
    possible_corners = set(
        plot + offset
        for plot in region
        for offset in corner_offsets
    )

    for corner in possible_corners:
        surroundings = [corner + offset in region for offset in corner_offsets]
        neighbors = sum(surroundings)
        if neighbors == 1:
            sides += 1
        elif neighbors == 2 and (surroundings == [True, False, True, False] or surroundings == [False, True, False, True]):
            sides += 2
        elif neighbors == 3:
            sides += 1

    answer += sides * len(region)

print(answer)
