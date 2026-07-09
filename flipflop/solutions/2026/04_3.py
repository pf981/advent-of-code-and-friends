with open("./input/2026/04.txt") as f:
    lines = f.read().splitlines()
# lines = """\|/
#  -@-
#  /|\\
#   |-o
# o-|
# o-|
#   |-o
#   |
# o-|
#   |-o
#   |-o
# o-|   < CUT
# o-|
#   |
# o-|
# o-|
#   |
# o-|
#   |-o
# #####""".splitlines()

workers = 0
is_right = True
while is_right is not None:
    is_right = None
    last = 0
    last_last = None
    for i in range(len(lines))[::-1]:
        line = lines[i]
        if "o" not in line:
            continue

        if line[0] == "o":
            if is_right is None:
                is_right = False

            if is_right:
                is_right = False
                lines[last_last] = "x"
            else:
                last = i
        else:
            if is_right is None:
                is_right = True

            if not is_right:
                is_right = True
                lines[last_last] = "x"
            else:
                last = i
        last_last = i
    lines[last] = "x"
    if last_last is not None:
        lines[last_last] = "x"
    print("\n".join(lines))
    print()
    print()
    print()
    workers += 1

answer1 = workers - 1
print(answer1)
# 106 incorrect
