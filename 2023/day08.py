import re
import math


def count_steps(start, end, instr):
    steps = 0
    current_node = (start, coords.get(start))
    while not end(current_node):
        for i in instr:
            steps += 1
            next_node = current_node[1][i]
            current_node = (next_node, coords.get(next_node))
    return steps


with open("input/day08.txt") as f:
    instructions, coords = f.read().split("\n\n")
    coords = [
        tuple(m.group() for m in re.finditer(r"\w{3}", coord))
        for coord in coords.splitlines()
    ]
    coords = dict([(x, (y, z)) for x, y, z in coords])
    instr = [0 if i == "L" else 1 for i in instructions]

# Part 1
steps1 = count_steps("AAA", lambda x: x[0] == "ZZZ", instr)
print(steps1)

# Part 2
steps2 = []
for node in [(n, coords.get(n)) for n in coords.keys() if n.endswith("A")]:
    steps2.append(count_steps(node[0], lambda x: x[0][-1] == "Z", instr))
print(math.lcm(*steps2))
