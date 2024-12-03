def is_safe(row):
    signs = []
    for i in range(len(row) - 1):
        difference = row[i + 1] - row[i]
        if abs(difference) > 3 or difference == 0:
            return False
        signs.append(difference > 0)
    return all(signs) or not any(signs)

def lenient_check(row):
    return any(
        is_safe(row[:i] + row[i + 1:])
        for i in range(len(row))
    )

with open("input.txt", "r") as file:
    print(sum(
        lenient_check(list(map(int, line.split(" "))))
        for line in file.read().splitlines()
    ))
