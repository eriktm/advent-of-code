#
# I first tried to solve this using a multi-dimensional array and looping over every.
# single. character. I couldn't make this work (or didn't have the time and/or patience).
# The code below is mostly a copy of the solution by @Jessseee(1) with some added comments
# from me while learning what actually happens here. Let's see if what I learned today
# sticks until the next 2D-challenge...
#
# (1) https://github.com/Jessseee/AdventOfCode
#

import re
from itertools import product
from numpy import prod


def get_adjacencies(pos: tuple[int, int]) -> list[tuple[int, int]]:
    # given an input (x, y) position, return a list
    # of all direct adjacencies, including diagonal
    return [
        tuple(map(sum, zip(pos, adj)))
        for adj in product([-1, 0, 1], repeat=2)
        if adj != (0, 0)
    ]


with open("input/day03.txt") as f:
    data = f.read().splitlines()

numbers, symbols = [], {}
for row, string in enumerate(data):
    # without this we'll get a "list index out of range" error
    numbers.append({})

    # find all numbers and save them based on their span (start and end position)
    for match in re.finditer(r"\d+", string):
        numbers[row][match.span()] = match.group()

    # find all symbols, except period, and save them with row and col positions
    for match in re.finditer(r"[^.|\w]", string):
        symbols[(row, match.start())] = match.group()

# numbers: a list with dicts per line
#   each dict contains the numbers in format:
#   (start_pos, end_pos): "value"

# symbols: a dict of all symbols
#   each symbol is represented in format:
#   (row_idx, col_idx): "value"

sum_part_numbers = sum_gear_ratios = 0
for position, symbol in symbols.items():
    # loop over every symbol, finding any possible adjacent coordinates
    adj = get_adjacencies(position)
    matches = {}
    for row, col in adj:
        # for every possible adjacency..
        for span, num in numbers[row].items():
            # check every actual number in the row of the possible adjacency..
            if col in range(*span):
                # we have a match if the column position of the possible adjacency
                # is within the span (start to end position) of the number
                matches[(row, span)] = int(num)
    sum_part_numbers += sum(matches.values())

    if symbol == "*" and len(matches) == 2:
        sum_gear_ratios += prod(list(matches.values()))

print(sum_part_numbers)
print(sum_gear_ratios)
