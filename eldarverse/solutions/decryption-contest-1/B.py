import itertools

mask = (1 << 64) - 1
h_start = 0xCBF29CE484222325
for c in "salt":
    h_start ^= ord(c)
    h_start = (h_start * 0x100000001B3) & mask


def fnv_1a(password: tuple[int, int, int, int, int]) -> int:
    h = h_start
    for p in password:
        h ^= p
        h = (h * 0x100000001B3) & mask
    return h


with open("./input/problem-decryption-contest-1-B-input.txt") as f:
    text = f.read()

n, *hashes = text.splitlines()
n = int(n)
hashes = [int(x, 16) for x in hashes]
assert n == len(hashes)

hash_to_password = {}
remaining = set(hashes)
for password in itertools.product(
    [ord(c) for c in "abcdefghijklmnopqrstuvwxyz0123456789"], repeat=5
):
    hash_ = fnv_1a(password)
    if hash_ in remaining:
        hash_to_password[hash_] = "".join(chr(x) for x in password)
        remaining.remove(hash_)

    if not remaining:
        break

output = "Case #1:\n" + "\n".join(hash_to_password[hash_] for hash_ in hashes)

# ~30 seconds to brute force
with open("./output/problem-decryption-contest-1-B.txt", "w") as f:
    f.write(output)
