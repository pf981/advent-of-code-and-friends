import itertools
import string

with open("./input/23.txt") as f:
    text = f.read()

keyword = "power plant"

seen = {" ", "j"}
r = c = 0
pos_to_ch = {}
ch_to_pos = {}
for ch in keyword + string.ascii_lowercase:
    if ch in seen:
        continue

    pos_to_ch[(r, c)] = ch
    ch_to_pos[ch] = (r, c)

    seen.add(ch)
    c += 1
    if c == 5:
        c = 0
        r += 1

answer = ""
for ch1, ch2 in itertools.batched(text.strip(), 2):
    r1, c1 = ch_to_pos[ch1]
    r2, c2 = ch_to_pos[ch2]

    if r1 == r2:
        answer += pos_to_ch[(r1, (c1 - 1) % 5)]
        answer += pos_to_ch[(r2, (c2 - 1) % 5)]
    elif c1 == c2:
        answer += pos_to_ch[((r1 - 1) % 5, c1)]
        answer += pos_to_ch[((r2 - 1) % 5, c2)]
    else:
        answer += pos_to_ch[(r1, c2)]
        answer += pos_to_ch[(r2, c1)]

print(answer)
