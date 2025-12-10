from aocd import get_data, submit
import z3


def get_min_presses(i, target, buttons):
    o = z3.Optimize()

    presses = [z3.Int(f"press_{i}") for i in range(len(buttons))]
    for p in presses:
        o.add(p >= 0)

    for i, t in enumerate(target):
        eq = 0
        for btn, jolt_is in enumerate(buttons):
            if i not in jolt_is:
                continue
            eq = presses[btn] + eq
        o.add(eq == t)

    output = z3.Int("output")
    o.add(output == z3.Sum(presses))
    o.minimize(output)

    res = o.check()
    assert res == z3.sat

    return o.model()[output].py_value()


inp = get_data(day=10, year=2025)
lines = inp.splitlines()

answer2 = 0
for line in lines:
    target, *buttons, joltages = line.split()
    target = [c == "#" for c in target[1:-1]]
    buttons = [[int(x) for x in part[1:-1].split(",")] for part in buttons]
    joltages = [int(x) for x in joltages[1:-1].split(",")]

    answer2 += get_min_presses(0, tuple(joltages), tuple(tuple(b) for b in buttons))

submit(answer2, part="b", day=10, year=2025)
