import re

with open("input/day03.txt", "r") as f:
    data = f.read()

p_mul = r"mul\((\d+,\d+)\)"
p_instr = r"(do\(\)|don\'t\(\))"

matches = re.findall(p_mul, data)
pairs = [(int(x.split(",")[0]), int(x.split(",")[1])) for x in matches]
res1 = sum([x * y for (x, y) in pairs])
print(f"Part 1: {res1}")

instructions = [{"pos": 0, "action": True}]
instructions.extend(
    [
        {"pos": match.start(), "action": match.group() == "do()"}
        for match in re.finditer(p_instr, data)
    ]
)
instructions.append({"pos": len(data), "action": False})
instrs = []
last_action = False
for i in instructions:
    if i["action"] != last_action:
        instrs.append(i["pos"])
        last_action = i["action"]
instrs = [range(instrs[x], instrs[x + 1]) for x in range(0, len(instrs), 2)]

muls = []
for match in re.finditer(p_mul, data):
    if any([match.start() in r for r in instrs]):
        muls.append(match.groups()[0])

pairs2 = [(int(x.split(",")[0]), int(x.split(",")[1])) for x in muls]
res2 = sum([x * y for (x, y) in pairs2])
print(f"Part 2: {res2}")
