from collections import defaultdict

with open("input.txt") as file:
    raw_rules, raw_updates = file.read().split("\n\n")

    rules = defaultdict(set)
    for line in raw_rules.splitlines():
        a, b = tuple(map(int, line.split("|")))
        rules[a].add(b)

    updates = [
        list(map(int, line.split(",")))
        for line in raw_updates.splitlines()
    ]

def is_valid(update):
    positions = {
        number: index
        for index, number in enumerate(update)
    }
    for i, number in enumerate(update):
        for after in rules[number]:
            if after not in positions.keys():
                continue
            if i > positions[after]:
                return False
    return True


print(sum(
    update[len(update) // 2]
    for update in updates
    if is_valid(update)
))
