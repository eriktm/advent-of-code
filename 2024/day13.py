import re


def solve(machine):
    (ax, ay), (bx, by), (rx, ry) = machine
    ca = cb = 0

    if rx > ry:
        cb = rx // bx
    else:
        cb = ry // by

    while (
        (((rx - cb * bx) // ax) * ax + cb * bx),
        (((ry - cb * by) // ay) * ay + cb * by),
    ) != (rx, ry):
        cb -= 1
        if cb < 0:
            return 0

    ca = (rx - cb * bx) // ax
    if ca < 0:
        return 0
    return ca * 3 + cb * 1


with open("input/day13.txt", "r") as f:
    data = f.read().split("\n\n")
    for idx, item in enumerate(data):
        res = re.findall(r"X(\+|\=)(\d+),\sY(\+|\=)(\d+)", item)
        data[idx] = (
            (int(res[0][1]), int(res[0][3])),
            (int(res[1][1]), int(res[1][3])),
            (int(res[2][1]), int(res[2][3])),
        )

# 76907 too high
# 27992 too low
print(f"Part 1: {sum([solve(machine) for machine in data])}")
