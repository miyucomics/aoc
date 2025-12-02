with open("input.txt") as file:
    raw = file.read().strip()

answer = 0
ranges = [
    tuple(map(int, line.split("-")))
    for line in raw.split(",")
]

max_endpoint = max(max(ran) for ran in ranges)
longest_base_length = int(len(str(max_endpoint)) // 2)
for length in range(1, longest_base_length + 1):
    for x in range(10 ** (length - 1), 10 ** length):
        i = int(str(x) + str(x))
        if any(ran[0] <= i <= ran[1] for ran in ranges):
            answer += i

print(answer)
