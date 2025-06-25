import itertools

import downloader


def vigenere_cipher(
    cipher: str, key_string: str, alphabet: str, decode: bool = False
) -> str:
    s1, s2 = cipher, key_string
    if len(s2) > len(s1):
        s1, s2 = s2, s1

    if not s2:
        return s1

    c_to_index = {c: i for i, c in enumerate(alphabet)}
    nums1, nums2 = [[c_to_index.get(c, c) for c in s] for s in [s1, s2]]

    n = len(alphabet)
    result = []
    for a, b in zip(nums1, itertools.cycle(nums2)):
        if isinstance(a, str):
            result.append(a)
        elif isinstance(b, str):
            result.append(b)
        else:
            if decode:
                result.append(alphabet[(a - (b + 1)) % n])
            else:
                result.append(alphabet[(a + b + 1) % n])

    return "".join(result)


text = downloader.get_puzzle(8)

decoded = vigenere_cipher(
    cipher=text,
    key_string="Roads? Where We're Going, We Don't Need Roads.",
    alphabet="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.,;:?! '()",
    decode=True,
)
print(decoded)

answer = "codingquest2022"
print(answer)
