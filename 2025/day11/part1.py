from functools import cache

with open("input.txt") as file:
    graph = {}
    for line in file.readlines():
        name, destinations = line.strip().split(": ")
        graph[name] = destinations.split(" ")

@cache
def count_paths(src, dst):
    if src == dst:
        return 1
    return sum(count_paths(neighbor, dst) for neighbor in graph.get(src, []))

print(count_paths("you", "out"))
