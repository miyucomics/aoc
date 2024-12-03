# a different approach, assume that it's in descending order, reverse will catch other case
def is_safe(data, tolerate_error):
    for i in range(len(data) - 1):
        if not 1 <= data[i] - data[i + 1] <= 3:
            return tolerate_error and (
                # no more error tolerance from here
                is_safe(data[i - 1:i] + data[i + 1:], False) or  # remove current value
                is_safe(data[i:i + 1] + data[i + 2:], False)     # remove next value
            )
    return True

with open("input.txt", "r") as file:
    answer = 0
    for line in file.read().splitlines():
        line = list(map(int, line.split(" ")))
        answer += is_safe(line, True) or is_safe(line[::-1], True)
    print(answer)
