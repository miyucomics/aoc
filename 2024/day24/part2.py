from dataclasses import dataclass

@dataclass
class Gate:
    a: str
    b: str
    op: str
    c: str

with open("input.txt") as file:
    state_data, gate_data = file.read().split("\n\n")

    known = {}
    for line in state_data.splitlines():
        wire, state = line.split(": ")
        known[wire] = state == "1"

    gates = []
    algorithm = {}
    for line in gate_data.splitlines():
        a, op, b, _, c = line.split(" ")
        gates.append(Gate(a, b, op, c))
        algorithm[c] = (a, b, op)

fails_i = [gate for gate in gates if gate.c[0] == "z" and gate.c != "z45" and gate.op != "XOR"]
fails_ii = [gate for gate in gates if gate.a[0] not in "xy" and gate.b[0] not in "xy" and gate.c[0] != "z" and gate.op == "XOR"]

def find_z_for_c(c):
    potential = [gate for gate in gates if gate.a == c or gate.b == c]

    for gate in potential:
        if gate.c[0] == "z":
            z_value = int(gate.c[1:]) - 1
            return f"z{z_value:02d}"

    for gate in potential:
        if result := find_z_for_c(gate.c):
            return result

for error in fails_ii:
    connected_error = next(gate for gate in fails_i if gate.c == find_z_for_c(error.c))
    # swap to fix
    connected_error.c, error.c = error.c, connected_error.c

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

x = sum(compute(key) * (2 ** int(key[1:])) for key in known if key[0] == "x")
y = sum(compute(key) * (2 ** int(key[1:])) for key in known if key[0] == "y")
z = sum(compute(key) * (2 ** int(key[1:])) for key in algorithm if key[0] == "z")
expected = x ^ y
faulty_bit = str(bin(expected ^ z)[::-1].find("1")).zfill(2)

erroring_gates = set(gate.c for gate in fails_i + fails_ii)
erroring_gates |= set(
    gate.c
    for gate in gates
    if gate.a.endswith(faulty_bit) and gate.b.endswith(faulty_bit)
)

print(",".join(sorted(erroring_gates)))
