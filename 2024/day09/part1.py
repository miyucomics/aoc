with open("input.txt") as file:
    format = file.read().strip()

disk = []
for i, amount in enumerate(format):
    if i % 2 == 0:
        disk.extend([i // 2] * int(amount))
    else:
        disk.extend([None] * int(amount))

rising_pointer = 0
falling_pointer = len(disk) - 1

answer = 0
while falling_pointer > rising_pointer:
    while disk[falling_pointer] is None:
        falling_pointer -= 1

    while disk[rising_pointer] is not None:
        answer += rising_pointer * disk[rising_pointer]
        rising_pointer += 1

    if falling_pointer <= rising_pointer:
        print(answer)
        exit()

    disk[rising_pointer] = disk[falling_pointer]
    answer += rising_pointer * disk[rising_pointer]
    disk[falling_pointer] = None

    falling_pointer -= 1
    rising_pointer += 1
