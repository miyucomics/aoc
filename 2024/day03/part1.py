import re

expression = re.compile("mul\\(\\d+,\\d+\\)")

with open("input.txt") as file:
    print(sum(
        int(a[4:]) * int(b[:-1])
        for match in expression.findall("mul\\(\\d+,\\d+\\)", file.read())
        for a, b in [match.split(",")]
    ))
