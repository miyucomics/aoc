with open("input.txt") as file:
    world = file.read()
    world_width = world.find("\n")
    world_height = world.count("\n")
    world = world.replace("\n", "")

def get(location):
    if location.real < 0 or location.real >= world_width or location.imag < 0 or location.imag >= world_height:
        return "."
    return world[int(world_width * location.imag + location.real)]

answer = 0
visited = set()
for i, plant_type in enumerate(world):
    y, x = divmod(i, world_width)
    position = x + y * 1j
    if position in visited:
        continue

    region = set()
    edges = 0
    stack = [position]
    visited.add(position)

    while stack:
        pos = stack.pop()
        region.add(pos)
        for offset in (-1, 1, -1j, 1j):
            new = pos + offset
            if get(new) != plant_type:
                edges += 1
                continue
            if new not in visited:
                stack.append(new)
                visited.add(new)

    answer += edges * len(region)

print(answer)
