with open("input.txt", "r") as file:
    stream = file.read().strip()

size = 14

window = []
counter = 0
for char in stream:
    counter += 1
    window.append(char)
    if len(window) > size:
        window.pop(0)
    if len(window) == size and len(set(window)) == len(window):
        break

print(counter)
