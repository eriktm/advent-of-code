import copy
import re

with open("input/day05", "r") as f:
    tbl, cmds = f.read().split("\n\n") # read out the starting table and commands
    tbl = tbl.replace("    ", "[ ]").split("\n") # fill in blanks in the table and split lines
    idx = tbl.pop().split() # pop out indexes
    tbl = [s.replace(" ", "")[1:-1].split("][") for s in tbl] # split text format into sub-lists
    tbl = list(zip(*tbl[::-1])) # rotate 2d list
    tbl = dict(zip(idx, [[i for i in s if i] for s in tbl])) # strip blank items and make a dict

tbl2 = copy.deepcopy(tbl) # make a full copy for part 2
for cmd in cmds.split("\n"):
    count, src, dest = re.search(r"^\w+\s(\d+)\s\w+\s(\d+)\s\w+\s(\d+)$", cmd).groups() # find the command numbers
    count = int(count)

    tbl2[dest].extend(tbl2[src][-count:]) # extend the destination with the correct number of items from the end of source
    del tbl2[src][-count:] # and remove them from source

    while count > 0:
        tbl[dest].append(tbl[src].pop()) # pop the last item from source and add to destination
        count -= 1 # do this count number of times

# print out the last (top-most) item in each stack
print("".join([stack[-1] for stack in tbl.values()]))
print("".join([stack[-1] for stack in tbl2.values()]))
