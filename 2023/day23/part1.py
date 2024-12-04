with open("input.txt") as file:
    world = file.read()
    world_width = world.find("\n")
    world_height = world.count("\n")
    world = world.replace("\n", "")

def get(x, y):
    if x < 0 or x >= world_width or y < 0 or y >= world_height:
        return "#"
    return world[y * world_width + x]

start = (1, 0)
end = (world_width - 2, world_height - 1)

vertices = [start, end]
for i, char in enumerate(world):
    if char == "#":
        continue
    y, x = divmod(i, world_width)
    if sum(get(x + dx, y + dy) != "#" for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]) > 2:
        vertices.append((x, y))

graph = {vertex: {} for vertex in vertices}
dirs = {"^": [(0, -1)], "v": [(0, 1)], "<": [(-1, 0)], ">": [(1, 0)], ".": [(-1, 0), (1, 0), (0, -1), (0, 1)]}

for junction_x, junction_y in vertices:
    stack = [(junction_x, junction_y, 0)]
    seen = {(junction_x, junction_y)}
    while stack:
        x, y, distance = stack.pop()
        if distance > 0 and (x, y) in vertices:
            graph[(junction_x, junction_y)][(x, y)] = distance
            continue
        for dx, dy in dirs[get(x, y)]:
            new_x = x + dx
            new_y = y + dy
            if get(new_x, new_y) != "#" and (new_x, new_y) not in seen:
                stack.append((new_x, new_y, distance + 1))
                seen.add((new_x, new_y))

def search(point):
    if point == end:
        return 0

    max_dist = -1
    for other in graph[point]:
        max_dist = max(max_dist, search(other) + graph[point][other])

    return max_dist

print(search(start))
