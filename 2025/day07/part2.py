from collections import defaultdict

with open("input.txt") as file:
    raw = file.readlines()
    beam_counter = defaultdict(int)
    beam_counter[raw[0].find("S")] = 1
    splitter_data = [set(i for i, char in enumerate(line.strip()) if char == "^") for line in raw[2::2]]

for i, row in enumerate(splitter_data):
    new_beam_counter = defaultdict(int)
    for column, count in beam_counter.items():
        if column in row:
            new_beam_counter[column - 1] += count
            new_beam_counter[column + 1] += count
        else:
            new_beam_counter[column] += count
    beam_counter = new_beam_counter

print(sum(beam_counter[i] for i in beam_counter.keys()))
