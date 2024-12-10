with open("input.txt") as file:
    format = file.read().strip()

cursor = 0
files = []
free_spaces = []

for i, amount in enumerate(format):
    size = int(amount)
    if size == 0:
        continue

    if i % 2 == 0:
        files.append((i // 2, cursor, size))
    else:
        free_spaces.append((cursor, size))

    cursor += size

for i in reversed(range(len(files))):
    id, position, size = files[i]

    for j, (start, length) in enumerate(free_spaces):
        if start >= position:
            free_spaces = free_spaces[:j]
            break

        if size <= length:
            files[i] = (id, start, size)
            if size == length:
                free_spaces.pop(j)
            else:
                free_spaces[j] = (start + size, length - size)
            break

print(sum((position * size + size * (size - 1) // 2) * id for id, position, size in files))
