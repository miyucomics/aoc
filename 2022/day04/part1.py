with open("input.txt", "r") as file:
    lines = file.read().splitlines()

answer = 0
for line in lines:
    first, second = line.split(",")
    first = tuple(map(int, first.split("-")))
    second = tuple(map(int, second.split("-")))

    if first[0] <= second[0] and first[1] >= second[1]:
        answer += 1
    elif second[0] <= first[0] and second[1] >= first[1]:
        answer += 1

print(answer)
