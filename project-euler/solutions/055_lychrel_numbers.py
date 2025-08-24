def is_palindrome(n: int) -> bool:
    return str(n) == str(n)[::-1]


def is_lychrel(n: int) -> bool:
    palindrom_candidate = n

    for _ in range(50):
        palindrom_candidate += int(str(palindrom_candidate)[::-1])
        if is_palindrome(palindrom_candidate):
            return False

    return True


lychrel_numbers = [n for n in range(10_000) if is_lychrel(n)]
answer = len(lychrel_numbers)
print(answer)
