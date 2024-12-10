def last(d):
    return next((len(d) - 1 - i for i, v in enumerate(reversed(d)) if v != "."))


def is_fragmented(d):
    return "." in d and d.index(".") != sorted(
        d, reverse=True, key=lambda x: str(x)
    ).index(".")


def defrag(d):
    data = d.copy()

    while is_fragmented(data):
        idx = last(data)
        data[data.index(".")] = data.pop(idx)
        data.insert(idx, ".")

    return data


def mul(args):
    return args[0] * args[1] if args[1] != "." else 0


if __name__ == "__main__":
    with open("input/day09_ex.txt", "r") as f:
        data = [int(char) for char in f.read()]
        data = [
            int(idx / 2) if idx % 2 == 0 else "."
            for idx, val in enumerate(data)
            for _ in range(val)
        ]

    d1 = defrag(data)
    print(f"Part 1: {sum([idx * val for idx, val in enumerate(d1) if val != '.'])}")
