with open("input.txt") as file:
    lines = file.readlines()
    matrix = [
        [token.strip() for token in line.split(" ") if token]
        for line in lines
    ]
    transposed = list(map(list, zip(*matrix)))

answer = 0
for problem in transposed:
    operands = [int(number) for number in problem[:-1]]
    if problem[-1] == "+":
        answer += sum(operands)
    else:
        a = 1
        for b in operands:
            a *= b
        answer += a

print(answer)
