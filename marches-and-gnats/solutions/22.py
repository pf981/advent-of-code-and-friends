def generate_code() -> str:
    lines = []

    def a(s):
        lines.append(s)

    letters = "abcdefghijklmnopqrstuvwxyz"

    # Append E
    for c in letters + ":":
        a(f"INIT {c} INIT {c} R")
    a("INIT _ SEEK_LEFT E L")

    for c in letters + ":EX":
        a(f"SEEK_LEFT {c} SEEK_LEFT {c} L")
    a("SEEK_LEFT _ POP _ R")

    a("POP : WIPE_RIGHT _ R")  # Finished processing key first
    for c in letters:
        a(f"POP {c} POPPED_{c} _ R")
        for c2 in letters:
            a(f"POPPED_{c} {c2} POPPED_{c} {c2} R")

        a(f"POPPED_{c} : POPPED_NEXT_{c} : R")
        a(f"POPPED_NEXT_{c} X POPPED_NEXT_{c} X R")
        a(f"POPPED_NEXT_{c} E WIPE_LEFT _ L")  # Finished processing cipher first
        for c2 in letters:
            a(
                f"POPPED_NEXT_{c} {c2} APPEND_{letters[(letters.index(c2) - letters.index(c)) % len(letters)]} X R"
            )

        for c2 in letters + "E":
            a(f"APPEND_{c} {c2} APPEND_{c} {c2} R")
        a(f"APPEND_{c} _ SEEK_LEFT {c} L")

    for c in letters + ":X":
        a(f"WIPE_RIGHT {c} WIPE_RIGHT _ R")
    a("WIPE_RIGHT E HALT _ R")

    for c in letters + ":X":
        a(f"WIPE_LEFT {c} WIPE_LEFT _ L")
    a("WIPE_LEFT _ HALT _ R")

    return "\n".join(lines)


if __name__ == "__main__":
    code = generate_code()
    with open("solutions/22.txt", "w", encoding="utf-8") as f:
        f.write(code)
