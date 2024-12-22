from collections import Counter

number_pad = {char: divmod(i, 3) for i, char in enumerate("789456123X0A")}
arrow_pad = {char: divmod(i, 3) for i, char in enumerate("X^A<v>")}

def count_ways(keypad, code, to_reach_here):
    current_y, current_x = keypad["A"]
    avoid_y, avoid_x = keypad["X"]

    counts = Counter()
    for char in code:
        target_y, target_x = keypad[char]
        counts[(
            target_x - current_x,
            target_y - current_y,
            target_x == avoid_x and current_y == avoid_y or target_y == avoid_y and current_x == avoid_x
        )] += to_reach_here
        current_x, current_y = target_x, target_y

    return counts

with open("input.txt") as file:
    answer = 0

    for code in file.read().splitlines():
        counts = count_ways(number_pad, code, 1)

        for _ in range(3):
            new_counts = Counter()
            for x, y, reverse in counts:
                movement = "<" * -x + "v" * y + "^" * -y + ">" * x
                if reverse:
                    movement = movement[::-1]
                count = counts[(x, y, reverse)]
                new_counts += count_ways(arrow_pad, movement + "A", count)
            counts = new_counts

        answer += counts.total() * int(code[:-1])

    print(answer)
