def generate_code() -> str:
    lines = []

    def a(s):
        lines.append(s)

    a("INIT | PLACE_COMMA | L")
    a("PLACE_COMMA _ NEXT , L")
    a("NEXT _ APPEND_LAST | R")

    a("APPEND_LAST X APPEND_LAST | R")
    a("APPEND_LAST , APPEND_LAST , R")
    a("APPEND_LAST Y APPEND_LAST Y R")
    a("APPEND_LAST | CHECK_DONE Y R")

    a("CHECK_DONE _ CLEANUP _ L")
    a("CLEANUP Y CLEANUP _ L")
    a("CLEANUP , CLEANUP _ L")
    a("CLEANUP | HALT | L")

    a("CHECK_DONE | NEXT | L")

    a("NEXT X NEXT X L")
    a("NEXT Y NEXT Y L")
    a("NEXT , NEXT , L")

    a("NEXT | ACC_2 X L")

    max_accumulate = 256
    for i in range(2, max_accumulate, 2):
        a(f"ACC_{i} | ACC_{i + 2} X L")
        a(f"ACC_{i} _ APPEND_{i} _ R")

    a(f"ACC_{max_accumulate} | APPEND_{max_accumulate} | R")

    for i in range(2, max_accumulate + 1, 2):
        for c in "X,Y":
            a(f"APPEND_{i} {c} APPEND_{i} {c} R")

    for i in range(2, max_accumulate + 1):
        a(f"APPEND_{i} | APPEND_{i - 1} Y R")
    a("APPEND_1 | NEXT Y L")

    return "\n".join(lines)


if __name__ == "__main__":
    code = generate_code()
    with open("solutions/15.txt", "w", encoding="utf-8") as f:
        f.write(code)
