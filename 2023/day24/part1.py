with open("input.txt", "r") as file:
    hailstones = [
        (x, y, dx, dy)
        for hailstone in file.read().splitlines()
        for x, y, _, dx, dy, _ in [map(int, hailstone.replace(" @", "").replace(",", "").split())]
    ]

def intersects_within_bounds(hail1, hail2):
    a1, b1, c1 = hail1[3], -hail1[2], hail1[3] * hail1[0] - hail1[2] * hail1[1]
    a2, b2, c2 = hail2[3], -hail2[2], hail2[3] * hail2[0] - hail2[2] * hail2[1]
    if a1 * b2 == a2 * b1:
        return False
    x = (b2 * c1 - b1 * c2) / (a1 * b2 - a2 * b1)
    y = (c2 * a1 - c1 * a2) / (a1 * b2 - a2 * b1)
    if x < 200000000000000 or x > 400000000000000 or y < 200000000000000 or y > 400000000000000:
        return False
    return all((x - hs[0]) * hs[2] >= 0 and (y - hs[1]) * hs[3] >= 0 for hs in (hail1, hail2))

print(sum(
    intersects_within_bounds(a, b)
    for index, a in enumerate(hailstones)
    for b in hailstones[:index]
))
