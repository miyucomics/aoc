from collections import deque

with open("input.txt") as file:
    walls = set(
        x + y * 1j
        for byte in file.read().splitlines()[:1024]
        for (x, y) in [map(int, byte.split(","))]
    )

def is_wall(location):
    if location.real < 0 or location.real > 70 or location.imag < 0 or location.imag > 70:
        return True
    return location in walls

queue = deque([(0, 0)])
visited = set()

while queue:
    position, steps = queue.popleft()
    if position in visited:
        continue
    visited.add(position)

    if position == 70 + 70j:
        print(steps)
        exit()

    for displacement in [-1, 1, -1j, 1j]:
        new = position + displacement
        if not is_wall(new) and new not in visited:
            queue.append((new, steps + 1))
