import re


def simplify_roman(roman_numeral: str) -> str:
    substitutions = (
        (r"IIII", "IV"),
        (r"VIV", "IX"),
        (r"XXXX", "XL"),
        (r"LXL", "XC"),
        (r"CCCC", "CD"),
        (r"DCD", "CM"),
    )

    for regex, replace in substitutions:
        roman_numeral = re.sub(regex, replace, roman_numeral)

    return roman_numeral


with open("data/0089_roman.txt") as f:
    text = f.read()

answer = sum(
    len(roman_numeral) - len(simplify_roman(roman_numeral))
    for roman_numeral in text.splitlines()
)
print(answer)
