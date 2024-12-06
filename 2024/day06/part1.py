with open("input.txt") as file:
    world = file.read()
    world_width = world.find("\n")
    world_height = world.count("\n")
    world = world.replace("\n", "")

    player_position = world.find("^")
    player_position = player_position % world_width + (player_position // world_width) * 1j
    player_direction = -1j

def get(location):
    if location.real < 0 or location.real >= world_width or location.imag < 0 or location.imag >= world_height:
        return "!"
    return world[int(world_width * location.imag + location.real)]

visited = set()
while True:
    visited.add(player_position)
    player_position += player_direction
    current_tile = get(player_position)
    if current_tile == "#":
        player_position -= player_direction
        player_direction *= 1j
    elif current_tile == "!":
        break

print(len(visited))
