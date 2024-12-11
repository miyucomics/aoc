from collections import defaultdict

counts = defaultdict(int)
with open("input.txt") as file:
    for i in map(int, file.read().split(" ")):
        counts[i] += 1

for i in range(25):
    new_counts = defaultdict(int)
    for engraving, count in counts.items():
        if engraving == 0:
            new_counts[1] += count
            continue

        text = str(engraving)
        if len(text) % 2 == 0:
            new_counts[int(text[:len(text) // 2])] += count
            new_counts[int(text[len(text) // 2:])] += count
            continue

        new_counts[engraving * 2024] += count

    counts = new_counts

print(sum(counts.values()))
