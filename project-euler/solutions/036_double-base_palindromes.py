from typing import Generator
import itertools


def gen_binary_palindromes() -> Generator[int]:
    for left in itertools.count(1):
        left_str = f"{left:b}"
        right_str = left_str[::-1]
        yield int(left_str + right_str, 2)
        yield int(left_str + "0" + right_str, 2)
        yield int(left_str + "1" + right_str, 2)


answer = 1
for binary_palindrome in gen_binary_palindromes():
    if binary_palindrome >= 2 * 1_000_000:
        break
    if binary_palindrome >= 1_000_000:
        continue
    s = str(binary_palindrome)
    if s == s[::-1]:
        answer += binary_palindrome
print(answer)
