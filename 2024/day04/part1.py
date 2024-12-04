with open("input.txt") as file:
    world = file.read()
    world_width = world.find("\n")
    world_height = world.count("\n")
    world = world.replace("\n", "")

def get(location):
    if location.real < 0 or location.real >= world_width or location.imag < 0 or location.imag >= world_height:
        return "."
    return world[int(world_width * location.imag + location.real)]

target_string = "XMAS"
directions = [
    dx + dy * 1j
    for dx in range(-1, 2)
    for dy in range(-1, 2)
    if not (dx == 0 and dy == 0)
]

def matches(position):
    return sum(
        all(get(position + (index + 1) * direction) == char for index, char in enumerate(target_string[1:]))
        for direction in directions
    )

print(sum(
    matches(x + y * 1j)
    for x in range(world_width)
    for y in range(world_height)
    if get(x + y * 1j) == target_string[0]
))
