with open("./input/2026/04.txt") as f:
    lines = f.read().splitlines()

answer1 = "".join(lines[: -400 - 1]).count("o")
print(answer1)
