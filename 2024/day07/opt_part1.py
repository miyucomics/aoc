def possible(target, elements):
    if len(elements) == 0:
        return target == 0

    focus = elements[-1]

    if target > focus and possible(target - focus, elements[:-1]):
        return True

    if target % focus == 0 and possible(target / focus, elements[:-1]):
        return True

    return False

with open("input.txt") as file:
    answer = 0
    for line in file.read().splitlines():
        target, elements = line.split(": ")
        target = int(target)
        elements = list(map(int, elements.split(" ")))
        answer += target * possible(target, elements)
    print(answer)
