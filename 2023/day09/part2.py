with open("input.txt", "r") as file:
    strands = [list(map(int, line.split())) for line in file.read().splitlines()]

def recurse(strand):
    offsets = []
    for i, point in enumerate(strand[:-1]):
        offsets.append(strand[i + 1] - point)
    if all(offset == 0 for offset in offsets):
        return strand[-1]
    return strand[-1] + recurse(offsets)

print(sum(recurse(strand[::-1]) for strand in strands))
