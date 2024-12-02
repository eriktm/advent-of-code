def is_safe(line):
    changes = [line[idx + 1] - line[idx] for idx in range(len(line) - 1)]

    if not all(x < 0 for x in changes) and not all(x > 0 for x in changes):
        return 0

    if all(abs(x) <= 3 for x in changes):
        return 1

    return 0


with open("input/day02.txt", "r") as f:
    data = [list(map(int, line.split())) for line in f.read().splitlines()]

safe_count = 0
dampened_safe = 0
for line in data:
    if is_safe(line):
        safe_count += 1
        continue

    safes = 0
    for idx in range(len(line)):
        safes += is_safe(line[:idx] + line[idx + 1 :])
    if safes >= 1:
        dampened_safe += 1

print(f"Part 1: {safe_count}")
print(f"Part 2: {safe_count + dampened_safe}")
