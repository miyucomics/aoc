from collections import deque

with open("input.txt", "r") as file:
    stream = file.read().strip()

size = 4

window = deque()
counter = 0
for char in stream:
    counter += 1
    window.append(char)
    if len(window) > size:
        window.popleft()
    if len(window) == size and len(set(window)) == len(window):
        print(counter)
        exit()
