import re


def parse(lines: list) -> int:
    total = []
    for line in lines:
        num1 = line[[x.isdigit() for x in line].index(True)]
        num2 = line[::-1][[x.isdigit() for x in line[::-1]].index(True)]
        total.append(int(f"{num1}{num2}"))
    return total


def replace_numbers(text: str) -> str:
    mapping = {
        "one": "o1e",
        "two": "t2o",
        "three": "t3e",
        "four": "f4r",
        "five": "f5e",
        "six": "s6x",
        "seven": "s7n",
        "eight": "e8t",
        "nine": "n9e",
    }

    regex = re.compile("(%s)" % "|".join(map(re.escape, mapping.keys())))
    return regex.sub(lambda match: mapping[match.group()], text)


with open("input/day01.txt") as f:
    data = [x.strip("\n") for x in f.readlines()]

# part 1
print(sum(parse(data)))

# part 2
new_data = []
for line in data:
    new_data.append(replace_numbers(replace_numbers(line)))

print(sum(parse(new_data)))
