from collections import defaultdict

def hash(num):
    num = num ^ num << 6 & 0xFFFFFF
    num = num ^ num >> 5 & 0xFFFFFF
    num = num ^ num << 11 & 0xFFFFFF
    return num

with open("input.txt") as file:
    trend_value = defaultdict(int)

    for secret in file.read().splitlines():
        secret = int(secret)
        sliding_window = secret % 10
        previous_price = 0
        sold = set()

        for i in range(2000):
            secret = hash(secret)
            price = secret % 10
            sliding_window = (sliding_window << 4) + price - previous_price & 0xFFFF
            previous_price = price

            if i > 2 and sliding_window not in sold:
                trend_value[sliding_window] += price
                sold.add(sliding_window)

    print(max(trend_value.values()))
