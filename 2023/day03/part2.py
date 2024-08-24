with open("input.txt", "r") as file:
    input_text = file.read().splitlines()

gears = {}
schematic_width = len(input_text[0]) - 1
schematic_height = len(input_text) - 1

for y, line in enumerate(input_text):
    buffer = ""
    for x, char in enumerate(line):
        if char.isdigit():
            buffer += char
            if x == schematic_width or not line[x + 1].isdigit():
                left_bound = max(0, x - len(buffer))
                right_bound = min(schematic_width, x + 1)
                for dx in range(left_bound, right_bound + 1):
                    for dy in range(max(0, y - 1), min(y + 1, schematic_height) + 1):
                        if input_text[dy][dx] == "*":
                            gears.setdefault(dy * schematic_width + dx, []).append(int(buffer))
                buffer = ""

print(sum([gear[0] * gear[1] for gear in gears.values() if len(gear) == 2]))
