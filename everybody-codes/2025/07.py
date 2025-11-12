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
def count_ways(prev: str, length: int) -> int | None:
    if length == 0:
        return 1

    if prev not in instructions:
        return None

    ways = None
    for c in instructions[prev]:
        result = count_ways(c, length - 1)
        if result is not None:
            if ways is None:
                ways = 0
            ways += result

    return ways


with open("./2025/input/everybody_codes_e2025_q07_p3.txt") as f:
    text = f.read()


prefixes, instructions = parse(text)

# If two strings share a prefix, keep only the shortest
# to prevent double-counting
prefixes.sort(key=len, reverse=True)
final_prefixes = []
for i in range(len(prefixes)):
    for j in range(i + 1, len(prefixes)):
        if prefixes[i].startswith(prefixes[j]):
            break
    else:
        final_prefixes.append(prefixes[i])

answer3 = 0
for prefix in final_prefixes:
    if not is_valid(prefix):
        continue

    for length in range(7 - len(prefix), 11 - len(prefix) + 1):
        result = count_ways(prefix[-1], length)
        if result is not None:
            answer3 += result

print(answer3)
