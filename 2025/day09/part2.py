with open("input.txt") as file:
    red_tiles = []
    for line in file.readlines():
        a, b = line.split(",")
        red_tiles.append((int(a), int(b)))

boundary_segments = []
for i in range(len(red_tiles)):
    p1 = red_tiles[i]
    p2 = red_tiles[(i + 1) % len(red_tiles)]
    boundary_segments.append((p1, p2))

def is_inside(point):
    x, y = point
    crossings = 0

    for segment in boundary_segments:
        a, b = segment
        x1, y1 = a
        x2, y2 = b

        if x1 == x2 and x == x1 and min(y1, y2) <= y <= max(y1, y2):
            return True
        if y1 == y2 and y == y1 and min(x1, x2) <= x <= max(x1, x2):
            return True

        if x1 == x2:
            if x < x1 and min(y1, y2) < y < max(y1, y2):
                crossings += 1

    return crossings % 2 == 1

print(is_inside((0, 3)))
