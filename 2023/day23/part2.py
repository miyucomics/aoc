with open("input.txt") as file:
    world = file.read()
    world_width = len(world.split("\n")[0])
    world_height = world.count("\n")
    world = world.replace("\n", "")

def get(x, y):
    if x < 0 or x >= world_width or y < 0 or y >= world_height:
        return "#"
    return world[y * world_width + x]

vertices = []
for i, char in enumerate(world):
    y, x = divmod(i, world_width)
    if char == "#":
        continue
    if sum(get(x + dx, y + dy) != "#" for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]) > 2:
        vertices.append((x, y))

graph = {vertex: {} for vertex in vertices}

def encounter_first_vertex(point):
    distance = 0
    vertex = point
    no_backtrack = point

    while True:
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_x = vertex[0] + dx
            new_y = vertex[1] + dy
            if (new_x, new_y) == no_backtrack:
                continue
            if get(new_x, new_y) == "#":
                continue
            no_backtrack = vertex
            vertex = (new_x, new_y)
            distance += 1
            break
        if vertex in vertices:
            return vertex, distance

start, head = encounter_first_vertex((1, 0))
end, tail = encounter_first_vertex((world_width - 2, world_height - 1))

for junction_x, junction_y in vertices:
    stack = [(junction_x, junction_y, 0)]
    seen = {(junction_x, junction_y)}
    while stack:
        x, y, distance = stack.pop()
        if distance > 0 and (x, y) in vertices:
            graph[(junction_x, junction_y)][(x, y)] = distance
            continue
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_x = x + dx
            new_y = y + dy
            if get(new_x, new_y) != "#" and (new_x, new_y) not in seen:
                stack.append((new_x, new_y, distance + 1))
                seen.add((new_x, new_y))

seen = set()
def search(point):
    if point == end:
        return 0
    max_dist = -1
    seen.add(point)
    for other in graph[point]:
        if other not in seen:
            max_dist = max(max_dist, search(other) + graph[point][other])
    seen.remove(point)
    return max_dist

print(head + search(start) + tail)
