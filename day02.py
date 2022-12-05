shapes = {
    "A": "rock",
    "B": "paper",
    "C": "scissors",
    "X": "rock",
    "Y": "paper",
    "Z": "scissors"
}
results = {
    "X": 0,
    "Y": 3,
    "Z": 6
}
win = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}
scores = {
    "rock": 1,
    "paper": 2,
    "scissors": 3
}

with open("input/day02", "r") as f:
    data = [[s[0], s[2]] for s in f.read().split("\n")]

score1 = 0
for match in data:
    opponent = shapes[match[0]]
    play = shapes[match[1]]
    if win[opponent] == play: points = 0
    elif win[play] == opponent: points = 6
    else: points = 3
    score1 += scores.get(play) + points

print(score1)

score2 = 0
for match in data:
    opponent = shapes[match[0]]
    result = match[1]
    if result == "X": select = win[opponent]
    if result == "Y": select = opponent
    if result == "Z": select = list(win.keys())[list(win.values()).index(opponent)]
    score2 += scores.get(select) + results[result]

print(score2)
