import collections

with open("data/day21.txt") as f:
    text = f.read()

parts = text.split("\n\n")

answer = 1
for part in parts:
    valid = set()
    ends = []
    for r, line in enumerate(part.splitlines()):
        for c, ch in enumerate(line):
            match ch:
                case "O":
                    ends.append((r, c))
                case ".":
                    valid.add((r, c))
    valid.add(ends[1])

    assert len(ends) == 2

    q = collections.deque([ends[0]])
    d = 0
    while q:
        for _ in range(len(q)):
            r, c = q.popleft()

            if (r, c) == ends[1]:
                break

            for dr, dc in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                r2 = r + dr
                c2 = c + dc

                if (r2, c2) not in valid:
                    continue
                valid.remove((r2, c2))

                q.append((r2, c2))
        else:
            d += 1
            continue
        break

    answer *= d - 1

print(answer)
