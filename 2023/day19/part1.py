workflows = {}
queue = []

with open("input.txt", "r") as file:
    raw_workflows, raw_parts = file.read().strip().split("\n\n")

    workflows = {
        name: data[:-1].split(",")
        for raw in raw_workflows.splitlines()
        for name, data in [raw.split("{")]
    }

    queue = [
        ("in", [int(value[2:]) for value in raw_part[1:-1].split(",")])
        for raw_part in raw_parts.splitlines()
    ]

answer = 0

while queue:
    workflow, part = queue.pop()
    if workflow == "R":
        continue

    if workflow == "A":
        answer += sum(part)
        continue

    for procedure in workflows[workflow][:-1]:
        current = part["xmas".index(procedure[0])]
        threshold, target = procedure.split(":")
        threshold = int(threshold[2:])
        if procedure[1] == "<":
            if current < threshold:
                queue.append((target, part))
                break
        else:
            if current > threshold:
                queue.append((target, part))
                break
    else:
        queue.append((workflows[workflow][-1], part))

print(answer)
