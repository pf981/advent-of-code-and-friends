with open("./input/2025/02/input2.txt") as f:
    lines = f.read().splitlines()
# lines = """000110,c
# 000010,a
# 111100,C
# 111101,A
# 100011,b
# 100110,B""".splitlines()
braille = {
    "100000": "A",
    "110000": "B",
    "100100": "C",
    "100110": "D",
    "100010": "E",
    "110100": "F",
    "110110": "G",
    "110010": "H",
    "010100": "I",
    "010110": "J",
    "101000": "K",
    "111000": "L",
    "101100": "M",
    "101110": "N",
    "101010": "O",
    "111100": "P",
    "111110": "Q",
    "111010": "R",
    "011100": "S",
    "011110": "T",
    "101001": "U",
    "111001": "V",
    "010111": "W",
    "101101": "X",
    "101111": "Y",
    "101011": "Z",
    "000000": " ",
}

cols = []
for line in lines:
    s, c = line.split(",")
    cols.append((c, s))
cols = [s for _, s in sorted(cols)]
rows = ["".join(row) for row in zip(*cols)]

result = []
for r in range(0, len(rows), 3):
    for c in range(0, len(rows[0]), 2):
        s = ""
        for dc in range(2):
            for dr in range(3):
                s += rows[r + dr][c + dc]
        result.append(braille.get(s, s))

answer = "".join(result)
print(answer)
