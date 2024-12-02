with open("input/day01.txt", "r") as f:
    data = f.read().splitlines()

left = sorted([int(d.split("   ")[0]) for d in data])
right = sorted([int(d.split("   ")[1]) for d in data])

diff = 0
score = 0
for idx in range(len(left)):
    diff += max(left[idx], right[idx]) - min(left[idx], right[idx])
    score += left[idx] * right.count(left[idx])

print(f"Part 1: {diff}")
print(f"Part 2: {score}")
