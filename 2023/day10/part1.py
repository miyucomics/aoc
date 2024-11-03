with open("input.txt", "r") as file:
    world = file.read()
    world_width = len(world.split("\n")[0])
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

starty, startx = divmod(world.index("S"), world_width)
last_x = x = startx
last_y = y = starty
distance = 0

while True:
    for move, check in moves.items():
        new_x = x + move[0]
        new_y = y + move[1]
        if new_x == last_x and new_y == last_y:
            continue
        if check(get(x, y), get(new_x, new_y)):
            last_x = x
            last_y = y
            x = new_x
            y = new_y
            distance += 1
            if x == startx and y == starty:
                print(distance / 2)
                exit()
            break
