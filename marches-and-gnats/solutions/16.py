def generate_code() -> str:
    lines = []

    def a(s):
        lines.append(s)

    letters = "IVXLCDM"
    subtractive = {"I": {"V", "X"}, "X": {"L", "C"}, "C": {"D", "M"}}
    m = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    for c in letters:
        if c in subtractive:
            a(f"INIT {c} CHECK_SUB_{c} _ R")
            if c == "I":
                a(f"CHECK_SUB_{c} _ HALT | R")
            else:
                a(f"CHECK_SUB_{c} _ APPEND_{m[c] - 1} | R")
            a(f"CHECK_SUB_{c} | APPEND_{m[c]} | R")
            for c2 in letters:
                if c2 in subtractive[c]:
                    a(f"CHECK_SUB_{c} {c2} APPEND_{m[c2] - m[c]} _ R")
                else:
                    a(f"CHECK_SUB_{c} {c2} APPEND_{m[c]} {c2} R")
        else:
            a(f"INIT {c} APPEND_{m[c]} _ R")
    for n in range(1, 1001):
        for c in letters + "|":
            a(f"APPEND_{n} {c} APPEND_{n} {c} R")

        if n == 1:
            a(f"APPEND_{n} _ SEEK_LEFT | L")
        else:
            a(f"APPEND_{n} _ APPEND_{n - 1} | R")

    for c in letters + "|":
        a(f"SEEK_LEFT {c} SEEK_LEFT {c} L")
    a("SEEK_LEFT _ INIT _ R")
    a("INIT | HALT | R")

    return "\n".join(lines)


if __name__ == "__main__":
    code = generate_code()
    with open("solutions/16.txt", "w", encoding="utf-8") as f:
        f.write(code)
