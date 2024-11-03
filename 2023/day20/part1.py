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

# for the button presses, we already know there are 1000 low signals from the button presses
button_presses = 1000
signal_counter = {
    "L": button_presses,
    "H": 0
}

for i in range(button_presses):
    queue = deque(("broadcaster", "L", x) for x in network["broadcaster"])

    while queue:
        source, signal, target = queue.popleft()
        signal_counter[signal] += 1
        if target not in network:
            continue

        # flipflop
        if target[0] == "%":
            if signal == "H":
                continue
            output = "L" if flipflop_mem[target] else "H"
            flipflop_mem[target] = not flipflop_mem[target]

        # conjunction
        elif target[0] == "&":
            output = "H"
            conjunction_mem[target][source] = signal
            if all([value == "H" for value in conjunction_mem[target].values()]):
                output = "L"

        for destination in network[target]:
            queue.append((target, output, destination))

print(signal_counter["L"] * signal_counter["H"])
