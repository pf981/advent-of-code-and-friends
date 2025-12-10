from aocd import get_data, submit


def get_min_presses(i, target, buttons):
    if i == len(buttons):
        if all(not t for t in target):
            return 0
        return float("inf")

    # Don't press
    result = get_min_presses(i + 1, target, buttons)

    # Press
    target2 = target.copy()
    for j in buttons[i]:
        target2[j] = not target2[j]
    press = 1 + get_min_presses(i + 1, target2, buttons)

    result = min(result, press)
    return result


inp = get_data(day=10, year=2025)
# inp = """[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
# [...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
# [.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
# """
lines = inp.splitlines()

answer1 = 0
for line in lines:
    target, *buttons, costs = line.split()
    target = [c == "#" for c in target[1:-1]]
    buttons = [[int(x) for x in part[1:-1].split(",")] for part in buttons]
    costs = [int(x) for x in costs[1:-1].split(",")]
    # print(f"{target=} {buttons=} {costs}")
    answer1 += get_min_presses(0, target, buttons)

print(answer1)
submit(answer1, part="a", day=10, year=2025)
