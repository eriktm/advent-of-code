with open("input/day02.txt", "r") as f:
    data = f.read().split(",")
    data = [tuple(map(int, r.split("-"))) for r in data]

part1 = part2 = 0

for i, j in data:
    x = list(map(str, range(i, j + 1)))
    for y in x:
        if len(y) % 2 == 0:
            middle = len(y) // 2
            if y[:middle] == y[middle:]:
                # print(y)
                part1 += int(y)
                part2 += int(y)
                continue

        split = 3
        while split <= len(y):
            if len(y) % split == 0:
                parts = list(map("".join, zip(*[iter(y)] * int(len(y) / split))))
                if len(parts) > 0 and all(p == parts[0] for p in parts):
                    # print(y)
                    part2 += int(y)

            split += 1


print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
