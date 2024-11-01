with open("input.txt", "r") as file:
    input_text = file.read().splitlines()

times = [int(time) for time in input_text[0].split(":")[1].split()]
records = [int(record) for record in input_text[1].split(":")[1].split()]
answer = 1

for time, record in zip(times, records):
    answer *= sum(1 for attempt in range(time) if attempt * (time - attempt) > record)

print(answer)
