def extrapolate(line):
    sets = [line]
    last_set = []
    while not set(last_set) == set(
        [
            0,
        ]
    ):
        last_set = []
        for i, l in enumerate(sets[-1]):
            if i == len(sets[-1]) - 1:
                break
            last_set.append(sets[-1][i + 1] - l)
        sets.append(last_set)

    sets.reverse()
    return sets


def find_next_value(line, reverse=False):
    if reverse:
        sets = [x[::-1] for x in extrapolate(line)]
    else:
        sets = extrapolate(line)
    for i, s in enumerate(sets):
        if i == 0:
            sets[i].append(0)
            continue

        if reverse:
            sets[i].append(s[-1] - sets[i - 1][-1])
        else:
            sets[i].append(s[-1] + sets[i - 1][-1])

    return sets[-1][-1]


with open("input/day09.txt") as f:
    data = [list(map(int, line.split())) for line in f.read().splitlines()]

print(sum([find_next_value(line) for line in data]))
print(sum([find_next_value(line, True) for line in data]))
