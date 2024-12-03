import re

with open("input.txt") as file:
    print(sum(
        int(a[4:]) * int(b[:-1])
        for match in re.findall("mul\\(\\d+,\\d+\\)", file.read())
        for a, b in [match.split(",")]
    ))
