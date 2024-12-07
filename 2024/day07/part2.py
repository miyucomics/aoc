def possible(target, elements, accumulator, index):
    if accumulator > target:
        return False

    if index == len(elements):
        return target == accumulator

    if possible(target, elements, accumulator + elements[index], index + 1):
        return True

    if possible(target, elements, accumulator * elements[index], index + 1):
        return True

    if possible(target, elements, int(str(accumulator) + str(elements[index])), index + 1):
        return True

    return False

with open("input.txt") as file:
    answer = 0
    for line in file.read().splitlines():
        target, elements = line.split(": ")
        target = int(target)
        elements = list(map(int, elements.split(" ")))
        answer += target * possible(target, elements, elements[0], 1)
    print(answer)
