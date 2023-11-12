def factor(item): return 38 if item.isupper() else 96
with open("input/day03", "r") as f:
    input = f.read().split("\n") # read contents of each pack
    data = [[c[:int(len(c)/2)], c[int(len(c)/2):]] for c in input] # split into two equal compartments
    data = ["".join(set(pack[0]).intersection(pack[1])) for pack in data] # find items in both compartments
    print(sum([ord(i)-factor(i) for i in data])) # summarize based on priority

    groups = [input[x:x+3] for x in range(0, len(input), 3)] # divide into groups of 3
    badges = ["".join(set(g[0]).intersection(g[1]).intersection(g[2])) for g in groups] # find items in all packs
    print(sum([ord(i)-factor(i) for i in badges])) # summarize based on priority