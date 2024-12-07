with open("input.txt") as file:
    world = file.read()
    world_width = world.find("\n")
    world_height = world.count("\n")
    world = world.replace("\n", "")

    player_position = world.find("^")
    player_position = player_position % world_width + (player_position // world_width) * 1j
    original_player_position = player_position
    player_direction = -1j

def get(location):
    if location.real < 0 or location.real >= world_width or location.imag < 0 or location.imag >= world_height:
        return "!"
    return world[int(world_width * location.imag + location.real)]

def will_be_in_loop(spawning_position, guard_direction):
    turns = set()
    potential_position = spawning_position - guard_direction
    potential_direction = guard_direction

    while True:
        potential_position += potential_direction
        current_tile = get(potential_position)
        if potential_position == spawning_position or current_tile == "#":
            potential_position -= potential_direction
            potential_direction *= 1j
            if (potential_position, potential_direction) in turns:
                return True
            turns.add((potential_position, potential_direction))
        elif current_tile == "!":
            return False

states = {}
while True:
    if player_position not in states.keys():
        states[player_position] = player_direction
    player_position += player_direction
    current_tile = get(player_position)
    if current_tile == "#":
        player_position -= player_direction
        player_direction *= 1j
    elif current_tile == "!":
        break

print(sum(
    will_be_in_loop(position, direction)
    for position, direction in states.items()
))
