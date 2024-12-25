with open("input.txt") as file:
    images = file.read().strip().split("\n\n")
    keys = []
    locks = []

    for image in images:
        transposed = list(zip(*image.split("\n")))
        data = [row.count("#") - 1 for row in transposed]
        match image[0]:
            case ".": keys.append(data)
            case "#": locks.append(data)

print(sum(
    all(a + b <= 5 for a, b in zip(lock, key))
    for lock in locks
    for key in keys
))
