with open("input.txt") as file:
    ranges_raw, ingredients = file.read().split("\n\n")

ranges = []
for part in ranges_raw.split("\n"):
    a, b = part.split("-")
    ranges.append((int(a), int(b)))

ingredients = list(map(int, ingredients.strip().split("\n")))

def in_range(x):
    for lo, hi in ranges:
        if lo <= x <= hi:
            return True
    return False

print(sum(in_range(ingredient) for ingredient in ingredients))
