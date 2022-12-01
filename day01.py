# open and read file contents. read into a list, stripping \n
def lists_from_list(data, separator):
    """
    Splits out one list into several smaller lists based on
    the specified separator element.
    """
    idx = 0
    while idx < len(data):
        try:
            pos = data.index(separator, idx)
        except ValueError:
            # if the separator is not found in the list, that means we're done
            break

        yield data[idx:pos]
        
        # increase index, making sure to skip the separator
        # element so we don't hit it again on the next iteration
        idx = pos + 1


def main():
    with open("input/day01", "r") as f:
        data = f.read().splitlines()

    print(f"got {len(data)} lines")

    # separate out the elves based on a blank line in the input file
    # also convert strings to int at this point (can't do on import
    # because of the blank line)
    elves = [list(map(int, elf)) for elf in lists_from_list(data, "")]
    print(f"got {len(elves)} elves")

    # get the sum of each elf, and print out the highest amount
    totals = [sum(e) for e in elves]
    print(max(totals))

    # also print out the sum of the 3 highest
    print(sum(sorted(totals)[-3:]))


if __name__ == "__main__":
    main()
