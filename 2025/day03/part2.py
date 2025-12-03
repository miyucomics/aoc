with open("input.txt") as file:
    lines = file.readlines()

answer = 0
passes = 12

for line in lines:
    number_in_building = 0
    passes_remaining = passes
    buffer = list(map(int, line.strip()))

    for i in range(passes):
        passes_remaining -= 1
        pass_max = buffer[0]
        best_index = 0

        for chosen_pos, chosen_digit in enumerate(buffer):
            if chosen_digit > pass_max and len(buffer[chosen_pos + 1:]) >= passes_remaining:
                best_index = chosen_pos
                pass_max = chosen_digit
        buffer = buffer[best_index + 1:]
        number_in_building = number_in_building * 10 + pass_max

    answer += number_in_building

print(answer)
