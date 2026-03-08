def generate_code() -> str:
    lines = []
    letters = "abcdefgh"
    nums = "12345678"
    ext_letters = "abcdefghijklmno"
    ext_nums = "1234567890αβγδε"

    def a(s: str) -> None:
        lines.append(s)

    def bishop_sum(x: str, y: int) -> str:
        return ext_letters[letters.index(x) + nums.index(y)]

    def bishop_diff(x: str, y: int) -> str:
        return ext_nums[letters.index(x) - nums.index(y) + 7]

    a("INIT K INIT _ R")
    for kx in ext_letters:
        a(f"INIT {kx} {kx} {kx} R")
        a(f"{kx} , {kx} , R")
        for ky in ext_nums:
            a(f"{kx} {ky} {kx} {ky} R")

    # --- Rook ---
    for kx in ext_letters:
        a(f"{kx} R ROOK_{kx} R R")
        a(f"{kx} Q ROOK_{kx} Q R")
        for px in ext_letters:
            if kx == px:
                a(f"ROOK_{kx} {px} FINISH_Y {px} R")
            else:
                # kx != px. Check py next.
                a(f"ROOK_{kx} {px} ROOK {px} R")

    for py in ext_nums:
        a(f"ROOK {py} ROOK_{py} {py} L")
        for px in ext_letters:
            a(f"ROOK_{py} {px} ROOK_{py} {px} L")
        a(f"ROOK_{py} , ROOK_{py} , L")
        a(f"ROOK_{py} R ROOK_{py} R L")
        a(f"ROOK_{py} Q ROOK_{py} Q L")
        for ky in ext_nums:
            if py == ky:
                a(f"ROOK_{py} {ky} FINISH_Y {ky} R")
            else:
                a(f"ROOK_{py} {ky} FINISH_N_IF_NOT_QUEEN {ky} R")

    a("FINISH_N_IF_NOT_QUEEN , FINISH_N_IF_NOT_QUEEN , R")
    a("FINISH_N_IF_NOT_QUEEN R FINISH_N R R")

    # If we do not have a rook-check and the piece is a queen, convert to a bishop
    # "ROOKIFY" will just go to the left and restart
    a("FINISH_N_IF_NOT_QUEEN Q ROOKIFY B L")

    # --- Bishop ---
    # Convert kx to represent positive diagonal, ky to be negative, and same for px, py
    # Then change "B" to "R" and treat it as a rook comparison
    for kx in letters:
        a(f"{kx} B BISHOP_{kx} B L")
        a(f"BISHOP_{kx} , BISHOP_{kx} , L")
        for ky in nums:
            bs = bishop_sum(kx, ky)
            a(f"BISHOP_{kx} {ky} BISHOP_SUM_{bs} {bishop_diff(kx, ky)} L")
            a(f"BISHOP_SUM_{bs} {kx} BISHOP_GOTO_RHS {bs} R")

    for bd in ext_nums:
        a(f"BISHOP_GOTO_RHS {bd} BISHOP_GOTO_RHS {bd} R")
    a("BISHOP_GOTO_RHS , BISHOP_GOTO_RHS , R")
    a("BISHOP_GOTO_RHS B BISHOP_RHS B R")
    for px in letters:
        a(f"BISHOP_RHS {px} BISHOP_{px} {px} R")

    # px, py converted. Now treat as Rook problem
    a("BISHOP_GOTO_RHS _ ROOKIFY _ L")
    a("ROOKIFY B ROOKIFY R L")
    for c in ext_letters + ext_nums + ",":
        a(f"ROOKIFY {c} ROOKIFY {c} L")
    a("ROOKIFY _ INIT _ R")

    # --- Knight ---
    for kx in letters:
        a(f"{kx} N KNIGHT_{kx} N R")
        for px in letters:
            d = abs(letters.index(kx) - letters.index(px))
            if d not in (1, 2):
                a(f"KNIGHT_{kx} {px} FINISH_N {px} R")
            else:
                a(f"KNIGHT_{kx} {px} KNIGHT_Y {'O' if d == 1 else 'T'} R")

    for py in nums:
        a(f"KNIGHT_Y {py} KNIGHT_Y_{py} _ L")
        for d in "OT,":
            a(f"KNIGHT_Y_{py} {d} KNIGHT_Y_{py} {d} L")
        a(f"KNIGHT_Y_{py} N KNIGHT_Y_{py} N L")

        for ky in nums:
            d = abs(nums.index(ky) - nums.index(py))
            if d not in (1, 2):
                a(f"KNIGHT_Y_{py} {ky} FINISH_N {ky} R")
            else:
                a(f"KNIGHT_Y_{py} {ky} KNIGHT_FINAL_{'O' if d == 1 else 'T'} {ky} R")

    for d in "OT":
        a(f"KNIGHT_FINAL_{d} , KNIGHT_FINAL_{d} , R")
        a(f"KNIGHT_FINAL_{d} N KNIGHT_FINAL_{d} N R")
        for d2 in "OT":
            if d != d2:
                a(f"KNIGHT_FINAL_{d} {d2} FINISH_Y {d2} R")
            else:
                a(f"KNIGHT_FINAL_{d} {d2} FINISH_N {d2} R")

    # --- Append result then wipe left ---
    for result in "YN":
        a(f"FINISH_{result} _ WIPE_LEFT {result} L")
        for c in ext_letters + ext_nums + "QRBN,TO":
            a(f"FINISH_{result} {c} FINISH_{result} {c} R")

    for c in ext_letters + ext_nums + "QRBN,TO":
        a(f"WIPE_LEFT {c} WIPE_LEFT _ L")
    a("WIPE_LEFT _ HALT _ L")

    return "\n".join(lines)


if __name__ == "__main__":
    code = generate_code()
    with open("solutions/38.txt", "w", encoding="utf-8") as f:
        f.write(code)
