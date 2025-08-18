import collections


def parse_lines(lines: list[str]) -> dict[str, list[str]]:
    m = {}
    for line in lines:
        a, b = line.split(':')
        m[a] = collections.Counter(b.split(','))
    return m


def simulate(start: str, n: int, m: dict[str, list[str]]) -> int:
    counts = collections.Counter([start])

    for _ in range(n):
        counts2 = collections.Counter()
        for c, cnt in counts.items():
            for c2, cnt2 in m[c].items():
                counts2[c2] += cnt * cnt2
        counts = counts2

    return sum(counts.values())


with open("./2024/input/everybody_codes_e2024_q11_p1.txt") as f:
    lines = f.read().splitlines()

m = parse_lines(lines)
answer1 = simulate('A', 4, m)
print(answer1)


# Part 2


with open("./2024/input/everybody_codes_e2024_q11_p2.txt") as f:
    lines = f.read().splitlines()

m = parse_lines(lines)
answer2 = simulate('Z', 10, m)
print(answer2)


# Part 3


with open("./2024/input/everybody_codes_e2024_q11_p3.txt") as f:
    lines = f.read().splitlines()

m = parse_lines(lines)
populations = [simulate(start, 20, m) for start in m]
answer3 = max(populations) - min(populations)
print(answer3)
