with open("input.txt") as file:
    world, moves = file.read().split("\n\n")

    world_width = world.find("\n")
    world_height = world.count("\n") + 1
    world = world.replace("\n", "")

    robot_index = world.find("@")
    robot = robot_index % world_width + robot_index // world_width * 1j

    world = list(world)
    world[robot_index] = "."

    direction_lookup = {"<": -1, "^": -1j, ">": 1, "v": 1j}
    moves = [direction_lookup[char] for char in moves.replace("\n", "")]

def get(location):
    if location.real < 0 or location.real >= world_width or location.imag < 0 or location.imag >= world_height:
        return "#"
    return world[int(world_width * location.imag + location.real)]

def can_push(position, move):
    affected = []
    position += move
    while get(position) == "O":
        affected.append(position)
        position += move
    if get(position) == ".":
        return True, affected
    return False, []

def attempt_move(move):
    new = robot + move
    if get(new) == "#":
        return robot

    if get(new) == "O":
        pushable, affected = can_push(robot, move)
        if not pushable:
            return robot

        for box in reversed(affected):
            world[int(world_width * box.imag + box.real)] = "."
            world[int(world_width * (box + move).imag + (box + move).real)] = "O"

    return new

for move in moves:
    robot = attempt_move(move)

print(sum(
    i // world_width * 100 + i % world_width
    for i, char in enumerate(world)
    if char == "O"
))
