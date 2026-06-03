with open("./input/2025/02/input1.txt") as f:
    lines = f.read().splitlines()[1:]


def sorter(line):
    parts = line.split(",")
    return int(parts[1]), parts[2], int(parts[3])


lines.sort(key=sorter)
answer = "".join(line[0] for line in lines)
print(answer)
