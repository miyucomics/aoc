import re

with open("input.txt") as file:
    enabled = True
    answer = 0
    for match in re.findall("don't\\(\\)|do\\(\\)|mul\\(\\d+,\\d+\\)", file.read()):
        if match == "do()":
            enabled = True
        elif match == "don't()":
            enabled = False
        elif enabled:
            a, b = match.split(",")
            answer += int(a[4:]) * int(b[:-1])

    print(answer)
