with open("input.txt") as file:
    ranges = []
    for part in file.read().split(","):
        a, b = part.split("-")
        ranges.append((int(a), int(b)))
    upper_bound = max(r[1] for r in ranges)

def in_range(x):
    for lo, hi in ranges:
        if lo <= x <= hi:
            return True
    return False

results = set()
for number_of_repeated_digits in range(1, int(len(str(upper_bound)) // 2) + 1):
    for pattern in range(10 ** (number_of_repeated_digits - 1), 10 ** number_of_repeated_digits):
        repetitions = 2
        while True:
            magic = sum(10 ** (i * number_of_repeated_digits) for i in range(repetitions))
            n = pattern * magic
            if n > upper_bound:
                break
            results.add(n)
            repetitions += 1

print(sum(result for result in results if in_range(result)))
