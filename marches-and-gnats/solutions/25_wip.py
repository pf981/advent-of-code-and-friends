import collections
import itertools
from typing import Any


def int_to_french(n: int) -> str:
    units = [
        "",
        "un",
        "deux",
        "trois",
        "quatre",
        "cinq",
        "six",
        "sept",
        "huit",
        "neuf",
    ]
    teens = ["dix", "onze", "douze", "treize", "quatorze", "quinze", "seize"]
    tens = ["", "dix", "vingt", "trente", "quarante", "cinquante", "soixante"]

    def under_hundred(x: int) -> str:
        if x < 10:
            return units[x]
        if 10 <= x <= 16:
            return teens[x - 10]
        if 17 <= x <= 19:
            return "dix-" + units[x - 10]
        if 20 <= x <= 69:
            q, r = divmod(x, 10)
            if r == 1:
                return tens[q] + "-et-un"
            return tens[q] + "-" + units[r] if r else tens[q]
        if 70 <= x <= 79:
            return under_hundred(60) + "-" + under_hundred(x - 60)
        if 80 <= x <= 99:
            return (
                "quatre-vingts" if x == 80 else "quatre-vingt-" + under_hundred(x - 80)
            )
        raise ValueError(f"Number out of range for under_hundred: {x} (must be 0–99)")

    def under_thousand(x: int) -> str:
        h, r = divmod(x, 100)
        prefix = "" if h == 0 else ("cent" if h == 1 else units[h] + "-cent")
        return (
            prefix
            if r == 0
            else prefix + "-" + under_hundred(r)
            if prefix
            else under_hundred(r)
        )

    m, r = divmod(n, 1000)
    prefix = "" if m == 0 else ("mille" if m == 1 else units[m] + "-mille")
    if r == 0:
        return prefix
    return prefix + "-" + under_thousand(r) if prefix else under_thousand(r)


l = []
for num in range(1, 1101):
    l.append((int_to_french(num), num))

l.sort()
print("\n".join(f"{a}\t{b}" for a, b in l))


firsts = collections.defaultdict(list)
for french, num in l:
    digit1 = str(num)[0]
    part1 = french.split("-")[0]
    firsts[digit1].append(part1)

for digit1 in sorted(firsts):
    print(
        f"{digit1}:\t{' '.join(sorted(f'{s}({collections.Counter(firsts[digit1])[s]})' for s in set(firsts[digit1])))}"
    )

trie: Any = {}

for num in range(1, 1101):
    print(num, int_to_french(num))

for num in range(1, 1101):
    # for num in range(1, 11):
    # for num in range(1, 2):
    # for num in range(14, 16):
    # for num in range(1, 100):
    # for num in [21, 22]:
    # for num in [21]:
    node = trie
    for c in int_to_french(num):
        c = c.replace(" ", "-")  # TEST?
        node[c] = node.get(c, {})
        node[None] = node.get(None, [])
        node[None].append(num)
        node = node[c]
    node[None] = [num]


def get_only_path(node: Any) -> str:
    result = []
    while node:
        if len(node) == 1:
            break
        assert len(node[None]) == 1
        c = next(ch for ch in node if ch is not None)
        result.append(c)
        node = node[c]

    return "".join(result)


# get_only_path(trie["q"]["u"]["a"])

rules = set()


def dfs(node: Any, prefix: str | None) -> bool:
    if len(node[None]) == 1:
        answer = str(node[None][0])
        prefix = prefix or "INIT"
        state = prefix
        for i, (c_in, c_out) in enumerate(
            itertools.zip_longest(get_only_path(node), answer)
        ):
            c_in = c_in or "_"
            c_out = c_out or "_"

            next_state = answer if state == prefix else state[1:]
            if not next_state:
                next_state = "WIPE"
                # c_out = "_"

            rules.add(f"{state} {c_in} {next_state} {c_out} R")
            # prefix += c_in
            state = next_state

        # rules.add(f"{state} _ HALT _ R")

        return True

    for c in node:
        if c is None:
            continue
        state = prefix or "INIT"
        next_state = prefix + c.replace(" ", "_")
        dfs(node[c], next_state)
        rules.add(f"{state} {c} {next_state} _ R")
    return False


dfs(trie, "")
# rules.add("INIT | HALT | R")  # DEBUG
rules.add("WIPE _ HALT _ R")  # DEBUG
code = "\n".join(sorted(rules))
with open("solutions/25.txt", "w", encoding="utf-8") as f:
    f.write(code)
# for res in result:
#     print(res)


# def generate_code() -> str:
#     lines = []

#     def a(s):
#         lines.append(s)

#     return "\n".join(lines)


# if __name__ == "__main__":
#     code = generate_code()
#     with open("solutions/25.txt", "w", encoding="utf-8") as f:
#         f.write(code)
