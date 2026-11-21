with open("./2026/input/everybody_codes_e2026_q20_p1.txt") as f:
    lines = f.read().splitlines()

# lines = """5 - 4 = 9 - 8
# 2 + 1 = 3 + 0
# 6 + 7 = 4 + 9
# 1 + 2 = 3 + 4""".splitlines()


def get_segments(c: str) -> int:
    return {
        "0": 6,
        "1": 2,
        "2": 5,
        "3": 5,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 3,
        "8": 7,
        "9": 6,
        "+": 2,
        "-": 1,
        "=": 2,
        " ": 0,
    }[c]


answer = 0
for line in lines:
    if eval(line.replace("=", "==")):
        answer += sum(map(get_segments, line))


print(answer)
