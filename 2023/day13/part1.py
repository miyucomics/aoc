def row(grid):
    for y in range(1, len(grid)):
        if all(up == down for up, down in zip(grid[:y][::-1], grid[y:])):
            return y
    return 0

with open("input.txt", "r") as file:
    answer = 0
    for puzzle in file.read().split("\n\n"):
        puzzle = puzzle.splitlines()
        answer += row(puzzle) * 100
        puzzle = list(zip(*puzzle))  # transpose grid
        answer += row(puzzle)
    print(answer)
