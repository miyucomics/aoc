from collections import defaultdict

graph = defaultdict(set)
with open("input.txt") as file:
    for line in file.read().splitlines():
        a, b = line.split("-")
        graph[a].add(b)
        graph[b].add(a)

passwords = set()
def search(vertex, seen):
    password = tuple(sorted(seen))
    if password in passwords:
        return
    passwords.add(password)

    for neighbour in graph[vertex]:
        if neighbour in seen:
            continue
        if not seen <= graph[neighbour]:
            continue
        search(neighbour, seen | {neighbour})

for vertex in graph:
    search(vertex, {vertex})

print(",".join(max(passwords, key=len)))
