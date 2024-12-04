with open("input.txt") as file:
    world = file.read()
    world_width = world.find("\n")
    world_height = world.count("\n")
    world = world.replace("\n", "")

def get(location):
    if location.real < 0 or location.real >= world_width or location.imag < 0 or location.imag >= world_height:
        return "."
    return world[int(world_width * location.imag + location.real)]

directions = [-1 - 1j, -1j, 1 - 1j, -1, 1, -1 + 1j, 1j, 1 + 1j]

def matches(position):
    return sum(all(
        get(position + (index + 1) * direction) == char
        for index, char in enumerate("MAS")
    ) for direction in directions)

print(sum(
    matches(x + y * 1j)
    for x in range(world_width)
    for y in range(world_height)
    if get(x + y * 1j) == "X"
))
