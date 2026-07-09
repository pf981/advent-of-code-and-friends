with open("./input/2026/04.txt") as f:
    lines = f.read().splitlines()

workers = 0
while True:
    last = is_right = None
    for i in reversed(range(len(lines))):
        line = lines[i]
        if "o" not in line:
            continue

        if line[0] == "o":
            if is_right is None:
                is_right = False

            if is_right:
                is_right = False
                lines[last] = "x"
        else:
            if is_right is None:
                is_right = True

            if not is_right:
                is_right = True
                lines[last] = "x"
        last = i

    if last is None:
        break

    lines[last] = "x"
    workers += 1

answer3 = workers
print(answer3)
