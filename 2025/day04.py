def solve(data, only_length=True):
    def find_at_pos(x, y, dx, dy):
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= len(data[0]) or ny < 0 or ny >= len(data):
            return None

        return data[ny][nx]

    adjs = [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    ]
    avail_coords = set()

    for yi, yv in enumerate(data):
        for xi, xv in enumerate(yv):
            if xv == ".":
                continue

            c = 0
            for dx, dy in adjs:
                c += find_at_pos(xi, yi, dx, dy) == "@"
            if c < 4:
                avail_coords.add((xi, yi))

    return len(avail_coords) if only_length else avail_coords


def clean(data):
    removed = 0
    while coords := solve(data, False):
        for xi, yi in coords:
            data[yi][xi] = "."
            removed += 1

    return removed


with open("input/day04.txt", "r") as f:
    data = [[c for c in line] for line in f.read().splitlines()]

print(f"Part 1: {solve(data)}")
print(f"Part 2: {clean(data)}")
