def gosper_hack(x):
    smallest = x & -x
    ripple = x + smallest
    new_smallest = ripple & -ripple
    ones = ((new_smallest // smallest) >> 1) - 1
    return ripple | ones

def compute_state(mask, buttons):
    result = 0
    m = mask
    i = 0
    while m:
        if m & 1:
            result ^= buttons[i]
        m >>= 1
        i += 1
    return result

def solve_line(line):
    parts = [segment[1:-1] for segment in line.strip().split(" ")]
    target = sum(2 ** i for i, char in enumerate(parts[0]) if char == "#")
    buttons = [sum(map(lambda x: 2 ** int(x), button.split(","))) for button in parts[1:-1]]

    n = len(buttons)
    for bit_count in range(1, n + 1):
        mask = (1 << bit_count) - 1
        while mask < (1 << n):
            if compute_state(mask, buttons) == target:
                return bit_count
            mask = gosper_hack(mask)

with open("input.txt") as file:
    print(sum(map(solve_line, file.readlines())))
