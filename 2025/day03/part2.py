with open("input.txt") as file:
    lines = file.readlines()

answer = 0
digits = 12

for line in lines:
    constructed_number = 0
    digits_left = digits
    buffer = list(map(int, line.strip()))

    for i in range(digits):
        digits_left -= 1
        pass_max = buffer[0]
        best_index = 0

        end = len(buffer) - digits_left
        for chosen_pos, chosen_digit in enumerate(buffer[:end]):
            if chosen_digit > pass_max:
                best_index = chosen_pos
                pass_max = chosen_digit

        buffer = buffer[best_index + 1:]
        constructed_number = constructed_number * 10 + pass_max

    answer += constructed_number

print(answer)
