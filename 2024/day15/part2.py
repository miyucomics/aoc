with open("input.txt") as file:
    world, moves = file.read().split("\n\n")

    world_width = world.find("\n")
    world_height = world.count("\n") + 1
    world = world.replace("\n", "")

    robot_index = world.find("@")
    robot = robot_index % world_width * 2 + robot_index // world_width * 1j

    expansions = {"#": "##", ".": "..", "O": "[]", "@": ".."}
    world = list("".join(expansions[char] for char in world))
    world_width *= 2

    direction_lookup = {"<": -1, "^": -1j, ">": 1, "v": 1j}
    moves = [direction_lookup[char] for char in moves.replace("\n", "")]

def print_map():
    for i in range(world_height):
        print("".join(world[i * world_width:(i + 1) * world_width]))

def get(location):
    if location.real < 0 or location.real >= world_width or location.imag < 0 or location.imag >= world_height:
        return "#"
    return world[int(world_width * location.imag + location.real)]

def can_push(position, move):
    affected = [position]
    for half in affected:
        new = half + move
        if new in affected:
            continue
        char = get(new)
        if char == "#":
            return False, []
        elif char == "[":
            affected.append(new)
            affected.append(new + 1)
        elif char == "]":
            affected.append(new)
            affected.append(new - 1)
    return True, affected

def attempt_move(move):
    new = robot + move
    if get(new) == "#":
        return robot

    if get(new) in "[]":
        pushable, chain = can_push(robot, move)
        if not pushable:
            return robot

        for box in reversed(chain):
            world[int(world_width * (box + move).imag + (box + move).real)] = world[int(world_width * box.imag + box.real)]
            world[int(world_width * box.imag + box.real)] = "."

    return new

for move in moves:
    robot = attempt_move(move)

print(sum(
    i // world_width * 100 + i % world_width
    for i, char in enumerate(world)
    if char == "["
))
