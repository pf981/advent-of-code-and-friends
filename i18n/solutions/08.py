import unicodedata


def is_valid(password: str) -> bool:
    # a length of at least 4 and at most 12
    if not (4 <= len(password) <= 12):
        return False

    # at least one digit
    if not any(c.isdigit() for c in password):
        return False

    decomposed = unicodedata.normalize("NFKD", password)
    normalised = "".join(c for c in decomposed if not unicodedata.combining(c)).lower()

    # at least one accented or unaccented
    # vowel (a, e, i, o, u) (examples: i, Á or ë).
    if all(c not in "aeiou" for c in normalised):
        return False

    # at least one accented or unaccented consonant,
    # examples: s, ñ or ŷ
    if all(c not in "bcdfghjklmnpqrstvwxyz" for c in normalised):
        return False

    # no recurring letters in any form. Ignoring
    # accents and case, letters should not recur.
    # For example, in 'niña' the 'n' occurs twice,
    # one time with accent and one time without.
    # 'Usul' is out because the 'u' occurs twice,
    # first uppercase and then lowercase.
    if len(normalised) != len(set(normalised)):
        return False

    return True


with open("./input/08.txt", encoding="utf-8") as f:
    text = f.read()

answer = sum(is_valid(password) for password in text.splitlines())
print(answer)
