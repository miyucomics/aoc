from collections import defaultdict

with open("input.txt", "r") as file:
    lenses = {}
    for step in file.read().strip().split(","):
        if "-" in step:
            lenses.pop(step.split("-")[0], None)
            continue
        label, focal_length = step.split("=")
        lenses[label] = focal_length

boxes = defaultdict(list)
for label, focal_length in lenses.items():
    hash = 0
    for char in label:
        hash = (hash + ord(char)) * 17 % 256
    boxes[hash].append((label, int(focal_length)))

print(sum(
    (box_number + 1) * (i + 1) * focal_length
    for box_number, lenses in boxes.items()
    for i, (_, focal_length) in enumerate(lenses)
))
