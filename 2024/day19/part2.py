with open("input.txt") as file:
    lines = file.read().splitlines()
    patterns = set(lines[0].split(", "))
    max_length = max(len(pattern) for pattern in patterns)
    desired = lines[2:]

cache = {"": 1}

def count_ways(design):
    if design in cache:
        return cache[design]

    count = sum(
        count_ways(design[i:])
        for i in range(min(len(design), max_length) + 1)
        if design[:i] in patterns
    )

    cache[design] = count
    return count

print(sum(count_ways(design) for design in desired))
