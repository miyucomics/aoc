with open("input.txt") as file:
    lines = file.readlines()
    transposed = list(map(list, zip(*lines)))

    transposed_problems = []
    buffer = []
    for column in transposed:
        if all(not char.isdigit() for char in column):
            transposed_problems.append(buffer)
            buffer = []
        else:
            buffer.append(column)

answer = 0
for transposed_problem in transposed_problems:
    operands = [int("".join(column[:-1])) for column in transposed_problem]
    if transposed_problem[0][-1] == "+":
        answer += sum(operands)
    else:
        a = 1
        for b in operands:
            a *= b
        answer += a

print(answer)
