import itertools

with open("./input/35.txt") as f:
    text = f.read()


def encrypt(plaintext: str, key: str) -> str:
    seq = [i for _, i in sorted((c, i) for i, c in enumerate(key))]
    rows = list(zip(*itertools.batched(plaintext, len(seq))))
    rows_shuffled = [rows[i] for i in seq]
    cipher = "".join(itertools.chain.from_iterable(rows_shuffled))

    return cipher


def decrypt(cipher: str, key: str) -> str:
    seq = [0] * len(key)
    for val, (_, i) in enumerate(sorted((c, i) for i, c in enumerate(key))):
        seq[i] = val

    columns = list(itertools.batched(cipher, len(cipher) // len(seq)))
    columns_shuffled = [columns[i] for i in seq]
    plaintext = "".join(itertools.chain.from_iterable(zip(*columns_shuffled)))

    return plaintext


def decrypt_seq(cipher: str, seq: list[int]) -> str:
    columns = list(itertools.batched(cipher, len(cipher) // len(seq)))
    columns_shuffled = [columns[i] for i in seq]
    plaintext = "".join(itertools.chain.from_iterable(zip(*columns_shuffled)))

    return plaintext


plaintext = "WE ARE DISCOVERED FLEE AT ONCE"
key = "GLASS"
# key = "LEVER"

cipher = encrypt("WE ARE DISCOVERED FLEE AT ONCE", "GLASS")
print(cipher)

plaintext = decrypt(cipher, key)
print(plaintext)
print(decrypt(encrypt("WE ARE DISCOVERED FLEE AT ONCE", "LEVER"), "LEVER"))

# columns = [[] for _ in range(len(seq))]

# for batch in itertools.batched(plaintext, len(seq)):
#     print(batch)


# print(cipher)
# math.comb
# math.perm(10, 10)
# len()

# cipher = encrypt("WE ARE DISCOVERED FLEE AT ONCE", "GLASS")
# cipher = text.rstrip()
# for word_len in range(1, 10):
#     for seq in itertools.permutations(range(word_len)):
#         plaintext = decrypt_seq(cipher, seq)
#         if not plaintext[0].isupper():
#             continue
#         print(f"{''.join(str(i) for i in seq)}:\t{plaintext[:50]}")
# (1, 2, 0, 3, 4)

# May .. your
# My
# someday


# cipher = encrypt("WE ARE DISCOVERED FLEE AT ONCE", "GLASS")

# cipher = text.rstrip().rstrip("#")
# for word_len in range(1, 10):
#     bad_starts = set()
#     for seq in itertools.permutations(range(word_len)):
#         if seq[0] in bad_starts:
#             continue
#         plaintext = decrypt_seq(cipher, seq)
#         if not plaintext[0].isupper():
#             bad_starts.add(seq[0])
#             continue
#         print(f"{''.join(str(i) for i in seq)}:\t{plaintext[:50]}")


# output = []
# cipher = text.rstrip().rstrip("#")
# # for word_len in range(1, 10):
# for word_len in [12]:
#     bad_starts = set()
#     for seq in itertools.permutations(range(word_len)):
#         if seq[0] in bad_starts:
#             continue
#         plaintext = decrypt_seq(cipher, seq)
#         if not plaintext[0].isupper():
#             bad_starts.add(seq[0])
#             continue

#         if " I " not in cipher[:100]:
#             continue
#         # print(f"{''.join(str(i) for i in seq)}:\t{plaintext[:50]}")
#         output.append(plaintext[:50])

# output.sort()
# for line in output:
#     print(line)

# # My journey

with open("./input/words.txt") as f:
    words_text = f.read()

seqs = {}  # seq -> key
for key in words_text.splitlines():
    seq = [0] * len(key)
    for val, (_, i) in enumerate(sorted((c, i) for i, c in enumerate(key))):
        seq[i] = val

    seq = tuple(seq)
    if seq in seqs:
        seqs[seq] = None
    else:
        seqs[seq] = key

seqs = {seq: key for seq, key in seqs.items() if key is not None}
# len(seqs)
# sum(len(s) < 10 for s in seqs)


output = []
cipher = text.rstrip()  # .rstrip("#")
bad_starts = set()  # {(word_len, i0), }
for seq, key in seqs.items():
    if (len(seq), seq[0]) in bad_starts:
        continue
    plaintext = decrypt_seq(cipher, seq)
    if not plaintext[0].isupper():
        bad_starts.add((len(seq), seq[0]))
        continue

    # if " I " not in not[:100]:
    #     continue

    if ". " not in plaintext:
        continue
    if "! " not in plaintext:
        continue
    if " for " not in plaintext:
        continue

    # print(f"{''.join(str(i) for i in seq)}:\t{plaintext[:50]}")
    output.append(f"{plaintext[:50]} -> {key}")

output.sort()
for line in output:
    print(line)

# My daughter
# joy

# Midway upon the journey of our life I found myself
answer = "nonsense"
