import itertools

with open("./story_3/input/everybody_codes_e3_q02_p3.txt") as f:
    lines = f.read().splitlines()


# lines = """#..#.......#...
# ...#...........
# ...#...........
# #######........
# ...#....#######
# ...#...@...#...
# ...#.......#...
# ...........#...
# ...........#...
# #..........#...
# ##......#######""".splitlines()

# source, bones
bones = set()
for r, line in enumerate(lines):
    for c, ch in enumerate(line):
        if ch == "@":
            source = r, c
        if ch == "#":
            bones.add((r, c))

r, c = source
seen = {(r, c)}

max_r = min_r = r
max_c = min_c = c

for bone in bones:
    min_r = min(min_r, bone[0])
    max_r = max(max_r, bone[0])
    min_c = min(min_c, bone[1])
    max_c = max(max_c, bone[1])


def flood_fill(r: int, c: int, visited: set[tuple[int, int]]) -> bool:
    # print(f"Flood {r=} {c=} {seen=}")
    # print(f"{r=} {c=}")
    if (r, c) in bones:
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
    # print(f"set_all {r=} {c=} {seen=}")
    if (r, c) in seen or (r, c) in bones:
        return
    seen.add((r, c))
    set_all(r - 1, c)
    set_all(r + 1, c)
    set_all(r, c + 1)
    set_all(r, c - 1)


def p():
    for r1 in range(min_r, max_r + 1):
        for c1 in range(min_c, max_c + 1):
            ch = "."
            if (r1, c1) in seen:
                ch = "+"
            if (r1, c1) == (r, c):
                ch = "@"
            if (r1, c1) in bones:
                ch = "#"
            print(ch, end="")
        print()


# Fill in enclosed areas
for rr, cc in bones:
    if flood_fill(rr, cc - 1, set()):
        set_all(rr, cc - 1)
    if flood_fill(rr, cc + 1, set()):
        set_all(rr, cc + 1)
    if flood_fill(rr - 1, cc, set()):
        set_all(rr - 1, cc)
    if flood_fill(rr + 1, cc, set()):
        set_all(rr + 1, cc)

it = itertools.cycle("NNNEEESSSWWW")
answer3 = 0
for dir in it:
    # print(f"{answer2=} {r=} {c=} {seen=}")
    r2 = r + (dir == "S") - (dir == "N")
    c2 = c + (dir == "E") - (dir == "W")
    if (r2, c2) in seen or (r2, c2) in bones:
        continue
    seen.add((r2, c2))

    min_r = min(min_r, r2)
    max_r = max(max_r, r2)
    min_c = min(min_c, c2)
    max_c = max(max_c, c2)

    r, c = r2, c2
    answer3 += 1

    # print(f"{answer3=} {r=} {c=} {seen=}")
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

    # print(f"--- {answer3} ---")
    print(answer3)
    # p()
    # if answer3 >= 10:  # FIXME: REMOVE
    #     break

    for bone in bones:
        if not (
            ((bone[0] - 1, bone[1]) in seen or (bone[0] - 1, bone[1]) in bones)
            and ((bone[0] + 1, bone[1]) in seen or (bone[0] + 1, bone[1]) in bones)
            and ((bone[0], bone[1] - 1) in seen or (bone[0], bone[1] - 1) in bones)
            and ((bone[0], bone[1] + 1) in seen or (bone[0], bone[1] + 1) in bones)
        ):
            break
    else:
        break

print(answer3)
