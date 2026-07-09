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

keep = lines[: -400 - 1]
answer1 = "".join(keep).count("o")
print(answer1)
# 402 too high
