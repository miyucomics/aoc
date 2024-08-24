with open("input.txt") as file:
    world = tuple(file.read().splitlines())

iteration = 0
states = [world]
while True:
    iteration += 1

    # north
    world = tuple(map("".join, zip(*world)))
    world = tuple("#".join("".join(sorted(text, reverse=True)) for text in row.split("#")) for row in world)

    # west
    world = tuple(map("".join, zip(*world)))
    world = tuple("#".join("".join(sorted(text, reverse=True)) for text in row.split("#")) for row in world)

    # south
    world = tuple(map("".join, zip(*world)))
    world = tuple("#".join("".join(sorted(text)) for text in row.split("#")) for row in world)

    # east
    world = tuple(map("".join, zip(*world)))
    world = tuple("#".join("".join(sorted(text)) for text in row.split("#")) for row in world)

    if world in states:
        break
    states.append(world)

loop_start = states.index(world)
final = states[(1000000000 - loop_start) % (iteration - loop_start) + loop_start]
final = tuple(map("".join, zip(*final)))  # transpose the future

print(sum(
    index + 1
    for row in final
    for index, char in enumerate(row[::-1])
    if char == "O"
))
