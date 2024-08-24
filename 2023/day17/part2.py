from heapq import heappush, heappop

with open("input.txt") as file:
    world = file.read()
    world_width = len(world.split("\n")[0])
    world_height = world.count("\n")
    world = world.replace("\n", "")

def get(x, y):
    if x < 0 or x >= world_width or y < 0 or y >= world_height:
        return ""
    return int(world[y * world_width + x])

seen = set()
queue = [(0, 0, 0, 0, 0, 0)]

while queue:
    heat, x, y, dx, dy, straight_moves = heappop(queue)

    if x == world_width - 1 and y == world_height - 1 and straight_moves >= 4:
        print(heat)
        exit()

    if (x, y, dx, dy, straight_moves) in seen:
        continue
    seen.add((x, y, dx, dy, straight_moves))

    if straight_moves < 10 and (dx, dy) != (0, 0):
        new_x = x + dx
        new_y = y + dy
        if get(new_x, new_y) != "":
            heappush(queue, (heat + get(new_x, new_y), new_x, new_y, dx, dy, straight_moves + 1))

    if straight_moves >= 4 or (dx, dy) == (0, 0):
        for new_dx, new_dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if (new_dx, new_dy) == (dx, dy):
                continue
            if (new_dx, new_dy) == (-dx, -dy):
                continue

            new_x = x + new_dx
            new_y = y + new_dy
            if get(new_x, new_y) != "":
                heappush(queue, (heat + get(new_x, new_y), new_x, new_y, new_dx, new_dy, 1))
