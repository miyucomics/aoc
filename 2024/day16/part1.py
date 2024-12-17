from heapq import heappush, heappop

with open("input.txt") as file:
    world = file.read()

    world_width = world.find("\n")
    world_height = world.count("\n")
    world = world.replace("\n", "")

    start = world.find("S")
    start = start % world_width + start // world_width * 1j

    end = world.find("E")
    end = end % world_width + end // world_width * 1j

def get(location):
    if location.real < 0 or location.real >= world_width or location.imag < 0 or location.imag >= world_height:
        return "#"
    return world[int(world_width * location.imag + location.real)]

uuid = 0
seen = set()
queue = []
def push_state(score, pos, dir):
    global uuid
    uuid += 1
    heappush(queue, (score, uuid, pos, dir))

push_state(0, start, 1)

while queue:
    score, _, pos, dir = heappop(queue)

    if (pos, dir) in seen:
        continue
    seen.add((pos, dir))

    if pos == end:
        print(score)
        exit()

    if get(pos + dir) != "#":
        push_state(score + 1, pos + dir, dir)
    push_state(score + 1000, pos, dir * -1j)
    push_state(score + 1000, pos, dir * 1j)
