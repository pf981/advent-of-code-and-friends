import bcrypt
import itertools
import unicodedata

from typing import Literal

with open("./input/10.txt", encoding="utf-8") as f:
    text = f.read()

hashes_str, attempts_str = text.split("\n\n")
hashes = dict(line.split() for line in hashes_str.splitlines())
forms: list[Literal["NFC", "NFD"]] = ["NFC", "NFD"]

answer = 0
for line in attempts_str.splitlines():
    name, attempt = line.split()
    normalised = unicodedata.normalize("NFC", attempt)
    candidates = [
        {unicodedata.normalize(form, c) for form in forms} for c in normalised
    ]
    for candidate in itertools.product(*candidates):
        h = "".join(candidate).encode("utf-8")
        if bcrypt.checkpw(h, hashes[name].encode("utf-8")):
            answer += 1
            break
print(answer)
