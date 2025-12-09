from collections import deque

with open("input.txt") as file:
    points = []
    for line in file.readlines():
        x, y = line.split(",")
        points.append((int(x), int(y)))

x_values = sorted({x for x, _ in points})
y_values = sorted({y for _, y in points})
x_to_comp = {val: i * 2 for i, val in enumerate(x_values)}
y_to_comp = {val: i * 2 for i, val in enumerate(y_values)}

grid_width = len(x_values) * 2 - 1
grid_height = len(y_values) * 2 - 1
grid = [[1] * grid_height for _ in range(grid_width)]

loop_points = points + points[:1]
for i in range(len(points)):
    (ax, ay) = loop_points[i]
    (bx, by) = loop_points[i + 1]
    comp_ax, comp_ay = x_to_comp[ax], y_to_comp[ay]
    comp_bx, comp_by = x_to_comp[bx], y_to_comp[by]
    for x in range(min(comp_ax, comp_bx), max(comp_ax, comp_bx) + 1):
        for y in range(min(comp_ay, comp_by), max(comp_ay, comp_by) + 1):
            grid[x][y] = 0

outside_region = {(-1, -1)}
queue = deque(outside_region)

while queue:
    x, y = queue.popleft()
    for dx, dy in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
        if dx < -1 or dy < -1 or dx > len(grid) or dy > len(grid[0]):
            continue
        if 0 <= dx < len(grid) and 0 <= dy < len(grid[0]) and grid[dx][dy] == 0:
            continue
        if (dx, dy) in outside_region:
            continue
        outside_region.add((dx, dy))
        queue.append((dx, dy))

for x in range(len(grid)):
    for y in range(len(grid[0])):
        if (x, y) not in outside_region:
            grid[x][y] = 0

prefix_sum = [[0] * len(row) for row in grid]
for x in range(len(prefix_sum)):
    for y in range(len(prefix_sum[0])):
        prefix_sum[x][y] = (
            grid[x][y]
            + (prefix_sum[x - 1][y] if x > 0 else 0)
            + (prefix_sum[x][y - 1] if y > 0 else 0)
            - (prefix_sum[x - 1][y - 1] if x > 0 and y > 0 else 0)
        )

rectangles = []
for i, (ax, ay) in enumerate(points):
    for j in range(i):
        (bx, by) = points[j]
        area = (abs(ax - bx) + 1) * (abs(ay - by) + 1)
        rectangles.append((area, ax, ay, bx, by))

rectangles.sort(reverse=True)
for area, ax, ay, bx, by in rectangles:
    comp_ax, comp_ay = x_to_comp[ax], y_to_comp[ay]
    comp_bx, comp_by = x_to_comp[bx], y_to_comp[by]
    if (
        prefix_sum[comp_bx][comp_by]
        - (prefix_sum[comp_ax - 1][comp_by] if comp_ax > 0 else 0)
        - (prefix_sum[comp_bx][comp_ay - 1] if comp_ay > 0 else 0)
        + (prefix_sum[comp_ax - 1][comp_ay - 1] if comp_ax > 0 and comp_ay > 0 else 0)
    ) == 0:
        print(area)
        exit()
