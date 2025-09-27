import collections
import functools
import math


class HashableCounter(collections.Counter[int]):
    def inc(self, val: int) -> None:
        self[val] += 1

    def dec(self, val: int) -> None:
        if val not in self:
            raise ValueError(f"{val!r} not in HashableCounter {self}")
        self[val] -= 1
        if not self[val]:
            del self[val]

    def __hash__(self):
        return hash(tuple(sorted(self.items())))


def pop_wild(
    wilds: tuple[tuple[int, int], ...], val: int
) -> tuple[tuple[int, int], ...] | None:
    # TODO: Binary search
    for i, (start, end) in enumerate(wilds):
        if start <= val <= end:
            return wilds[:i] + wilds[i + 1 :]

    return None


@functools.cache
def get_differences(
    g: HashableCounter, vals: HashableCounter, wilds: tuple[tuple[int, int], ...]
) -> int | None:
    if not vals and not wilds:
        return 0

    # Wilds only
    if not vals:
        # val1=1, val2=1 is only case where sum > prod
        if 1 in g:
            sum_ = 2
            prod = 1
            val1 = val2 = 1

            g2 = g.copy()

            try:
                g2.dec(sum_)
                g2.dec(prod)
            except ValueError:
                return None

            wilds2 = pop_wild(wilds, val1)
            if wilds2 is None:
                return None

            wilds2 = pop_wild(wilds, val2)
            if wilds2 is None:
                return None

            return get_differences(g2, vals, wilds2)
        else:
            prod = max(g)

            g2 = g.copy()
            g2.dec(prod)

            for val1 in range(1, math.isqrt(prod) + 1):
                if val1 % prod:
                    continue

                val2 = prod // val1
                sum_ = val1 + val2

                if sum_ not in g2:
                    continue

                wilds2 = pop_wild(wilds, val1)
                if wilds2 is None:
                    continue

                wilds2 = pop_wild(wilds, val2)
                if wilds2 is None:
                    continue

                result = get_differences(g2, vals, wilds2)
                if result is not None:
                    return result

            return None
        raise NotImplementedError("Wilds only not yet implemented")

    val1 = next(iter(vals))
    vals2 = vals.copy()
    vals2.dec(val1)
    g2 = g.copy()

    for sum_ in g:
        val2 = sum_ - val1
        prod = val1 + val2

        if prod not in g:
            continue

        used_wild = False
        wilds2 = wilds
        if val2 not in vals2:
            popped_wilds = pop_wild(wilds2, val2)
            if popped_wilds is None:
                continue
            wilds2 = popped_wilds
        else:
            vals2.dec(val2)

        result = get_differences(g2, vals2, wilds2)
        if result is not None:
            return abs(val2 - val1) + result

        if not used_wild:
            vals2.inc(val2)

    return None


def parse(
    part: str,
) -> tuple[HashableCounter, HashableCounter, tuple[tuple[int, int], ...]]:
    g_str, i_str = part.splitlines()

    g = HashableCounter(int(s) for s in g_str[2:].split())
    vals = HashableCounter()
    wilds = []

    prev = 0
    for s in i_str[2:].split():
        if s == "*":
            wilds.append((prev, -1))
        else:
            val = int(s)
            vals.inc(val)

            for i in range(len(wilds)):
                if wilds[i][1] == -1:
                    wilds[i] = (wilds[i][0], val)

            prev = val

    max_g = max(g)
    for i in range(len(wilds)):
        if wilds[i][1] == -1:
            wilds[i] = (wilds[i][0], max_g)

    return g, vals, tuple(wilds)


with open("./input/36.txt") as f:
    text = f.read()

# text = """g:252 260 13 30 25 144 36 30 48 21 40 30 224 56 46 22
# i:* 2 2 5 6 6 8 10 14 16 21 23 24 26 28 42"""
# text = """g:252 260 13 30 25 144 36 30 48 21 40 30 224 56 46 22
# i:1 2 2 5 6 6 8 10 14 16 21 23 24 26 28 42"""

answer = 0
for part in text.split("\n\n"):
    g, vals, wilds = parse(part)
    # print(f"{g=} {vals=} {wilds=}")

    differences = get_differences(g, vals, wilds)
    assert differences is not None
    answer += differences

print(answer)
