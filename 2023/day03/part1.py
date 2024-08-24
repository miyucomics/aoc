with open("input.txt", "r") as file:
    input_text = file.read().splitlines()

nongears = set("0123456789.")
schematic_width = len(input_text[0]) - 1
schematic_height = len(input_text) - 1

def get_surrounding_chars(x, y, length):
    left_bound = max(0, x - length)
    right_bound = min(schematic_width, x + 1) + 1
    surroundings = input_text[y][left_bound:right_bound]
    if y - 1 >= 0:
        surroundings += input_text[y - 1][left_bound:right_bound]
    if y + 1 < schematic_height:
        surroundings += input_text[y + 1][left_bound:right_bound]
    return set(surroundings)

answer = 0

for y, line in enumerate(input_text):
    buffer = ""
    for x, char in enumerate(line):
        if char.isdigit():
            buffer += char
            if x == schematic_width or not line[x + 1].isdigit():
                if get_surrounding_chars(x, y, len(buffer)) - nongears:
                    answer += int(buffer)
                buffer = ""

print(answer)
