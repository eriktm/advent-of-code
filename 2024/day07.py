from itertools import product
from operator import add, mul


def concat(a, b):
    return int(f"{a}{b}")


def solve(line, operators):
    total, parts = line
    for ops in product(operators, repeat=len(parts) - 1):
        score = 0
        for idx, op in enumerate(ops):
            score = op(score or parts[idx], parts[idx + 1])

        if score == total:
            return score

    return 0


with open("input/day07.txt", "r") as f:
    data = [
        (int(line.split()[0]), list(map(int, line.split()[1:])))
        for line in f.read().replace(":", "").splitlines()
    ]


print(f"Part 1: {sum([solve(line, (add, mul)) for line in data])}")
print(f"Part 2: {sum([solve(line, (add, mul, concat)) for line in data])}")
