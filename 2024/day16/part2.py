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
queue = []
def push_state(score, pos, dir, path):
    global uuid
    uuid += 1
    heappush(queue, (score, uuid, pos, dir, path))

optimal = {}
highscore = float("inf")
push_state(0, start, 1, tuple([start]))

seats = set()
while queue:
    score, _, pos, dir, path = heappop(queue)
    if score > highscore:
        break
    if (pos, dir) in optimal and optimal[(pos, dir)] < score:
        continue

    optimal[(pos, dir)] = score

    if pos == end:
        highscore = score
        seats |= set(path)

    if get(pos + dir) != "#":
        push_state(score + 1, pos + dir, dir, (*path, pos + dir))
    push_state(score + 1000, pos, dir * -1j, path)
    push_state(score + 1000, pos, dir * 1j, path)

print(len(seats))
