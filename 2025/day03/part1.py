with open("input.txt") as file:
    lines = file.readlines()

answer = 0
for line in lines:
    buffer = list(map(int, line.strip()))

    slice_position = 0
    best_first_digit = buffer[0]
    for i, num in enumerate(buffer):
        if num > best_first_digit and i != len(buffer) - 1:
            slice_position = i
            best_first_digit = num

    answer += 10 * best_first_digit + max(buffer[slice_position + 1:])

print(answer)
