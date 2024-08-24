with open("input.txt", "r") as file:
    lines = file.read().splitlines()

answer = 0
for line in lines:
    digits = []
    for i, char in enumerate(line):
        if char.isdigit():
            digits.append(char)
            continue
        for value, name in enumerate(["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]):
            if line[i:].startswith(name):
                digits.append(str(value + 1))
                break
    answer += int(digits[0] + digits[-1])

print(answer)
