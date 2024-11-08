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
head = complex(0, 0)
tail = complex(0, 0)

with open("input.txt", "r") as file:
    for instruction in file.read().splitlines():
        direction, distance = instruction.split(" ")
        for _ in range(int(distance)):
            head += directions[direction]
            offset = head - tail
            if offset.real * offset.real + offset.imag * offset.imag > 2:
                tail += complex(sign(head.real - tail.real), 0)
                tail += complex(0, sign(head.imag - tail.imag))
                visited.add(tail)

print(len(visited))
