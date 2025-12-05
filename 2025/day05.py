with open("input/day05.txt", "r") as f:
    fresh, available = f.read().split("\n\n")
    fresh = [tuple(map(int, line.split("-"))) for line in fresh.splitlines()]
    available = [int(i) for i in available.splitlines()]

part1 = []
for item in available:
    if any(lower <= item <= upper for (lower, upper) in fresh):
        part1.append(item)

fresh.sort()
part2 = 0
prev = 0
for lower, upper in fresh:
    upper += 1
    if upper > prev:
        part2 += upper - max(lower, prev)
        prev = upper


print(f"Part 1: {len(part1)}")
print(f"Part 2: {part2}")
