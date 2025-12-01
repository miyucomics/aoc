with open("input.txt") as file:
    lines = file.readlines()

current = 50
answer = 0

for line in lines:
    direction = 1
    if line[0] == "L":
        direction = -1

    if current == 0:
        required = 100
    elif direction == 1:
        required = 100 - current
    else:
        required = current

    distance = int(line[1:])
    if distance >= required:
        answer += 1 + (distance - required) // 100

    current = (current + direction * distance) % 100

print(answer)
