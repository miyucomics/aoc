def hash(num):
    num = num ^ num << 6 & 0xFFFFFF
    num = num ^ num >> 5 & 0xFFFFFF
    num = num ^ num << 11 & 0xFFFFFF
    return num

with open("input.txt") as file:
    answer = 0
    for secret in file.read().splitlines():
        secret = int(secret)
        for _ in range(2000):
            secret = hash(secret)
        answer += secret
    print(answer)
