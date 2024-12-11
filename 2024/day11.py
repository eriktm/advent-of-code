from functools import lru_cache


@lru_cache(None)
def blink_calc(item, blinks=0, limit=25):
    if blinks == limit:
        return 1

    if item == 0:
        return blink_calc(1, blinks + 1, limit)

    s = str(item)
    sl = len(s)

    if sl % 2 == 0:
        return blink_calc(int(s[: sl // 2]), blinks + 1, limit) + blink_calc(
            int(s[sl // 2 :]), blinks + 1, limit
        )

    return blink_calc(item * 2024, blinks + 1, limit)


def expand_stones(ints, limit):
    answer = 0
    for i in ints:
        answer += blink_calc(i, limit=limit)

    return answer


with open("input/day11.txt", "r") as f:
    data = list(map(int, f.read().split()))

print(f"Part 1: {expand_stones(data, 25)}")
print(f"Part 2: {expand_stones(data, 75)}")
