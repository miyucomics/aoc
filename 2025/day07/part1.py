with open("input.txt") as file:
    raw = file.readlines()
    beam_columns = set()
    beam_columns.add(raw[0].find("S"))
    splitter_data = [set(i for i, char in enumerate(line.strip()) if char == "^") for line in raw[2::2]]

splits = 0
for row in splitter_data:
    new_beam_columns = set()
    for beam in beam_columns:
        if beam in row:
            new_beam_columns.add(beam - 1)
            new_beam_columns.add(beam + 1)
            splits += 1
        else:
            new_beam_columns.add(beam)
    beam_columns = new_beam_columns

print(splits)
