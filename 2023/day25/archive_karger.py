from collections import defaultdict
from copy import deepcopy
from random import shuffle

edges = []
with open("input.txt", "r") as file:
    edges = [
        [source, target]
        for line in file.read().splitlines()
        for source, targets in [line.split(": ")]
        for target in targets.split()
    ]

def karger(edges, edges_map, sizes):
    shuffle(edges)
    while len(edges_map) > 2:
        # choose an edge and contract it
        edge = edges.pop()
        a, b = edge
        if a == b:
            continue

        for edge in edges_map[b]:
            for i in range(2):
                if edge[i] == b:
                    edge[i] = a

            edges_map[a].append(edge)
        del edges_map[b]

        sizes[a] += sizes[b]
        del sizes[b]

        newedges = []
        for edge in edges_map[a]:
            x, y = edge
            if x != y:
                newedges.append(edge)
        edges_map[a] = newedges

while True:
    copied_edges = deepcopy(edges)

    edges_map = defaultdict(list)
    for edge in copied_edges:
        a, b = edge
        edges_map[a].append(edge)
        edges_map[b].append(edge)

    sizes = {vertex: 1 for vertex in edges_map}
    karger(copied_edges, edges_map, sizes)

    keys = list(edges_map)
    if len(edges_map[keys[0]]) <= 3:
        print(sizes[keys[0]] * sizes[keys[1]])
        exit(0)
