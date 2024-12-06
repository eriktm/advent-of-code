def get_coords(chart, item):
    for x in range(len(chart)):
        for y in range(len(chart[x])):
            if chart[x][y] == item:
                return x, y


def map_path(chart):
    px, py = get_coords(chart, "^")
    dx, dy = -1, 0
    path = {((px, py), (dx, dy))}

    while True:
        nx, ny = px + dx, py + dy
        # print(f"{px=}, {py=}, {dx=}, {dy=}, {nx=}, {ny=}")
        if nx < 0 or nx > len(chart) - 1 or ny < 0 or ny > len(chart[0]) - 1:
            break

        if chart[nx][ny] == "#":
            dx, dy = dy, -dx
            continue

        coord = ((nx, ny), (dx, dy))
        if coord in path:
            return False, set()

        path.add(coord)
        px, py = nx, ny

    return True, {coord for coord, _ in path}


def find_new_obstacles(chart, path):
    obstacles = set()

    for x, y in path:
        if chart[x][y] != ".":
            continue

        chart[x][y] = "#"

        exited, _ = map_path(chart)
        if not exited:
            obstacles.add((x, y))

        chart[x][y] = "."

    return len(obstacles)


with open("input/day06.txt", "r") as f:
    data = [[char for char in line] for line in f.read().splitlines()]

_, path = map_path(data)
print(f"Part 1: {len(path)}")

obstacles = find_new_obstacles(data, path)
print(f"Part 2: {obstacles}")
