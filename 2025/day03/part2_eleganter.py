with open("input.txt") as file:
    lines = file.readlines()

answer = 0
digits = 12

for line in lines:
    buffer = list(map(int, line.strip()))
    to_remove = len(buffer) - digits
    stack = []

    for digit in buffer:
        while stack and stack[-1] < digit and to_remove > 0:
            stack.pop()
            to_remove -= 1
        stack.append(digit)

    answer += sum(digit * 10 ** (digits - i - 1) for i, digit in enumerate(stack[:digits]))

print(answer)
