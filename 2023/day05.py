import re
from concurrent.futures import ProcessPoolExecutor


def process_seed(seed, maps):
    next_coords = seed
    for _, ranges in maps.items():
        for r in ranges:
            if r[1] <= next_coords <= (r[1] + r[2]):
                next_coords = r[0] + next_coords - r[1]
                break
        else:
            continue

    return next_coords


def run(seed_range):
    total = []
    for seed in range(seed_range[0], seed_range[0] + seed_range[1]):
        total.append(process_seed(seed, maps))
    print(min(total))


with open("input/day05.txt") as f:
    data = f.read().split("\n\n")


maps = {}
for stuff in data[1:]:
    source, destination = re.findall(r"(\w+)-to-(\w+)", stuff)[0]
    maps[destination] = list()
    for match in re.finditer(r"\d+ \d+ \d+", stuff):
        maps[destination].append(tuple(map(int, match.group().split())))


if __name__ == "__main__":
    # part 1
    seeds = list(map(int, re.findall(r"\d+", data[0])))
    total = [process_seed(seed, maps) for seed in seeds]
    print(min(total))

    # part 2
    seed_ranges = []
    for match in re.finditer(r"\d+ \d+", data[0][7:]):
        seed_ranges.append(tuple(int(s) for s in match.group().split()))

    # find the lowest number in the output manually
    with ProcessPoolExecutor(len(seed_ranges)) as exe:
        exe.map(run, seed_ranges)
