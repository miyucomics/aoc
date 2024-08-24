with open("input.txt") as file:
    seeds, *mappings = file.read().strip().split("\n\n")

seeds = [int(seed) for seed in seeds.split(": ")[1].split()]

for mapping in mappings:
    ranges = [list(map(int, group.split())) for group in mapping.split("\n")[1:]]
    mapped = []
    for seed in seeds:
        for destination, source, length in ranges:
            if source <= seed < source + length:
                mapped.append(seed - source + destination)
                break
        else:
            mapped.append(seed)
    seeds = mapped

print(min(seeds))
