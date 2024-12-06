def get_coords(chart, item):
    for x in range(len(chart)):
        for y in range(len(chart[x])):
            if chart[x][y] == item:
                return x, y


def next_dir(dx, dy):
    if (dx, dy) == (-1, 0):
        return (0, 1)
    elif (dx, dy) == (0, 1):
        return (1, 0)
    elif (dx, dy) == (1, 0):
        return (0, -1)
    elif (dx, dy) == (0, -1):
        return (-1, 0)


def map_path(chart, start, dir):
    px, py = start
    dx, dy = dir
    path = [start]

    while True:
        nx, ny = px + dx, py + dy
        # print(f"{px=}, {py=}, {dx=}, {dy=}, {nx=}, {ny=}")
        if nx < 0 or nx > len(chart) - 1 or ny < 0 or ny > len(chart[0]) - 1:
            return path

        if chart[nx][ny] == "#":
            dx, dy = next_dir(dx, dy)
            continue

        px, py = nx, ny
        path.append((nx, ny))


with open("input/day06.txt", "r") as f:
    data = [[char for char in line] for line in f.read().splitlines()]

paths = map_path(data, get_coords(data, "^"), (-1, 0))
print(f"Part 1: {len(set(paths))}")
