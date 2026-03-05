import itertools

with open("./story_3/input/everybody_codes_e3_q02_p3.txt") as f:
    lines = f.read().splitlines()

bones = set()
for r, line in enumerate(lines):
    for c, ch in enumerate(line):
        if ch == "@":
            source = r, c
        if ch == "#":
            bones.add((r, c))

seen = {source}
r, c = source

max_r = min_r = r
max_c = min_c = c

for bone in bones:
    seen.add(bone)
    min_r = min(min_r, bone[0])
    max_r = max(max_r, bone[0])
    min_c = min(min_c, bone[1])
    max_c = max(max_c, bone[1])


def is_enclosed(r: int, c: int, seen: set[tuple[int, int]]) -> bool:
    if (r, c) in seen:
        return True
    seen.add((r, c))

    if not (min_r <= r <= max_r and min_c <= c <= max_c):
        return False

    return (
        is_enclosed(r - 1, c, seen)
        and is_enclosed(r + 1, c, seen)
        and is_enclosed(r, c + 1, seen)
        and is_enclosed(r, c - 1, seen)
    )


def fill(r: int, c: int, seen: set[tuple[int, int]]):
    seen2 = seen.copy()
    if is_enclosed(r, c, seen2):
        seen.update(seen2)


# Some areas start enclosed by bones
for r_bone, c_bone in bones:
    for rr, cc in [
        (r_bone, c_bone - 1),
        (r_bone, c_bone + 1),
        (r_bone - 1, c_bone),
        (r_bone + 1, c_bone),
    ]:
        fill(rr, cc, seen)

it = itertools.cycle("NNNEEESSSWWW")
answer3 = 0
for dir in it:
    r2 = r + (dir == "S") - (dir == "N")
    c2 = c + (dir == "E") - (dir == "W")
    if (r2, c2) in seen:
        continue
    seen.add((r2, c2))

    min_r = min(min_r, r2)
    max_r = max(max_r, r2)
    min_c = min(min_c, c2)
    max_c = max(max_c, c2)

    r, c = r2, c2
    answer3 += 1

    for rr, cc in [(r, c - 1), (r, c + 1), (r - 1, c), (r + 1, c)]:
        fill(rr, cc, seen)

    for bone_r, bone_c in bones:
        for rr, cc in [
            (bone_r, bone_c - 1),
            (bone_r, bone_c + 1),
            (bone_r - 1, bone_c),
            (bone_r + 1, bone_c),
        ]:
            if not ((rr, cc) in seen or (rr, cc) in bones):
                break
        else:
            continue
        break
    else:
        break

print(answer3)
