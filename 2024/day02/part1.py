def isSafe(row):
    signs = []
    for i in range(len(row) - 1):
        difference = row[i + 1] - row[i]
        if abs(difference) > 3 or difference == 0:
            return False
        signs.append(difference > 0)
    return all(signs) or not any(signs)

with open("input.txt", "r") as file:
    print(sum(isSafe(list(map(int, line.split(" ")))) for line in file.read().splitlines()))
