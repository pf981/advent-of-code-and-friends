def generate_code() -> str:
    lines = []

    def a(s):
        lines.append(s)

    letters = "abcdef"

    for c in letters:
        a(f"INIT {c} SEEK_RIGHT_{c} _ R")

        for c2 in letters:
            a(f"SEEK_RIGHT_{c} {c2} SEEK_RIGHT_{c} {c2} R")

        a(f"SEEK_RIGHT_{c} _ POP_{c} _ L")
        a(f"POP_{c} {c} SEEK_LEFT _ L")
        a(f"POP_{c} _ HALT Y L")  # Odd

        for c2 in letters:
            if c != c2:
                a(f"POP_{c} {c2} WIPE_LEFT_N _ L")
        a(f"SEEK_LEFT {c} SEEK_LEFT {c} L")

    a("SEEK_LEFT _ INIT _ R")
    a("INIT _ HALT Y R")

    for c in letters:
        a(f"WIPE_LEFT_N {c} WIPE_LEFT_N _ L")
    a("WIPE_LEFT_N _ HALT N L")

    return "\n".join(lines)


if __name__ == "__main__":
    code = generate_code()
    with open("solutions/30.txt", "w", encoding="utf-8") as f:
        f.write(code)
