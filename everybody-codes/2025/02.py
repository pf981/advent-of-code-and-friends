import re


def cycle(x: int, y: int, a: int, b: int, denominator: int) -> tuple[int, int]:
    x, y = (x * x - y * y, x * y + y * x)

    x = int(x / denominator)
    y = int(y / denominator)

    x += a
    y += b

    return x, y


with open("./2025/input/everybody_codes_e2025_q02_p1.txt") as f:
    text = f.read()

a, b = (int(s) for s in re.findall(r"-?\d+", text))
x, y = 0, 0
for _ in range(3):
    x, y = cycle(x, y, a, b, 10)

answer1 = f"[{x},{y}]"
print(answer1)


# Part 2


def should_engrave(a: int, b: int) -> bool:
    x, y = 0, 0
    for c in range(100):
        x, y = cycle(x, y, a, b, 100000)

        if not (-1000000 <= x <= 1000000) or not (-1000000 <= y <= 1000000):
            return False

    return True


with open("./2025/input/everybody_codes_e2025_q02_p2.txt") as f:
    text = f.read()

a, b = (int(s) for s in re.findall(r"-?\d+", text))
answer2 = 0
for r in range(101):
    for c in range(101):
        answer2 += should_engrave(a + r * 10, b + c * 10)

print(answer2)


# # Part 3


with open("./2025/input/everybody_codes_e2025_q02_p3.txt") as f:
    text = f.read()


answer3 = 0
for r in range(1001):
    for c in range(1001):
        answer3 += should_engrave(a + r, b + c)
print(answer3)
