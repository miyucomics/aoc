with open("input.txt", "r") as file:
    input_text = file.read().splitlines()

tree = {}

for line in input_text[2:]:
    name, paths = line.split(" = ")
    paths = paths[1:9].split(", ")
    tree[name] = {
        "L": paths[0],
        "R": paths[1]
    }

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def lcm(a, b):
    return a * b // gcd(a, b)

smallest_cycle = 1
instructions = input_text[0]
for start in [key for key in tree if key[2] == "A"]:
    steps = 0
    while start[2] != "Z":
        start = tree[start][instructions[steps % len(instructions)]]
        steps += 1
    smallest_cycle = lcm(smallest_cycle, steps)

print(smallest_cycle)
