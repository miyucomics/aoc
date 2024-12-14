import re

numbers = re.compile("-?\\d+")
with open("input.txt") as file:
    robots = [
        tuple(map(int, numbers.findall(line)))
        for line in file.read().splitlines()
    ]

def half_mad(data):
    mean = sum(data) / len(data)
    return sum(abs(i - mean) for i in data)

x = min(range(101), key=lambda i: half_mad([(px + i * vx) % 101 for px, _, vx, _ in robots]))
y = min(range(103), key=lambda i: half_mad([(py + i * vy) % 103 for _, py, _, vy in robots]))

# 51 is mod inverse of 101 and 103
print(101 * (51 * (y - x) % 103) + x)
