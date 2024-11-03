from collections import defaultdict

with open("input.txt", "r") as file:
    lines = file.read().splitlines()

directory = ["/"]
sizes = defaultdict(int)

reading = False
for line in lines:
    if line.startswith("$ cd "):
        reading = False
        argument = line[5:]
        if argument == "..":
            directory.pop()
        elif argument == "/":
            directory = ["/"]
        else:
            directory.append(argument)

    elif line == "$ ls":
        reading = True

    elif reading and not line.startswith("dir"):
        for i in range(len(directory)):
            key = "/".join(directory[:i + 1])
            sizes[key] += int(line.split(" ")[0])

required_space = 30000000 - (70000000 - sizes["/"])
print(min(size for size in sizes.values() if size >= required_space))
