register = 1
cycles = 0
display = list(" " * 40 * 6)

def blit():
    y, x = divmod(cycles, 40)
    if abs(x - register) <= 1:
        display[cycles] = "█"

with open("input.txt", "r") as file:
    for line in file.read().splitlines():
        blit()
        if line.startswith("addx"):
            cycles += 1
            blit()
            register += int(line.split(" ")[1])
        cycles += 1

for i in range(6):
    print("".join(display[i * 40:i * 40 + 40]))
