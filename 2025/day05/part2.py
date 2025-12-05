with open("input.txt") as file:
    ranges_raw, _ = file.read().split("\n\n")

ranges = []
for part in ranges_raw.split("\n"):
    a, b = part.split("-")
    ranges.append((int(a), int(b)))

ranges.sort()

merged = []
for interval in ranges:
    if len(merged) == 0 or interval[0] > merged[-1][1] + 1:
        merged.append(interval)
    else:
        original = merged[-1]
        merged[-1] = (merged[-1][0], max(merged[-1][1], interval[1]))

print(sum(
    interval[1] - interval[0] + 1
    for interval in merged
))
