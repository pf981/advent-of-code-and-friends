def to_roman(num: int) -> str:
    values = [
        ("I", 1),
        ("IV", 4),
        ("V", 5),
        ("IX", 9),
        ("X", 10),
        ("XL", 40),
        ("L", 50),
        ("XC", 90),
        ("C", 100),
        ("CD", 400),
        ("D", 500),
        ("CM", 900),
        ("M", 1000),
    ]

    result = ""
    while num:
        while values[-1][1] > num:
            values.pop()
        result += values[-1][0]
        num -= values[-1][1]

    return result


with open("./input/22.txt") as f:
    text = f.read()

answer = 0
for s in text.split():
    roman = to_roman(int(s))
    for c in roman:
        answer += ord(c) - ord("A") + 1

print(answer)
