import functools


def parse(text: str) -> tuple[list[str], dict[str, list[str]]]:
    names_str, instrs_str = text.split("\n\n")

    names = names_str.split(",")
    instructions = {}

    for line in instrs_str.splitlines():
        a, b = line.split(" > ")
        assert a not in instructions
        instructions[a] = b.split(",")

    return names, instructions


def is_valid(name: str) -> bool:
    for a, b in zip(name[:-1], name[1:]):
        if b not in instructions[a]:
            return False
    return True


with open("./2025/input/everybody_codes_e2025_q07_p1.txt") as f:
    text = f.read()

names, instructions = parse(text)

answer1 = next(name for name in names if is_valid(name))
print(answer1)


# Part 2


with open("./2025/input/everybody_codes_e2025_q07_p2.txt") as f:
    text = f.read()

names, instructions = parse(text)

answer2 = sum(i for i, name in enumerate(names, 1) if is_valid(name))
print(answer2)


# Part 3


@functools.cache
def get_suffixes(prev: str, length: int) -> frozenset[str]:
    # print(f"{prev=} {length=}")
    if length == 0:
        return frozenset([""])

    if prev not in instructions:
        return frozenset()

    result: set[str] = set()
    for c in instructions[prev]:
        suffixes = get_suffixes(c, length - 1)
        # print(f"  {prev=} {length=} {suffixes=}")

        for suffix in suffixes:
            result.add(c + suffix)

    # print(f"  {prev=} {length=} {result=}")
    return frozenset(result)


with open("./2025/input/everybody_codes_e2025_q07_p3.txt") as f:
    text = f.read()


prefixes, instructions = parse(text)

all_names: set[str] = set()
for prefix in prefixes:
    if not is_valid(prefix):
        print(f"Skipping {prefix=}")
        continue

    for length in range(7 - len(prefix), 11 - len(prefix) + 1):
        for suffix in get_suffixes(prefix[-1], length):
            all_names.add(prefix + suffix)

answer3 = len(all_names)
print(answer3)
