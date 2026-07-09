with open("./input/2026/04.txt") as f:
    lines = f.read().splitlines()
# lines = """\|/
#  -@-
#  /|\
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
#   |
#   |-o
# #####""".splitlines()

swaps = 0
is_right = True
for line in lines[::-1]:
    if "o" not in line:
        continue
    if line[0] == "o":
        if is_right:
            is_right = False
            swaps += 1
        else:
            pass
    else:
        if not is_right:
            is_right = True
            swaps += 1
        else:
            pass

answer1 = swaps
print(answer1)
