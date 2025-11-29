import collections

with open("./2025/input/everybody_codes_e2025_q20_p3_bonus.txt", encoding="utf8") as f:
    lines = f.read().splitlines()

nrows = len(lines)
ncols = len(lines[0])

m = collections.defaultdict(str)
for r, row in enumerate(lines):
    for c, ch in enumerate(row):
        if ch in "._":
            continue
        m[(r, c)] = ch


def extract_message(r, c):
    words = []
    word = [m[(r, c)]]

    last_move = None

    while m[(r, c)]:
        seen.add((r, c))

        r_start, c_start = r, c

        # Left
        if m[(r, c - 1)] and last_move != "left":
            c -= 1
            word.append(m[(r, c)])
            seen.add((r, c))
            last_move = "left"

        # Down
        if m[(r + 1, c)] and last_move != "right":
            r += 1
            word.append(m[(r, c)])
            seen.add((r, c))
            last_move = "right"

        # elif not m[(r, c - 1)]:
        if (r, c) == (r_start, c_start):
            # # Down Left
            # if not m[(r + 1, c)]:
            r += 1
            c -= 1
            words.append("".join(word))
            word = [m[(r, c)]]

    return " ".join(words)


seen = set()
# extract_message(0, lines[0].index("I"))
# extract_message(4, lines[4].rindex("B"))

messages = []
for r in range(nrows):
    for c in reversed(range(ncols)):
        if not m[(r, c)].isalpha():
            continue

        if (r, c) in seen:
            continue

        messages.append(extract_message(r, c))

for r in range(nrows):
    for c in reversed(range(ncols)):
        ch = lines[r][c]
        if (r, c) in seen:
            ch = "`"
        print(ch, end="")
    print()

print("\n".join(messages))

"""
MAY THE GOLDEN DUCK BE WITH YOU!
SEE YOU AROUND MAY/JUNE
THANKS SO MUCH FOR JOINING IN!

THANKS FOR SHARING YOUR SOLUTIONS,
VISUALISATIONS, AND ALL THE “HOW CAN WE
MAKE THIS FASTER?” DISCUSSIONS!

THANKS TO YOU, I PICKED UP A FEW NEW
TRICKS MYSELF, AND I’LL DEFINITELY
USE THEM IN THE FUTURE!

FOR THE NEXT STORY!
AND CRACKING A FEW PUZZLES ALONG THE WAY

IDKROO
NOW MOST OF YOU DON'T READ THE STORY,

QUACK! QUACK!
EMIL
"""

"""
I KNOW MOST OF YOU DON'T READ THE STORY,
BUT THAT’S HOW THE ORDER OF THE GOLDEN DUCK FROM THE 2024 EVENT CAME TO BE!

THANKS SO MUCH FOR JOINING IN!

I HOPE YOU HAD A GREAT TIME RAISING YOUR DRAGONDUCK
AND CRACKING A FEW PUZZLES ALONG THE WAY
THANKS FOR SHARING YOUR SOLUTIONS,
VISUALISATIONS, AND ALL THE “HOW CAN WE
MAKE THIS FASTER?” DISCUSSIONS!

THANKS TO YOU, I PICKED UP A FEW NEW
TRICKS MYSELF, AND I’LL DEFINITELY
USE THEM IN THE FUTURE!

MAY THE GOLDEN DUCK BE WITH YOU!

SEE YOU AROUND MAY/JUNE
FOR THE NEXT STORY!

QUACK! QUACK!
EMIL
"""
