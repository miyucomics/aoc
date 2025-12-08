with open("input.txt") as file:
    boxes = [tuple(map(int, line.split(","))) for line in file.readlines()]
    number = len(boxes)

connections = []
for id_a, a in enumerate(boxes):
    for id_b in range(id_a + 1, len(boxes)):
        b = boxes[id_b]
        connections.append(tuple([(a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2, id_a, id_b]))
connections.sort()

parent_lookup = list(range(number))
circuit_sizes = [1] * number
circuit_count = number

def find_parent(x):
    while parent_lookup[x] != x:
        parent_lookup[x] = parent_lookup[parent_lookup[x]]
        x = parent_lookup[x]
    return x

def join(a, b):
    global circuit_count
    a = find_parent(a)
    b = find_parent(b)
    if a == b:
        return False
    if circuit_sizes[a] < circuit_sizes[b]:
        a, b = b, a
    parent_lookup[b] = a
    circuit_sizes[a] += circuit_sizes[b]
    circuit_count -= 1
    return True

for _, i, j in connections:
    join(i, j)
    if circuit_count == 1:
        print(boxes[i][0] * boxes[j][0])
        break
