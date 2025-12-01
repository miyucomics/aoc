with open("input.txt") as file:
    lines = file.readlines()

current = 50
answer = 0

for line in lines:
    direction = 1
    if line[0] == "L":
        direction = -1
    number = int(line[1:])
    for i in range(number):
        current = (current + direction) % 100
        if current == 0:
            answer += 1

print(answer)
