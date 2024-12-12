from collections import deque


def ranges(nums):
    nums = sorted(set(nums))
    gaps = [[s, e] for s, e in zip(nums, nums[1:]) if s + 1 < e]
    edges = iter(nums[:1] + sum(gaps, []) + nums[-1:])
    return list(zip(edges, edges))


def trace(grid, start):
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    seen = set()

    queue = deque([start])

    while queue:
        node = queue.pop()
        if node in seen:
            continue

        seen.add(node)
        r, c = node

        for nr, nc in [(r + dr, c + dc) for dr, dc in directions]:
            if nr >= 0 and nr < len(grid) and nc >= 0 and nc < len(grid[0]):
                if grid[nr][nc] == grid[r][c]:
                    queue.append((nr, nc))

    return seen


def edges(box):
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    total = 0
    seen = set()

    for r, c in box:
        for nr, nc in [(r + dr, c + dc) for dr, dc in directions]:
            if (nr, nc) not in box:
                seen.add(((r, c), (r - nr, c - nc)))
                total += 1

    unique = set()
    for (r, c), (dr, dc) in seen:
        if dr == 0:
            unique.add(("c", c, dc))
        else:
            unique.add(("r", r, dr))

    edges = 0
    for u in unique:
        if u[0] == "c":
            ud = set([r for (r, c), (_, dc) in seen if c == u[1] and dc == u[2]])
        else:
            ud = set([c for (r, c), (dr, _) in seen if r == u[1] and dr == u[2]])

        edges += len(ranges(ud))

    return total, edges


with open("input/day12.txt", "r") as f:
    data = [[char for char in line] for line in f.read().splitlines()]

gardens = []
for r, row in enumerate(data):
    for c, col in enumerate(row):
        if not any([(r, c) in garden for garden in gardens]):
            gardens.append(trace(data, (r, c)))


print(f"Part 1: {sum([len(garden) * edges(garden)[0] for garden in gardens])}")
print(f"Part 2: {sum([len(garden) * edges(garden)[1] for garden in gardens])}")
