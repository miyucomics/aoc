with open("input.txt", "r") as file:
    print(max(
        sum(map(int, group.strip().split("\n")))
        for group in file.read().split("\n\n")
    ))
