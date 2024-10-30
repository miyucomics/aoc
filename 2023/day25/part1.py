from collections import defaultdict

graph = defaultdict(set)
with open("input.txt") as file:
    for line in file.read().splitlines():
        origin, *destinations = line.replace(":", "").split()
        for destination in destinations:
            graph[origin].add(destination)
            graph[destination].add(origin)

partite = set(graph)
graph_size = len(partite)

def strangeness(vertex):
    return len(graph[vertex] - partite)

while sum(map(strangeness, partite)) != 3:
    partite.remove(max(partite, key=strangeness))

print(len(partite) * (graph_size - len(partite)))
