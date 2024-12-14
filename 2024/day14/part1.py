import re

numbers = re.compile("-?\\d+")
with open("input.txt") as file:
    quadrantI = 0
    quadrantII = 0
    quadrantIII = 0
    quadrantIV = 0
    for line in file.read().splitlines():
        px, py, vx, vy = map(int, numbers.findall(line))
        x = (px + 100 * vx) % 101
        y = (py + 100 * vy) % 103
        if x > 50 and y > 51:
            quadrantI += 1
        if x < 50 and y > 51:
            quadrantII += 1
        if x < 50 and y < 51:
            quadrantIII += 1
        if x > 50 and y < 51:
            quadrantIV += 1
    print(quadrantI * quadrantII * quadrantIII * quadrantIV)
