with open("input.txt") as file:
    boxes = [tuple(map(int, line.split(","))) for line in file.readlines()]

connections = []
for id_a, a in enumerate(boxes):
    for id_b in range(id_a + 1, len(boxes)):
        b = boxes[id_b]
        connections.append(tuple([(a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2, id_a, id_b]))
connections.sort()

working_id = 0
circuit_lookup = {}
circuit_sizes = {}

for distance, id_a, id_b in connections[:1000]:
    a_in = id_a in circuit_lookup
    b_in = id_b in circuit_lookup
    if a_in and b_in:
        id_i = circuit_lookup[id_a]
        id_j = circuit_lookup[id_b]
        if id_i != id_j:
            for box, circuit in circuit_lookup.items():
                if circuit == id_j:
                    circuit_lookup[box] = id_i
            circuit_sizes[id_i] += circuit_sizes[id_j]
            del circuit_sizes[id_j]
    elif a_in:
        circuit = circuit_lookup[id_a]
        circuit_lookup[id_b] = circuit
        circuit_sizes[circuit] += 1
    elif b_in:
        circuit = circuit_lookup[id_b]
        circuit_lookup[id_a] = circuit
        circuit_sizes[circuit] += 1
    else:
        circuit_lookup[id_a] = working_id
        circuit_lookup[id_b] = working_id
        circuit_sizes[working_id] = 2
        working_id += 1

answer = 1
for size in sorted(circuit_sizes.values(), reverse=True)[:3]:
    answer *= size
print(answer)
