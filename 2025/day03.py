def solve(lines, length):
    score = 0

    for line in lines:
        start = 0
        res = []

        for i in range(length):
            remaining = length - i - 1
            end = len(line) - remaining
            c = max(line[start:end])
            start = start + line[start:end].index(c) + 1
            res.append(c)

        score += int("".join(map(str, res)))

    return score


with open("input/day03.txt", "r") as f:
    data = f.read().splitlines()
    data = [[int(c) for c in line] for line in data]


print(f"Part 1: {solve(data, 2)}")
print(f"Part 2: {solve(data, 12)}")
