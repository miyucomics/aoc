with open("input.txt", "r") as file:
    print(sum(
        sorted(
            sum(map(int, group.strip().split("\n")))
            for group in file.read().split("\n\n")
        )[-3:]
    ))
