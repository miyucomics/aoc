import re

pattern = re.compile("\\d+")
with open("input.txt") as file:
    a, b, c, *program = map(int, pattern.findall(file.read()))

def execute(a, b, c):
    pointer = 0
    output = []
    while pointer < len(program):
        opcode = program[pointer]
        operand = program[pointer + 1]
        combos = [0, 1, 2, 3, a, b, c]

        match opcode:
            case 0: a = a >> combos[operand]
            case 1: b = b ^ operand
            case 2: b = combos[operand] % 8
            case 3: pointer = operand - 2 if a else pointer
            case 4: b = b ^ c
            case 5: output.append(combos[operand] % 8)
            case 6: b = a >> combos[operand]
            case 7: c = a >> combos[operand]

        pointer += 2

    return output

def search(a, iteration):
    if execute(a, b, c) == program:
        print(a)
        exit()
    if iteration == 0 or execute(a, b, c) == program[-iteration:]:
        for tack_on in range(8):
            search(a << 3 | tack_on, iteration + 1)

search(0, 0)
