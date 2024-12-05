from functools import cmp_to_key


def has_correct_order(item, rules):
    for before, after in rules:
        if before in item and after in item and item.index(before) > item.index(after):
            return False
    return True


def sort_by_rules(item, rules):
    @cmp_to_key
    def compare(x, y):
        for before, after in rules:
            if x == before and y == after:
                return -1
            elif y == before and x == after:
                return 1

    return sorted(item, key=compare)


with open("input/day05.txt", "r") as f:
    rules, updates = f.read().split("\n\n")
    rules = [tuple(map(int, r.split("|"))) for r in rules.splitlines()]
    updates = [tuple(map(int, u.split(","))) for u in updates.splitlines()]

correct = [update for update in updates if has_correct_order(update, rules)]
print(f"Part 1: {sum([u[len(u)//2] for u in correct])}")

incorrect = [update for update in updates if not has_correct_order(update, rules)]
incorrect_sorted = [sort_by_rules(update, rules) for update in incorrect]
print(f"Part 2: {sum([u[len(u)//2] for u in incorrect_sorted])}")
