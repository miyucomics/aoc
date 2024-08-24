perimeter = 0
verts = []

with open("input.txt") as file:
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    cursor = (0, 0)

    for color in [line.split("#")[1][:-1] for line in file.read().splitlines()]:
        direction = directions[int(color[-1])]
        length = int(color[:-1], 16)
        perimeter += length

        cursor = (cursor[0] + direction[0] * length, cursor[1] + direction[1] * length)
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

print(shoelace(verts) + perimeter / 2 + 1)
