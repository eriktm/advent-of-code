def search_word(grid, word):
    def search_from_position(x, y, dx, dy):
        for i in range(len(word)):
            nx, ny = x + i * dx, y + i * dy
            if (
                nx < 0
                or nx >= len(grid)
                or ny < 0
                or ny >= len(grid[0])
                or grid[nx][ny] != word[i]
            ):
                return False
        return True

    directions = [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    ]  # 8 directions
    occurrences = []
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            for dx, dy in directions:
                if search_from_position(x, y, dx, dy):
                    occurrences.append(((x, y), (dx, dy)))
    return occurrences


def search_crosses(grid, center, chars):
    dir1 = [(-1, -1), (1, 1)]
    dir2 = [(-1, 1), (1, -1)]
    occurrences = []

    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if not grid[x][y] == center:
                continue

            hits = [[], []]
            for dx, dy in dir1:
                nx, ny = x + dx, y + dy
                if len(grid) <= nx or nx < 0 or len(grid[nx]) <= ny or ny < 0:
                    continue
                if grid[nx][ny] in chars:
                    hits[0] += grid[nx][ny]
            for dx, dy in dir2:
                nx, ny = x + dx, y + dy
                if len(grid) <= nx or nx < 0 or len(grid[nx]) <= ny or ny < 0:
                    continue
                if grid[nx][ny] in chars:
                    hits[1] += grid[nx][ny]

            if all([len(set(d)) == len(chars) for d in hits]):
                occurrences.append((x, y))

    return occurrences


with open("input/day04.txt", "r") as f:
    data = [[char for char in line] for line in f.read().splitlines()]

print(f"Part 1: {len(search_word(data, 'XMAS'))}")
print(f"Part 2: {len(search_crosses(data, 'A', ['M', 'S']))}")
