with open("input.txt") as file:
    state_data, gate_data = file.read().split("\n\n")

    known = {}
    for line in state_data.splitlines():
        wire, state = line.split(": ")
        known[wire] = state == "1"

    algorithm = {}
    for line in gate_data.splitlines():
        a, op, b, _, c = line.split(" ")
        algorithm[c] = (a, b, op)

ops = {
    "AND": lambda x, y: x & y,
    "OR": lambda x, y: x | y,
    "XOR": lambda x, y: x ^ y
}

def compute(wire):
    if wire in known:
        return known[wire]
    a, b, op = algorithm[wire]
    state = ops[op](compute(a), compute(b))
    known[wire] = state
    return state

print(sum(
    compute(key) * (2 ** int(key[1:]))
    for key in algorithm
    if key[0] == "z"
))
