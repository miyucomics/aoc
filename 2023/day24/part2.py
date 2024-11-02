with open("input.txt", "r") as file:
    hailstones = [
        tuple(map(int, hailstone.replace(" @", ", ").replace(",", "").split()))
        for hailstone in file.read().splitlines()
    ]

def get_possible_velocities(a, b, a_velocity):
    possibilities = set()
    distance = b - a
    for test_velocity in range(-500, 500):
        if test_velocity == a_velocity:
            possibilities.add(test_velocity)
            continue
        if distance % (test_velocity - a_velocity) == 0:
            possibilities.add(test_velocity)
    return possibilities

potential_velocities = {"x": None, "y": None, "z": None}
for i, a in enumerate(hailstones):
    for b in hailstones[:i]:
        for dim, a_p, b_p, a_v, b_v in zip("xyz", a[:4], b[:4], a[3:], b[3:]):
            if a_v == b_v:
                new_velocities = get_possible_velocities(a_p, b_p, a_v)
                if potential_velocities[dim] is None:
                    potential_velocities[dim] = new_velocities.copy()
                potential_velocities[dim] &= new_velocities

rock_vx, rock_vy, rock_vz = [value.pop() for value in potential_velocities.values()]
a_x, a_y, a_z, a_vx, a_vy, a_vz = hailstones[0]
b_x, b_y, _, b_vx, b_vy, _ = hailstones[1]

# y = mx + b, solve for m and b
ma = (a_vy - rock_vy) / (a_vx - rock_vx)
mb = (b_vy - rock_vy) / (b_vx - rock_vx)
ba = a_y - (ma * a_x)
bb = b_y - (mb * b_x)

# set them equal to each other and solve for x
# m_a * x + b_a = m_b * x + b_b
# m_a * x - m_b * x = b_b - b_a
# x(m_a - m_b) = b_b - b_a
# x = (b_b - b_a) / (m_a - m_b)
x = int((bb - ba) / (ma - mb))

# plug the discovered x into one of the equations to get y
y = int(ma * x + ba)

# get the time the rock takes to hit the hailstone and derive z from that
time = (x - a_x) // (a_vx - rock_vx)
z = a_z + (a_vz - rock_vz) * time

# the rush of finally being able to type out x + y + z is amazing
print(x + y + z)
