with open("input/day06", "r") as f:
    data = f.read()

    # first series of 4 non-repeating characters
    for idx in range(0, len(data)):
        if len(set(data[0:idx+1][-4:])) < 4: continue
        print(idx+1)
        break

    # first series of 14 non-repeating characters
    for idx in range(0, len(data)):
        if len(set(data[0:idx+1][-14:])) < 14: continue
        print(idx+1)
        break
