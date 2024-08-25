with open("input.txt", "r") as file:
    raw = file.read()

state, instructions = raw.split("\n\n")

stacks = [[] for _ in range(9)]
for row in state.splitlines()[:-1][::-1]:
    for stack in range(1, 36, 4):
        if row[stack] != " ":
            stacks[stack // 4].append(row[stack])

for instruction in instructions.splitlines():
    _, number, _, source, _, destination = instruction.split(" ")
    source = int(source) - 1
    destination = int(destination) - 1
    for _ in range(int(number)):
        stacks[destination].append(stacks[source].pop())

print("".join(stack[-1] for stack in stacks if stack))
