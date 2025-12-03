with open("input.txt") as file:
    lines = file.readlines()

answer = 0
for line in lines:
    buffer = list(map(int, line.strip()))

    first_pass_max = buffer[0]
    first_pass_index = 0
    for i, num in enumerate(buffer):
        if num > first_pass_max and i != len(buffer) - 1:
            first_pass_index = i
            first_pass_max = num

    second_pass_max = float("-inf")
    for i, num in enumerate(buffer[first_pass_index + 1:]):
        if num > second_pass_max:
            second_pass_max = num

    answer += 10 * first_pass_max + second_pass_max

print(answer)
