with open("input.txt") as file:
    points = []
    for line in file.readlines():
        a, b = line.split(",")
        points.append(int(a) + int(b) * 1j)

answer = 0
for i, a in enumerate(points):
    for j in range(i + 1, len(points)):
        b = points[j]
        offset = a - b
        answer = max(answer, abs((offset.real + 1) * (offset.imag + 1)))

print(int(answer))
