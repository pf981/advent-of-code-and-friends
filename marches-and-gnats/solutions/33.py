def generate_code() -> str:
    lines = []

    def a(s):
        lines.append(s)

    opens = "([{"
    closes = ")]}"
    parens = opens + closes
    open_close = list(zip(opens, closes))

    for op, cl in open_close:
        a(f"INIT {op} MATCH{cl} {op} R")
        a(f"INIT {cl} WIPE_RIGHT N R")

        a(f"MATCH{cl} X MATCH{cl} X R")
        a(f"MATCH{cl} {cl} X_THEN_SEEK_LEFT X L")

        for op2, cl2 in open_close:
            a(f"MATCH{cl} {op2} MATCH{cl2} {op2} R")
            if cl2 == cl:
                continue
            a(f"MATCH{cl} {cl2} NEXT {cl2} R")

        a(f"MATCH{cl} _ WIPE_LEFT N L")

    a("X_THEN_SEEK_LEFT X X_THEN_SEEK_LEFT X L")
    for op in opens:
        a(f"X_THEN_SEEK_LEFT {op} SEEK_LEFT X L")

    for c in parens + "X":
        a(f"SEEK_LEFT {c} SEEK_LEFT {c} L")
    a("SEEK_LEFT _ NEXT _ R")

    for c in closes + "X":
        a(f"NEXT {c} NEXT {c} R")
    for op, cl in open_close:
        a(f"NEXT {op} MATCH{cl} {op} R")

    a("NEXT _ CHECK_EMPTY_LEFT _ L")
    a("CHECK_EMPTY_LEFT X CHECK_EMPTY_LEFT _ L")
    a("CHECK_EMPTY_LEFT _ HALT Y L")
    for c in parens:
        a(f"CHECK_EMPTY_LEFT {c} WIPE_LEFT N L")

    for c in parens + "X":
        a(f"WIPE_RIGHT {c} WIPE_RIGHT _ R")
        a(f"WIPE_LEFT {c} WIPE_LEFT _ L")
    a("WIPE_RIGHT _ HALT _ R")
    a("WIPE_LEFT _ HALT _ L")

    return "\n".join(lines)


if __name__ == "__main__":
    code = generate_code()
    with open("solutions/33.txt", "w", encoding="utf-8") as f:
        f.write(code)
