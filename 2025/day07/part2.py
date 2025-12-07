from collections import Counter

with open("input.txt") as file:
    lines = file.readlines()

beam_counts = Counter({lines[0].index("S"): 1})
splitter_data = [{i for i, char in enumerate(row) if char == "^"} for row in lines[2::2]]

for i, row in enumerate(splitter_data):
    updated = Counter()
    for column, count in beam_counts.items():
        if column in row:
            updated[column - 1] += count
            updated[column + 1] += count
        else:
            updated[column] += count
    beam_counts = updated

print(sum(beam_counts.values()))
