from itertools import combinations

with open("input/day08.txt", "r") as f:
    raw_data = f.read()
    grid = [[char for char in line] for line in raw_data.splitlines()]
    freqs = set([char for char in raw_data.replace("\n", "") if char != "."])

antennas = {key: set() for key in freqs}
for x in range(len(grid)):
    for y in range(len(grid[0])):
        if grid[x][y] in freqs:
            antennas[grid[x][y]].add((x, y))


def in_grid(x, y):
    return x >= 0 and x < len(grid) and y >= 0 and y < len(grid[0])


def paired_antinodes():
    antinodes = set()
    for _, positions in antennas.items():
        for (ax, ay), (bx, by) in combinations(positions, 2):
            dx, dy = ax - bx, ay - by
            possible_antinodes = [
                (ax + dx, ay + dy),
                (ax - dx, ay - dy),
                (bx + dx, by + dy),
                (bx - dx, by - dy),
            ]
            for px, py in possible_antinodes:
                if in_grid(px, py) and (px, py) != (ax, ay) and (px, py) != (bx, by):
                    antinodes.add((px, py))
    return antinodes


def endless_antinodes():
    antinodes = set()
    for _, positions in antennas.items():
        for (ax, ay), (bx, by) in combinations(positions, 2):
            dx, dy = ax - bx, ay - by
            px, py = ax, ay
            while in_grid(px, py):
                antinodes.add((px, py))
                px, py = px + dx, py + dy
            px, py = bx, by
            while in_grid(px, py):
                antinodes.add((px, py))
                px, py = px - dx, py - dy
    return antinodes


print(f"Part 1: {len(paired_antinodes())}")
print(f"Part 2: {len(endless_antinodes())}")
