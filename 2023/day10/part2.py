with open("input.txt", "r") as file:
    world = file.read()
    world_width = world.find("\n")
    world_height = world.count("\n")
    world = world.replace("\n", "")

def get(x, y):
    if x < 0 or x >= world_width or y < 0 or y >= world_height:
        return "."
    return world[y * world_width + x]

moves = {
    (0, -1): lambda a, b: a in "S|LJ" and b in "S|F7",  # up
    (0, 1): lambda a, b: a in "S|F7" and b in "S|LJ",  # down
    (-1, 0): lambda a, b: a in "S-J7" and b in "S-LF",  # left
    (1, 0): lambda a, b: a in "S-LF" and b in "S-J7"  # right
}

visited = []
intersections = []

minx = world_width
miny = world_height
maxx = 0
maxy = 0

starty, startx = divmod(world.index("S"), world_width)
last_x = x = startx
last_y = y = starty

running = True
while running:
    for move, check in moves.items():
        new_x = x + move[0]
        new_y = y + move[1]
        if new_x == last_x and new_y == last_y:
            continue
        if check(get(x, y), get(new_x, new_y)):
            last_x = x
            last_y = y
            visited.append((x, y))
            if get(x, y) in "L|J":
                intersections.append((x, y))
            x = new_x
            y = new_y

            minx = min(minx, x)
            miny = min(miny, y)
            maxx = max(maxx, x)
            maxy = max(maxy, y)

            if x == startx and y == starty:
                running = False
            break

answer = 0
for y in range(miny, maxy):
    inside = False
    for x in range(minx, maxx):
        if (x, y) in intersections:
            inside = not inside
        if (x, y) in visited:
            continue
        if inside:
            answer += 1
print(answer)
