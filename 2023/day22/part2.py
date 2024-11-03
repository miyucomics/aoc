from collections import defaultdict, deque
from dataclasses import dataclass

@dataclass
class Brick:
    west: int
    north: int
    bottom: int
    east: int
    south: int
    top: int

    def overlaps(self, other):
        return (self.west <= other.east and self.east >= other.west and self.north <= other.south and self.south >= other.north)

with open("input.txt") as file:
    bricks = [Brick(*map(int, line.split(","))) for line in file.read().replace("~", ",").splitlines()]
    bricks.sort(key=lambda brick: brick.bottom)

for i, brick in enumerate(bricks):
    tallest = 1
    for brick_below in bricks[:i]:
        if brick.overlaps(brick_below):
            tallest = max(tallest, brick_below.top + 1)
    brick.top -= brick.bottom - tallest
    brick.bottom = tallest

bricks.sort(key=lambda brick: brick.bottom)

supporting = defaultdict(set)
supporters_of = defaultdict(set)

for i, brick in enumerate(bricks):
    for j, brick_below in enumerate(bricks[:i]):
        if brick.overlaps(brick_below) and brick.bottom == brick_below.top + 1:
            supporting[j].add(i)
            supporters_of[i].add(j)

total = 0

for i in range(len(bricks)):
    queue = deque(supported for supported in supporting[i] if len(supporters_of[supported]) == 1)
    fallen = set(queue)
    fallen.add(i)

    while queue:
        # to fall is going to fall
        # so get what it's supporting that is still standing
        # if all of those are gone, queue it up
        to_fall = queue.popleft()
        for secondary in supporting[to_fall] - fallen:
            if supporters_of[secondary].issubset(fallen):
                queue.append(secondary)
                fallen.add(secondary)

    total += len(fallen) - 1

print(total)
