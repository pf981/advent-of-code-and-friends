with open("./2026/input/everybody_codes_e2026_q20_p1.txt") as f:
    lines = f.read().splitlines()

count_segs = {
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
}


answer = 0
for line in lines:
    if eval(line.replace("=", "==")):
        answer += sum(count_segs[c] for c in line)

print(answer)
