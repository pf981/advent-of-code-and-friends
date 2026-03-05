import itertools

with open("./story_3/input/everybody_codes_e3_q02_p2.txt") as f:
    lines = f.read().splitlines()

# lines = """.......
# .......
# .......
# .#.@...
# .......
# .......
# .......""".splitlines()

# source, bones
for r, line in enumerate(lines):
    for c, ch in enumerate(line):
        if ch == "@":
            source = r, c
        if ch == "#":
            bones = r, c

r, c = source
seen = {(r, c)}

max_r = min_r = r
max_c = min_c = c

min_r = min(min_r, bones[0])
max_r = max(max_r, bones[0])
min_c = min(min_c, bones[1])
max_c = max(max_c, bones[1])


def flood_fill(r: int, c: int, visited: set[tuple[int, int]]) -> bool:
    # print(f"{r=} {c=}")
    if (r, c) == bones:
        return True
    if (r, c) in visited:
        return True
    visited.add((r, c))

    if not (min_r <= r <= max_r and min_c <= c <= max_c):
        return False
    if (r, c) in seen:
        return True

    result = (
        flood_fill(r - 1, c, visited)
        and flood_fill(r + 1, c, visited)
        and flood_fill(r, c + 1, visited)
        and flood_fill(r, c - 1, visited)
    )

    # if result:
    #     seen.add((r, c))
    return result


def set_all(r, c):
    # print(f"{r=} {c=} {seen=}")
    if (r, c) in seen or (r, c) == bones:
        return
    seen.add((r, c))
    set_all(r - 1, c)
    set_all(r + 1, c)
    set_all(r, c + 1)
    set_all(r, c - 1)


def p():
    l = []
    for r1 in range(min_r, max_r + 1):
        for c1 in range(min_c, max_c + 1):
            ch = "."
            if (r1, c1) in seen:
                ch = "+"
            if (r1, c1) == (r, c):
                ch = "@"
            if (r1, c1) == bones:
                ch = "#"
            print(ch, end="")
        print()
    with open("test.txt") as f:
        f.write("".join(l))


it = itertools.cycle("NESW")
answer2 = 0
for dir in it:
    # print(f"{answer2=} {r=} {c=} {seen=}")
    r2 = r + (dir == "S") - (dir == "N")
    c2 = c + (dir == "E") - (dir == "W")
    if (r2, c2) in seen or (r2, c2) == bones:
        continue
    seen.add((r2, c2))

    min_r = min(min_r, r2)
    max_r = max(max_r, r2)
    min_c = min(min_c, c2)
    max_c = max(max_c, c2)

    r, c = r2, c2
    answer2 += 1

    # print(f"{answer2=} {r=} {c=} {seen=}")
    # p()
    # if (r - 1, c) in seen and (r + 1, c) in seen:
    #     if flood_fill(r, c - 1, set()):
    #         print(f"Flooded {r=} {c-1=}")
    #     if flood_fill(r, c + 1, set()):
    #         print(f"Flooded {r=} {c+1=}")
    # if (r, c - 1) in seen and (r, c + 1) in seen:
    #     if flood_fill(r - 1, c, set()):
    #         print(f"Flooded {r-1=} {c=}")
    #     if flood_fill(r + 1, c, set()):
    #         print(f"Flooded {r+1=} {c=}")
    if flood_fill(r, c - 1, set()):
        set_all(r, c - 1)
    if flood_fill(r, c + 1, set()):
        set_all(r, c + 1)
    if flood_fill(r - 1, c, set()):
        set_all(r - 1, c)
    if flood_fill(r + 1, c, set()):
        set_all(r + 1, c)

    # print("-------")
    # p()

    # if answer2 == 40:
    #     break
    if (
        (bones[0] - 1, bones[1]) in seen
        and (bones[0] + 1, bones[1]) in seen
        and (bones[0], bones[1] - 1) in seen
        and (bones[0], bones[1] + 1) in seen
    ):
        break

print(answer2)

# 3818
# Your answer length is: correct
# The first character of your answer is: correct
# not 3817 or 3819
