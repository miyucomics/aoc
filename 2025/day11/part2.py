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

dac_to_fft = count_paths("dac", "fft")
if dac_to_fft != 0:
    print(count_paths("svr", "dac") * dac_to_fft * count_paths("fft", "out"))
    exit()

print(count_paths("svr", "fft") * count_paths("fft", "dac") * count_paths("dac", "out"))
