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

answer = 0
current = "AAA"
instructions = input_text[0]
while current != "ZZZ":
    current = tree[current][instructions[answer % len(instructions)]]
    answer += 1

print(answer)
