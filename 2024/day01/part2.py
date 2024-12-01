left = []
right = []

with open("input.txt", "r") as file:
    for line in file.read().splitlines():
        a, b = line.split("   ")
        left.append(int(a))
        right.append(int(b))

print(sum(id * right.count(id) for id in left))
