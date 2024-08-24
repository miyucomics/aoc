with open("input.txt", "r") as file:
    lines = file.read().splitlines()

answer = 0
for line in lines:
    digits = [char for char in line if char.isdigit()]
    answer += int(digits[0] + digits[-1])

print(answer)
