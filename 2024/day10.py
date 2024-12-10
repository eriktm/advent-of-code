from collections import deque


def trace_trails(grid, start):
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    seen = set()
    total = 0

    # create a queue consisting of only the start position
    queue = deque([start])

    # loop until the queue is empty
    while queue:
        node = queue.pop()
        if node in seen:
            continue

        seen.add(node)
        r, c = node

        if grid[r][c] == 9:
            total += 1

        # add any valid next steps to the queue for further tracing
        for nr, nc in [(r + dr, c + dc) for dr, dc in directions]:
            if nr >= 0 and nr < len(grid) and nc >= 0 and nc < len(grid[0]):
                if grid[nr][nc] == grid[r][c] + 1:
                    queue.append((nr, nc))

    return total


def rate_trails(grid, start):
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    queue = deque([(start, (start,))])
    seen = set()
    paths = set()

    while queue:
        node = queue.pop()
        if node in seen:
            continue

        seen.add(node)
        (r, c), path = node

        if grid[r][c] == 9:
            paths.add(path)

        for nr, nc in [(r + dr, c + dc) for dr, dc in directions]:
            if nr >= 0 and nr < len(grid) and nc >= 0 and nc < len(grid[0]):
                if grid[nr][nc] == grid[r][c] + 1:
                    queue.append(((nr, nc), path + ((nr, nc))))

    return len(paths)


with open("input/day10.txt", "r") as f:
    grid = [list(map(int, line)) for line in f.read().splitlines()]
    starts = set(
        [(r, c) for r, row in enumerate(grid) for c, col in enumerate(row) if col == 0]
    )

print(f"Part 1: {sum([trace_trails(grid, s) for s in starts])}")
print(f"Part 2: {sum([rate_trails(grid, s) for s in starts])}")
