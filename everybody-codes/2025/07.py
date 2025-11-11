def is_valid(name: str) -> bool:
    for a, b in zip(name[:-1], name[1:]):
        if b not in instructions[a]:
            return False
    return True


with open("./2025/input/everybody_codes_e2025_q07_p1.txt") as f:
    text = f.read()

names_str, instrs_str = text.split("\n\n")

names = names_str.split(",")
instructions = {}

for line in instrs_str.splitlines():
    a, b = line.split(" > ")
    assert a not in instructions
    instructions[a] = b.split(",")

for name in names:
    if is_valid(name):
        answer1 = name
        break

print(answer1)


# Part 2


with open("./2025/input/everybody_codes_e2025_q07_p2.txt") as f:
    text = f.read()

names_str, instrs_str = text.split("\n\n")

names = names_str.split(",")
instructions = {}

for line in instrs_str.splitlines():
    a, b = line.split(" > ")
    assert a not in instructions
    instructions[a] = b.split(",")

answer2 = sum(i for i, name in enumerate(names, 1) if is_valid(name))
print(answer2)


# Part 3


with open("./2025/input/everybody_codes_e2025_q07_p3.txt") as f:
    text = f.read()

prefixes_str, instrs_str = text.split("\n\n")

prefixes = prefixes_str.split(",")
instructions = {}

for line in instrs_str.splitlines():
    a, b = line.split(" > ")
    assert a not in instructions
    instructions[a] = b.split(",")


cur_name: list[str] = []
all_names: set[str] = set()


def backtrack(prev: str, length: int) -> None:
    if length == 0:
        all_names.add("".join(cur_name))
        return

    if prev not in instructions:
        return

    for nxt in instructions[prev]:
        cur_name.append(nxt)
        backtrack(nxt, length - 1)
        cur_name.pop()


for prefix in prefixes:
    if not is_valid(prefix):
        continue

    for length in range(7 - len(prefix), 11 - len(prefix) + 1):
        cur_name.append(prefix)
        backtrack(prefix[-1], length)
        cur_name.pop()

answer3 = len(all_names)
print(answer3)
