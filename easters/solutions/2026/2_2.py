import itertools
import re
import string
from collections.abc import Generator

with open("./input/2026/2.txt") as f:
    lines = f.read().splitlines()

events = []
for i, line in enumerate(lines):
    for match in re.finditer(r"[^ ]+", line):
        events.append((match.start(), i, match.group()))
events.sort()

MOD = 2**32


def get_hash(s: str, iv: int) -> int:
    for ch in s:
        stacks = [[] for _ in range(len(lines))]
        stacks[0].extend([iv, ord(ch)])

        for _, i, op in events:
            stack = stacks[i]
            match op:
                case " ":
                    continue
                case "dup":
                    out = stack[-1]
                case "+":
                    b = stack.pop()
                    a = stack.pop()
                    out = a + b
                case "-":
                    b = stack.pop()
                    a = stack.pop()
                    out = a - b
                case "*":
                    b = stack.pop()
                    a = stack.pop()
                    out = a * b
                case "%":
                    b = stack.pop()
                    a = stack.pop()
                    out = a % b
                case "xor":
                    b = stack.pop()
                    a = stack.pop()
                    out = a ^ b
                case "or":
                    b = stack.pop()
                    a = stack.pop()
                    out = a | b
                case "v":
                    stacks[i + 1].append(stack.pop())
                    continue
                case "^":
                    stacks[i - 1].append(stack.pop())
                    continue
                case _ if op.isdigit():
                    out = int(op)
                case _:
                    raise ValueError(f"Unknown op: {op!s}")

            stack.append(out % MOD)

        iv = stacks[0].pop()

    return iv


def gen_s() -> Generator[str, None, None]:
    letters = string.digits + string.ascii_lowercase + string.ascii_uppercase

    cur = []

    def gen(length):
        if not length:
            yield "".join(cur)
            return

        for c in letters:
            cur.append(c)
            yield from gen(length - 1)
            cur.pop()

    for length in itertools.count(1):
        yield from gen(length)
    # for length in itertools.count(1):
    #     ...
    # for letter in letters:
    #     yield letter

    # for letter in letters:
    #     for nxt in gen_s():
    #         yield letter + nxt


# it = gen_s()
# for _ in range(1000):
#     print(next(it))

for s in gen_s():
    if get_hash(s, 0) == 1918767294:
        break

answer = s
print(s)
