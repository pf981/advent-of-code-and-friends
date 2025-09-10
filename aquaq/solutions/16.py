import collections
import itertools
import string

with open("./input/16.txt") as f:
    text = f.read()

text = "LTA"

with open("./input/asciialphabet.txt") as f:
    ascii_str = f.read()

ascii_letters = list(itertools.batched(ascii_str.splitlines(), 6))
lefts = []
rights = []
for lines in ascii_letters:
    lefts.append([line.index("#") for line in lines])
    rights.append([len(line) - 1 - line[::-1].index("#") for line in lines])

hash_counts = ["".join(lines).count("#") for lines in ascii_letters]

# for ch in text
width = hashes = 0
for ch in text:
    i = ord(ch) - ord("A")

    width += 6
    width -= 

    hashes += hash_counts[i]

answer = 6 * width - hashes
print(answer)
