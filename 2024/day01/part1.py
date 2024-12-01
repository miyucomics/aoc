left = []
right = []

with open("input.txt", "r") as file:
    for line in file.read().splitlines():
        a, b = line.split("   ")
        left.append(int(a))
        right.append(int(b))

left.sort()
right.sort()

print(sum(abs(a - b) for a, b in zip(left, right)))
