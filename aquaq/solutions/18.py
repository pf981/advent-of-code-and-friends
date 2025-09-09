import itertools


def is_palindrome(h, m, s):
    s = f"{h:>02}:{m:>02}:{s:>02}"
    return s == s[::-1]


with open("./input/18.txt") as f:
    text = f.read()

answer = 0
for line in text.splitlines():
    h, m, s = (int(x) for x in line.split(":"))

    h1, m1, s1 = h2, m2, s2 = h, m, s
    for d in itertools.count():
        if is_palindrome(h1, m1, s1) or is_palindrome(h2, m2, s2):
            break

        s1 += 1
        if s1 == 60:
            s1 = 0
            m1 += 1
            if m1 == 60:
                m1 = 0
                h1 += 1
                if h1 == 24:
                    h1 = 0

        s2 -= 1
        if s2 == -1:
            s2 = 59
            m2 -= 1
            if m2 == -1:
                m2 = 59
                h2 -= 1
                if h2 == -1:
                    h2 = 23
    answer += d

print(answer)
