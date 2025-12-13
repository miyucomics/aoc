from common_code import find_button_presses

def solve_line(line):
    parts = [segment[1:-1] for segment in line.strip().split(" ")]
    target = sum(2 ** i for i, char in enumerate(parts[0]) if char == "#")
    buttons = [sum(map(lambda x: 2 ** int(x), button.split(","))) for button in parts[1:-1]]
    return next(find_button_presses(target, buttons)).bit_count()

with open("input.txt") as file:
    print(sum(map(solve_line, file.readlines())))
