from collections import defaultdict

graph = defaultdict(set)
with open("input.txt") as file:
    for line in file.read().splitlines():
        a, b = line.split("-")
        graph[a].add(b)
        graph[b].add(a)

print(sum(
    a != c and a in graph[c] and any(name.startswith("t") for name in [a, b, c])
    for a in graph
    for b in graph[a]
    for c in graph[b]
) // 6)
