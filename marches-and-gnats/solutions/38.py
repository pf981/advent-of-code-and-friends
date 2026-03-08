def generate_code() -> str:
    lines = []
    letters = "abcdefgh"
    ext_letters = "abcdefghijklmno"
    ext_nums = "1234567890αβγδε"

    def a(s: str) -> None:
        lines.append(s)

    def bishop_sum(x: str, y: int) -> str:
        return ext_letters[letters.index(x) + y - 1]

    def bishop_diff(x: str, y: int) -> str:
        return ext_nums[letters.index(x) - (y - 1) + 7]

    def is_check(kx: str, ky: int, piece: str, px: str, py: int) -> bool:
        rook_check = kx == px or ky == py
        bishop_check = kx - ky == px - py or kx + ky == px + py
        knight_check = any(
            (px + dx, py + dy) == (kx, ky)
            for dx, dy in [(-2, 1), (-2, -1), (-1, -2), (-1, 2), (2, -1), (2, 1)]
        )

        match piece:
            case "Q":
                return rook_check or bishop_check
            case "R":
                return rook_check
            case "B":
                return bishop_check
            case "N":
                return knight_check
            case _:
                raise ValueError(f"Unknown piece: {piece}")

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

    # If we do not have a rook-check and the piece is a king, convert to a bishop
    # "ROOKIFY" will just go to the left and restart
    a("FINISH_N_IF_NOT_QUEEN Q ROOKIFY B L")

    # --- Bishop ---
    # Convert kx to represent positive diagonal, ky to be negative, and same for px, py
    # Then change "B" to "R" and treat it as a rook comparison
    for kx in letters:
        a(f"{kx} B BISHOP_{kx} B L")
        a(f"BISHOP_{kx} , BISHOP_{kx} , L")
        for ky in range(1, 9):
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

    # --- Append result then wipe left ---
    for result in "YN":
        a(f"FINISH_{result} _ WIPE_LEFT {result} L")
        for c in ext_letters + ext_nums + "QRBN,":
            a(f"FINISH_{result} {c} FINISH_{result} {c} R")

    for c in ext_letters + ext_nums + "QRBN,":
        a(f"WIPE_LEFT {c} WIPE_LEFT _ L")
    a("WIPE_LEFT _ HALT _ L")

    return "\n".join(lines)


if __name__ == "__main__":
    code = generate_code()
    with open("solutions/38.txt", "w", encoding="utf-8") as f:
        f.write(code)
