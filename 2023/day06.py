import re
import numpy as np


def calculate(race: tuple[int, int]) -> list[int]:
    time, record = race
    possibles = []

    for i in range(1, time + 1):
        distance = i * (time - i)
        if distance > record:
            possibles.append(i)

    return possibles


if __name__ == "__main__":
    with open("input/day06.txt") as f:
        data = f.read()
        data1 = [
            tuple(int(x.group()) for x in re.finditer(r"\d+", line))
            for line in data.splitlines()
        ]
        data1 = list(zip(*data1))
        data2 = tuple(
            [int(x.group()) for x in re.finditer(r"\d+", data.replace(" ", ""))]
        )

    possibilities = [calculate(race) for race in data1]
    print("Part 1:", np.prod(list(map(len, possibilities))))
    print("Part 2:", len(calculate(data2)))
