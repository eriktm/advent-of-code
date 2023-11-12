with open("input/day04", "r") as f:
    data = [l.split(",") for l in f.read().split("\n")] # read data and create a list with each pair being a list
    data = [[set([i for i in range(int(e.split("-")[0]), int(e.split("-")[1])+1)]) for e in g] for g in data] # expand the number ranges to sets

    print(sum([1 for pair in data if pair[0].issuperset(pair[1]) or pair[1].issuperset(pair[0])])) # pairs with full overlap
    print(sum([1 for pair in data if pair[0].intersection(pair[1])])) # pairs with partial overlap
