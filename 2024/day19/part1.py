with open("input.txt") as file:
    lines = file.read().splitlines()
    patterns = set(lines[0].split(", "))
    max_length = max(len(pattern) for pattern in patterns)
    desired = lines[2:]

cache = {"": True}

def is_possible(design):
    if design in cache:
        return cache[design]

    for i in range(min(len(design), max_length) + 1):
        if design[:i] in patterns and is_possible(design[i:]):
            cache[design] = True
            return True

    cache[design] = False
    return False


print(sum(is_possible(design) for design in desired))
