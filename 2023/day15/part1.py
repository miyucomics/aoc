with open("input.txt", "r") as file:
    answer = 0
    for step in file.read().strip().split(","):
        value = 0
        for char in step:
            value += ord(char)
            value *= 17
            value = value % 256
        answer += value
    print(answer)
