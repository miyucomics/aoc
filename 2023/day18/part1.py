verts = []

with open("input.txt", "r") as file:
    cursor = (0, 0)
    directions = {
        "U": (0, -1),
        "D": (0, 1),
        "L": (-1, 0),
        "R": (1, 0)
    }

    for (direction, length) in [line.split(" ")[:2] for line in file.read().splitlines()]:
        for i in range(int(length)):
            direction = directions[direction]
            cursor = (cursor[0] + direction[0], cursor[1] + direction[1])
            verts.append(cursor)

def shoelace(vertices):
    n = len(vertices)
    area = 0
    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n]
        area += x1 * y2 - x2 * y1
    area = abs(area) * 0.5
    return area

print(shoelace(verts) + len(verts) / 2 + 1)
