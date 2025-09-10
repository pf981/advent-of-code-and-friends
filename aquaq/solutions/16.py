import itertools

with open("./input/16.txt") as f:
    text = f.read()

with open("./input/asciialphabet.txt") as f:
    ascii_str = f.read()

ascii_letters = list(itertools.batched(ascii_str.splitlines(), 6))
left_gaps = []
right_gaps = []
widths = []
for lines in ascii_letters:
    left_gaps.append([line.index("#") for line in lines])
    right_gaps.append([line[::-1].index("#") for line in lines])
    widths.append(max(len(line) for line in lines))

hash_counts = ["".join(lines).count("#") for lines in ascii_letters]

width = hashes = 0
prev = None
for ch in text.strip():
    i = ord(ch) - ord("A")

    kern = 0
    if prev is not None:
        gaps = [left + right for left, right in zip(left_gaps[i], right_gaps[prev])]
        kern = min(gaps) - 1

    width += widths[i] - kern
    hashes += hash_counts[i]
    prev = i

answer = 6 * width - hashes
print(answer)
