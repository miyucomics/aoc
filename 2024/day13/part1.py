import re

def calculate(parameters):
    ax, ay, bx, by, target_x, target_y = parameters
    a_coefficient = (target_x * by - target_y * bx) / (ax * by - ay * bx)
    b_coefficient = (target_x - ax * a_coefficient) / bx
    if a_coefficient <= 100 and b_coefficient <= 100 and a_coefficient % 1 == 0 and b_coefficient % 1 == 0:
        return a_coefficient * 3 + b_coefficient
    return 0

numbers = re.compile("\\d+")
with open("input.txt") as file:
    print(int(sum(
        calculate(map(int, numbers.findall(machine)))
        for machine in file.read().split("\n\n")
    )))
