from functools import reduce
from operator import add, mul


def cephalopod_rotate(data):
    result = []
    chars = max(len(s) for s in data)

    for col in range(chars - 1, -1, -1):
        if ch := "".join(s[col] for s in data if col < len(s)):
            result.append(ch)

    return result


with open("input/day06.txt", "r") as f:
    data = f.read().splitlines()
    data1 = list(zip(*[line.split() for line in data][::]))

opmap = {"*": mul, "+": add}

part1 = part2 = 0
for prob in data1:
    op = opmap.get(prob[-1])
    part1 += reduce(op, map(int, prob[:-1]))

ops = data[-1]
idxs = [idx for idx, val in enumerate(ops) if val != " "]
data2 = []
for line in data:
    new_line = []
    for idx, pos in enumerate(idxs):
        end = len(line) if idx == len(idxs) - 1 else idxs[idx + 1] - 1
        new_line.append(line[pos:end])
    data2.append(new_line)
data2 = list(zip(*data2[::]))
data2 = [cephalopod_rotate(line[:-1]) for line in data2]

for idx, prob in enumerate(data2):
    op = opmap.get(ops[idxs[idx]])
    part2 += reduce(op, map(int, prob))

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
