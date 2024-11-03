from collections import defaultdict, deque

with open("input.txt", "r") as file:
    network = {
        source: destination.split(", ")
        for line in file.read().splitlines()
        for source, destination in [line.split(" -> ")]
    }

# label the module outputs with their type
# and collect lookup for what modules are inputs for conjunctions
conjunction_inputs = defaultdict(list)
for module, outputs in network.items():
    network[module] = []
    for output in outputs:
        if "&" + output in network:
            conjunction_inputs["&" + output].append(module)
            network[module].append("&" + output)
            continue
        network[module].append("%" + output)

flipflop_mem = {
    key: False
    for key in network if key[0] == "%"
}
conjunction_mem = {
    conjunction: {
        source: "L"
        for source in conjunction_inputs[conjunction]
    }
    for conjunction in network
    if conjunction[0] == "&"
}

for module, outputs in network.items():
    if "%rx" in outputs:
        gateway = module
        break
cycle_complete = {name: False for name, exports in network.items() if gateway in exports}
cycle_lengths = {}

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def lcm(a, b):
    return a * b // gcd(a, b)

presses = 0
while True:
    presses += 1
    queue = deque(("broadcaster", "L", x) for x in network["broadcaster"])

    while queue:
        source, signal, target = queue.popleft()
        if target not in network:
            continue

        if target == gateway and signal == "H":
            cycle_complete[source] = True
            if source not in cycle_lengths:
                cycle_lengths[source] = presses

            if all(cycle_complete.values()):
                smallest_cycle = 1
                for cycle_length in cycle_lengths.values():
                    smallest_cycle = lcm(smallest_cycle, cycle_length)
                print(smallest_cycle)
                exit()

        # flipflop
        if target[0] == "%":
            if signal == "H":
                continue
            output = "L" if flipflop_mem[target] else "H"
            flipflop_mem[target] = not flipflop_mem[target]

        # conjunction
        elif target[0] == "&":
            conjunction_mem[target][source] = signal
            output = "H"
            if all([value == "H" for value in conjunction_mem[target].values()]):
                output = "L"

        for destination in network[target]:
            queue.append((target, output, destination))
