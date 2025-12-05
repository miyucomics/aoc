with open("input.txt") as file:
    ranges_raw, _ = file.read().split("\n\n")

ranges = []
for part in ranges_raw.split("\n"):
    a, b = part.split("-")
    ranges.append((int(a), int(b)))

ranges.sort()

merged = [ranges[0]]
for interval in ranges[1:]:
    if interval[0] > merged[-1][1] + 1:
        merged.append(interval)
    else:
        a, b = merged[-1]
        merged[-1] = (a, max(b, interval[1]))

print(sum(
    interval[1] - interval[0] + 1
    for interval in merged
))
