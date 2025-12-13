from collections import Counter, defaultdict
from common_code import bits_to_indices, compute_state, select
from functools import cache

def solve_line(line):
    parts = [segment[1:-1] for segment in line.strip().split(" ")]
    joltages = tuple(map(int, parts[-1].split(",")))
    light_count = len(joltages)

    buttons = tuple(sum(map(lambda x: 2 ** int(x), button.split(","))) for button in parts[1:-1])
    solutions_cache = defaultdict(set)
    for i in range(0, 2 ** len(buttons)):
        final_state = compute_state(i, buttons)
        cost = Counter()
        for button in select(buttons, i):
            for light in bits_to_indices(button):
                cost[light] += 1
        joltage_drops = tuple(cost[index] for index in range(light_count))
        solutions_cache[final_state].add((i.bit_count(), joltage_drops))

    @cache
    def count_moves(goal):
        if all(joltage == 0 for joltage in goal):
            return 0

        answer = float("inf")
        for button_presses, joltage_drops in solutions_cache[sum(2 ** i for i, joltage in enumerate(goal) if joltage % 2 == 1)]:
            if any(drop > joltage for drop, joltage in zip(joltage_drops, goal)):
                continue
            answer = min(answer, button_presses + 2 * count_moves(tuple((joltage - drop) // 2 for drop, joltage in zip(joltage_drops, goal))))
        return answer

    return count_moves(joltages)

with open("input.txt") as file:
    print(sum(map(solve_line, file.readlines())))
