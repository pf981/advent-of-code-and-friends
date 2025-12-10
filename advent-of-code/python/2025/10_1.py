from aocd import get_data, submit


def get_min_presses(i, target, buttons):
    if i == len(buttons):
        if all(not t for t in target):
            return 0
        return float("inf")

    # Don't press
    dont_press = get_min_presses(i + 1, target, buttons)

    # Press
    target2 = target.copy()
    for j in buttons[i]:
        target2[j] = not target2[j]
    press = 1 + get_min_presses(i + 1, target2, buttons)

    return min(dont_press, press)


inp = get_data(day=10, year=2025)
lines = inp.splitlines()

answer1 = 0
for line in lines:
    target, *buttons, joltages = line.split()
    target = [c == "#" for c in target[1:-1]]
    buttons = [[int(x) for x in part[1:-1].split(",")] for part in buttons]
    joltages = [int(x) for x in joltages[1:-1].split(",")]

    answer1 += get_min_presses(0, target, buttons)

submit(answer1, part="a", day=10, year=2025)
