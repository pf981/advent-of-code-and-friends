import collections


with open("./2025/input/everybody_codes_e2025_q06_p1.txt") as f:
    text = f.read().strip()

answer1 = 0
mentors = 0
for c in text:
    if c == "A":
        mentors += 1
    elif c == "a":
        answer1 += mentors

print(answer1)


# Part 2


with open("./2025/input/everybody_codes_e2025_q06_p2.txt") as f:
    text = f.read().strip()

answer2 = 0
mentors = collections.Counter()
for c in text:
    if c.isupper():
        mentors[c] += 1
    else:
        answer2 += mentors[c.upper()]

print(answer2)


# Part 3


def count_left_to_right(text: str, max_dist: int) -> int:
    result = 0
    mentors = collections.defaultdict(collections.deque)
    for i, c in enumerate(text):
        if c.isupper():
            mentors[c].append(i)
        else:
            q = mentors[c.upper()]
            while q and q[0] < i - max_dist:
                q.popleft()
            result += len(q)

    return result


with open("./2025/input/everybody_codes_e2025_q06_p3.txt") as f:
    text = f.read().strip()
times = 1000
max_dist = 1000

text = text * times
answer3 = count_left_to_right(text, max_dist) + count_left_to_right(
    text[::-1], max_dist
)

print(answer3)
