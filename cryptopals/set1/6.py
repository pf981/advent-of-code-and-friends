import base64
import collections
import itertools

with open("./data/6.txt") as f:
    text = f.read()


# https://pi.math.cornell.edu/~mec/2003-2004/cryptography/subs/frequencies.html
target_counts = {
    " ": 21912 * 2,
    "E": 21912,
    "T": 16587,
    "A": 14810,
    "O": 14003,
    "I": 13318,
    "N": 12666,
    "S": 11450,
    "R": 10977,
    "H": 10795,
    "D": 7874,
    "L": 7253,
    "U": 5246,
    "C": 4943,
    "M": 4761,
    "F": 4200,
    "Y": 3853,
    "W": 3819,
    "G": 3693,
    "P": 3316,
    "B": 2715,
    "V": 2019,
    "K": 1257,
    "X": 315,
    "Q": 205,
    "J": 188,
    "Z": 128,
}
target_total = sum(target_counts.values())
target_freqs: collections.defaultdict[str, float] = collections.defaultdict(
    float, {c: count / target_total for c, count in target_counts.items()}
)


def score(text: str) -> float:
    freqs: collections.defaultdict[str, float] = collections.defaultdict(float)
    for c in text.upper():
        freqs[c] += 1
    total = sum(freqs.values())
    for c in freqs:
        freqs[c] = freqs[c] / total

    score = 0.0
    for c in set(freqs) | set(target_freqs):
        score += abs(freqs[c] - target_freqs[c])

    return score


def break_single_byte_xor(cipher: bytes) -> tuple[float, int, str]:
    result = []
    for xor in range(256):
        plaintext = bytes(xor ^ c for c in cipher).decode(
            encoding="utf-8", errors="replace"
        )
        result.append((score(plaintext), xor, plaintext))

    return min(result)


def repeating_key_xor(cipher: bytes, key: bytes) -> str:
    plaintext = bytes(k ^ c for k, c in zip(itertools.cycle(key), cipher)).decode()
    return plaintext


def hamming_dist(s1: bytes, s2: bytes) -> int:
    return sum(
        (a ^ b).bit_count() for a, b in itertools.zip_longest(s1, s2, fillvalue=0)
    )


assert hamming_dist("this is a test".encode(), "wokka wokka!!!".encode()) == 37

data = base64.b64decode(text)
best_d = float("inf")
best_keysize = 0
for keysize in range(2, 41):
    block1 = data[:keysize]
    block2 = data[keysize : 2 * keysize]

    d = hamming_dist(block1, block2) / keysize
    if d < best_d:
        best_d = d
        best_keysize = keysize

rows = list(itertools.batched(data, best_keysize))
transposed = list(itertools.zip_longest(*rows, fillvalue=0))

repeating_key = bytes(break_single_byte_xor(bytes(line))[1] for line in transposed)
# for line in transposed:
#     print(break_single_byte_xor(bytes(line)))
repeating_key_xor(data, repeating_key)
