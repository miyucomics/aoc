def row(grid):
    binary = [int(row, 2) for row in grid]
    for y in range(1, len(grid)):
        # use binary to count differences
        # sum them up and make sure there's only 1
        if sum(bin(up ^ down).count("1") for up, down in zip(binary[:y], binary[y:])) == 1:
            return y
    return 0

with open("input.txt", "r") as file:
    answer = 0
    for puzzle in file.read().replace("#", "1").replace(".", "0").split("\n\n"):
        puzzle = puzzle.splitlines()
        answer += row(puzzle) * 100
        puzzle = ["".join(row) for row in list(zip(*puzzle))]  # transpose grid
        answer += row(puzzle)
    print(answer)
