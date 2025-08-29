def is_valid(password: str) -> bool:
    # a length of at least 4 and at most 12
    if not (4 <= len(password) <= 12):
        return False

    # at least one digit
    if sum(c.isdigit() for c in password) < 1:
        return False

    # at least one uppercase letter (with or without accents, examples: A or Ż)
    if sum(c.isupper() for c in password) < 1:
        return False

    # at least one lowercase letter (with or without accents, examples: a or ŷ)
    if sum(c.islower() for c in password) < 1:
        return False

    # at least one character that is outside the standard 7-bit ASCII character set (examples: Ű, ù or ř)
    if sum(ord(c) > 127 for c in password) < 1:
        return False

    return True


with open("./input/03.txt", encoding="utf-8") as f:
    text = f.read()

answer = sum(is_valid(password) for password in text.splitlines())
print(answer)
