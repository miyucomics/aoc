with open("input.txt") as file:
    raw = file.read().strip()

def get_divisors(n):
    return [i for i in range(1, n) if n % i == 0]

def is_string_invalid(string):
    total = len(string)
    for divisor in get_divisors(total):
        substrings = [
            string[i:i + divisor]
            for i in range(0, total, divisor)
        ]
        if len(set(substrings)) == 1:
            return True
    return False

answer = 0
ranges = raw.split(",")
for ran in ranges:
    a, b = ran.split("-")
    for i in range(int(a), int(b) + 1):
        string = str(i)
        if is_string_invalid(string):
            answer += i

print(answer)
