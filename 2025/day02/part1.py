with open("input.txt") as file:
    raw = file.read().strip()

answer = 0
ranges = raw.split(",")
for ran in ranges:
    a, b = ran.split("-")
    for i in range(int(a), int(b) + 1):
        string = str(i)
        if len(string) % 2 == 1:
            continue
        if string[0:len(string) // 2] == string[len(string) // 2:]:
            answer += i

print(answer)
