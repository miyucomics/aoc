def count(row):
    return sum(index + 1 for index, char in enumerate(row[::-1]) if char == "O")

with open("input.txt", "r") as file:
    world = file.read().splitlines()
    world = list(map("".join, zip(*world)))  # transpose columns into rows
    # split by #, sort so all the O's move before the .'s, reattach by #'s
    # then pass into count function, which adds up locations where there are O's
    print(sum(count("#".join(["".join(sorted(text, reverse=True)) for text in row.split("#")])) for row in world))
