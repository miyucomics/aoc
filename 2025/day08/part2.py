with open("input.txt") as file:
    positions = [tuple(map(int, line.split(","))) for line in file.readlines()]
    all_boxes = set(range(len(positions)))

squared_distances = {}
for i, a in enumerate(positions):
    for j in range(i + 1, len(positions)):
        b = positions[j]
        squared_distances[(i, j)] = (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2

pairs = list(squared_distances.keys())
pairs.sort(key=lambda x: squared_distances[x])

circuit_id = 0
circuit_association = {}
circuit_sizes = {}
seen_boxes = set()

for i, j in pairs:
    seen_boxes.add(i)
    seen_boxes.add(j)

    ai = i in circuit_association
    bi = j in circuit_association
    if ai and bi:
        c1 = circuit_association[i]
        c2 = circuit_association[j]
        if c1 != c2:
            for box, circuit in circuit_association.items():
                if circuit == c2:
                    circuit_association[box] = c1
            circuit_sizes[c1] += circuit_sizes[c2]
            del circuit_sizes[c2]
    elif ai:
        circuit = circuit_association[i]
        circuit_association[j] = circuit
        circuit_sizes[circuit] += 1
    elif bi:
        circuit = circuit_association[j]
        circuit_association[i] = circuit
        circuit_sizes[circuit] += 1
    else:
        circuit_association[i] = circuit_id
        circuit_association[j] = circuit_id
        circuit_sizes[circuit_id] = 2
        circuit_id += 1

    if seen_boxes == all_boxes and len(circuit_sizes) == 1:
        print(positions[i][0] * positions[j][0])
        break
