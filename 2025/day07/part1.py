with open("input.txt") as file:
    lines = file.readlines()

beam_columns = {lines[0].index("S")}
splitter_data = [{i for i, char in enumerate(row) if char == "^"} for row in lines[2::2]]

splits = 0
for row in splitter_data:
    updated = set()
    for column in beam_columns:
        if column in row:
            updated.add(column - 1)
            updated.add(column + 1)
            splits += 1
        else:
            updated.add(column)
    beam_columns = updated

print(splits)
