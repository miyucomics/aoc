from collections import defaultdict
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
supporter_count = defaultdict(int)

for i, brick in enumerate(bricks):
    for j, brick_below in enumerate(bricks[:i]):
        if brick.overlaps(brick_below) and brick.bottom == brick_below.top + 1:
            supporting[j].add(i)
            supporter_count[i] += 1

print(sum(
    all(supporter_count[brick] > 1 for brick in supporting[i])
    for i in range(len(bricks))
))
