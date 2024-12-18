from bisect import bisect_left
from collections import deque

with open("input.txt") as file:
    walls = [
        x + y * 1j
        for byte in file.read().splitlines()
        for (x, y) in [map(int, byte.split(","))]
    ]

def is_wall(location, walls):
    if location.real < 0 or location.real > 70 or location.imag < 0 or location.imag > 70:
        return True
    return location in walls

def is_possible(fallen):
    queue = deque([0])
    visited = set()

    while queue:
        position = queue.popleft()
        if position in visited:
            continue
        visited.add(position)

        if position == 70 + 70j:
            return True

        for displacement in [-1, 1, -1j, 1j]:
            new = position + displacement
            if not is_wall(new, walls[:fallen]) and new not in visited:
                queue.append(new)

wall = walls[bisect_left(range(len(walls)), True, key=lambda x: is_possible(x) is None) - 1]
print(int(wall.real), int(wall.imag), sep=",")
