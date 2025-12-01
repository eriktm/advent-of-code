def solve(instructions, all_passes=False) -> int:
    pos = 50
    stops = passes = 0

    for instr in instructions:
        # transform the instruction to a number, positive or negative
        delta = int(instr[1:]) * (-1 if instr[0] == "L" else 1)

        # get new position after any wraparounds
        pos = (pos + delta) % 100

        # both solutions count stops at 0
        if pos == 0:
            stops += 1
            passes += 1

        # number of times we passed 0, not counting the stop above
        passes += abs(delta) // 100
        passes += delta > 0 and pos < (delta % 100) and pos != 0
        passes += delta < 0 and pos > 100 - (abs(delta) % 100)

    return passes if all_passes else stops


with open("input/day01.txt", "r") as f:
    data = f.read().splitlines()


print(f"Part 1: {solve(data)}")
print(f"Part 2: {solve(data, True)}")
