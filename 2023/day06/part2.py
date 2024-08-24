with open("input.txt") as file:
    input_text = file.read().splitlines()

time = int(input_text[0].split(":")[1].replace(" ", ""))
record = int(input_text[1].split(":")[1].replace(" ", ""))

left_bound = None
for attempt in range(time):
    if attempt * (time - attempt) > record:
        left_bound = attempt
        break

right_bound = None
for attempt in reversed(range(time)):
    if attempt * (time - attempt) > record:
        right_bound = attempt
        break

print(right_bound - left_bound + 1)
