from aocd import get_data, submit
import copy
import functools


@functools.cache
def get_min_presses(i, target, buttons):
    # print(f"{i=} {target=} {buttons=}")
    if i == len(buttons):
        if all(not t for t in target):
            return 0
        return float("inf")

    # Don't press
    result = get_min_presses(i + 1, target, buttons)

    # Press
    joltage2 = list(target)
    press = float("inf")
    for press_count in range(1, 200):
        for j in buttons[i]:
            joltage2[j] -= 1
            if joltage2[j] < 0:
                # if i == 0:
                #     print(f"Stopping i=0 at {press_count=} {joltage2=} {joltage2[i]=}")
                break
        else:
            press = min(
                press, press_count + get_min_presses(i + 1, tuple(joltage2), buttons)
            )
            continue
        break

    result = min(result, press)
    return result


inp = get_data(day=10, year=2025)
# inp = """[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
# [...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
# [.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
# """
# inp = """[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
# """
lines = inp.splitlines()

answer2 = 0
for line in lines:
    target, *buttons, costs = line.split()
    target = [c == "#" for c in target[1:-1]]
    buttons = [[int(x) for x in part[1:-1].split(",")] for part in buttons]
    joltage = [int(x) for x in costs[1:-1].split(",")]
    # print(f"{target=} {buttons=} {costs}")
    answer2 += get_min_presses(0, tuple(joltage), tuple(tuple(b) for b in buttons))

print(answer2)
submit(answer2, part="b", day=10, year=2025)
