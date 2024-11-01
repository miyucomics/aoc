def count_configurations(layout, groups):
    if layout == "":
        return 1 if groups == () else 0
    if groups == ():
        return 0 if "#" in layout else 1

    # the layout must be at least big enough to contain the remaining groups
    if sum(list(groups)) + len(groups) - 1 > len(layout):
        return 0

    count = 0

    if layout[0] in ".?":
        count += count_configurations(layout[1:], groups)

    if layout[0] in "#?":
        # there should not be an operational spring in the next n springs
        # where n is the first number of our group
        if "." in layout[:groups[0]]:
            return count

        # unless at the very end, there must be a non-damaged spring right after this ground
        if (groups[0] == len(layout) or layout[groups[0]] != "#"):
            count += count_configurations(layout[groups[0] + 1:], groups[1:])

    return count

with open("input.txt", "r") as file:
    answer = 0
    for line in file.read().splitlines():
        layout, groups = line.split()
        groups = tuple(map(int, groups.split(",")))
        answer += count_configurations(layout, groups)
    print(answer)
