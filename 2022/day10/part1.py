x = 1
cycles = 0
answer = 0

watched = [220, 180, 140, 100, 60, 20]

with open("input.txt", "r") as file:
    for line in file.read().splitlines():
        cycles += 1
        if line.startswith("addx"):
            cycles += 1
            if cycles >= watched[-1]:
                answer += x * watched[-1]
                watched.pop()
            if len(watched) == 0:
                print(answer)
                quit()
            x += int(line.split(" ")[1])
