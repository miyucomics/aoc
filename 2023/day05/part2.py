with open("input.txt", "r") as file:
    seeds, *mappings = file.read().strip().split("\n\n")

seeds = [int(seed) for seed in seeds.split(": ")[1].split()]
seed_ranges = [(seeds[i * 2], seeds[i * 2] + seeds[i * 2 + 1]) for i in range(len(seeds) // 2)]

for mapping in mappings:
    ranges = [list(map(int, group.split())) for group in mapping.split("\n")[1:]]
    mapped = []
    for start, end in seed_ranges:
        for destination, source, length in ranges:
            overlap_start = max(start, source)
            overlap_end = min(end, source + length)
            if overlap_start < overlap_end:
                mapped.append((overlap_start - source + destination,
                               overlap_end - source + destination))
                if overlap_start > start:
                    seed_ranges.append((start, overlap_start))
                if end > overlap_end:
                    seed_ranges.append((overlap_end, end))
                break
        else:
            mapped.append((start, end))
    seed_ranges = mapped

print(min(seed_ranges)[0])
