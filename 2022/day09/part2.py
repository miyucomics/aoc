def sign(x):
    if x > 0:
        return 1
    if x < 0:
        return -1
    return 0

directions = {
    "U": complex(0, 1),
    "D": complex(0, -1),
    "L": complex(-1, 0),
    "R": complex(1, 0),
}

visited = set([0])
points = [complex(0, 0)] * 10

with open("input.txt", "r") as file:
    for instruction in file.read().splitlines():
        direction, distance = instruction.split(" ")
        for _ in range(int(distance)):
            points[0] += directions[direction]
            for i in range(1, len(points)):
                head = points[i - 1]
                tail = points[i]
                offset = head - tail
                if offset.real * offset.real + offset.imag * offset.imag > 2:
                    points[i] += complex(sign(head.real - tail.real), 0)
                    points[i] += complex(0, sign(head.imag - tail.imag))
            visited.add(points[len(points) - 1])

print(len(visited))
