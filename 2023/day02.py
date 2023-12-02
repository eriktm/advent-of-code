import re


with open("input/day02.txt") as f:
    raw = f.read().splitlines()
    data = []
    for line in raw:
        idx, vals = line.split(": ")
        turns = vals.split("; ")
        data.append({"id": int(idx.split()[1]), "turns": turns})


# part 1
possible = {"red": 12, "green": 13, "blue": 14}
valid_ids = []
for game in data:
    valid = True
    for turn in game["turns"]:
        m = re.findall(r"(\d+) (red|green|blue)", turn)
        if not all([True if int(c[0]) <= possible[c[1]] else False for c in m]):
            valid = False
    if valid:
        valid_ids.append(game["id"])

print(sum(set(valid_ids)))


# part 2
powers = []
for game in data:
    highest = {"red": 0, "green": 0, "blue": 0}
    for turn in game["turns"]:
        m = re.findall(r"(\d+) (red|green|blue)", turn)
        for c in m:
            if int(c[0]) > highest[c[1]]:
                highest[c[1]] = int(c[0])
    powers.append(highest["red"] * highest["green"] * highest["blue"])

print(sum(powers))
