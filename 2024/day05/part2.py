from collections import defaultdict

with open("input.txt") as file:
    raw_rules, raw_updates = file.read().split("\n\n")

    rules = defaultdict(set)
    for line in raw_rules.splitlines():
        a, b = tuple(map(int, line.split("|")))
        rules[a].add(b)

    updates = [{
        number: index
        for index, number in enumerate(map(int, line.split(",")))
    } for line in raw_updates.splitlines()]

def is_valid(update):
    for i, number in enumerate(update):
        for after in rules[number]:
            if after not in update.keys():
                continue
            if i > update[after]:
                return False
    return True

def get_middle_element(update):
    target_count = len(update.keys()) // 2
    for number in update:
        if len(set(update.keys()) & rules[number]) == target_count:
            return number

print(sum(
    get_middle_element(update)
    for update in updates
    if not is_valid(update)
))
