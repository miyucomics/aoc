with open("input.txt") as file:
    queries = file.read().split("\n\n")[-1]

answer = 0
for query in queries.splitlines():
    size, circuits = query.split(": ")
    width, height = size.split("x")
    if int(width) * int(height) // 9 >= sum(map(int, circuits.split())):
        answer += 1

print(answer)
