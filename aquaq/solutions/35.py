import itertools


def key_to_seq(key: str) -> tuple[int, ...]:
    seq_li = [0] * len(key)
    for val, (_, i) in enumerate(sorted((c, i) for i, c in enumerate(key))):
        seq_li[i] = val

    return tuple(seq_li)


def decrypt_seq(cipher: str, seq: tuple[int, ...]) -> str:
    columns = list(itertools.batched(cipher, len(cipher) // len(seq)))
    columns_shuffled = [columns[i] for i in seq]
    plaintext = "".join(itertools.chain.from_iterable(zip(*columns_shuffled)))

    return plaintext


with open("./input/35.txt") as f:
    text = f.read()


with open("./input/words.txt") as f:
    words_text = f.read()


invalid: set[tuple[int, ...]] = set()
seqs = {}  # seq -> key
for key in words_text.splitlines():
    seq = key_to_seq(key)
    if seq in seqs:
        invalid.add(seq)

    seqs[seq] = key

expect = [
    ". ",
    "! ",
    " for ",
    " I ",
    ", ",
    ' "',
    " of ",
    " with ",
    " that ",
    " my ",
    " to ",
    " has ",
    " had ",
    " not ",
    " at ",
    " once ",
]

cipher = text.rstrip()
bad_starts = set()  # {(word_len, i0), }
candidates = []
for seq, key in seqs.items():
    if (len(seq), seq[0]) in bad_starts:
        continue

    plaintext = decrypt_seq(cipher, seq)
    if not plaintext[0].isupper():
        bad_starts.add((len(seq), seq[0]))
        continue

    for exp in expect:
        if exp not in plaintext:
            break
    else:
        candidates.append((key, plaintext))

assert len(candidates) == 1
answer = candidates[0][0]
print(answer)
