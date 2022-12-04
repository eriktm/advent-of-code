scores = {"X": 1, "Y": 2, "Z": 3}
def fight(a, b):
    if ord(a) == ord(b)-23:
        return 3
    elif (a == "A" and b == "Z") or (a == "B" and b == "X") or (a == "C" and b == "Y"):
        return 0
    else:
        return 6

with open("input/day02", "r") as f:
    data = f.read().split("\n")
    data = [[s.split()[0], s.split()[1]] for s in data]

score = 0
for match in data:
    points = scores[match[1]] + fight(match[0], match[1])
    #print(f"{match=}, {points=}")
    score += points

print(score)