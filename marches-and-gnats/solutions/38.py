def generate_code() -> str:
    lines = []
    letters = "abcdefgh"

    def a(s: str) -> None:
        lines.append(s)

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
    for kx in letters:
        a(f"INIT {kx} {kx} {kx} R")
        a(f"{kx} , {kx} , R")
        for ky in range(1, 9):
            a(f"{kx} {ky} {kx} {ky} R")

    # --- Rook ---
    for kx in letters:
        a(f"{kx} R ROOK_{kx} R R")
        for px in letters:
            if kx == px:
                a(f"ROOK_{kx} {px} FINISH_Y {px} R")
            else:
                # kx != px. Set px to 'a' to reduce states. Check py next.
                a(f"ROOK_{kx} {px} ROOK a R")

    for py in range(1, 9):
        a(f"ROOK {py} ROOK_{py} {py} L")
        a(f"ROOK_{py} a ROOK_{py} a L")
        a(f"ROOK_{py} , ROOK_{py} , L")
        a(f"ROOK_{py} R ROOK_{py} R L")
        for ky in range(1, 9):
            if py == ky:
                a(f"ROOK_{py} {ky} FINISH_Y {ky} R")
            else:
                a(f"ROOK_{py} {ky} FINISH_N {ky} R")

    # --- Append result then wipe left ---
    for result in "YN":
        a(f"FINISH_{result} _ WIPE_LEFT {result} L")
        for c in letters + "QRBN12345678,":
            a(f"FINISH_{result} {c} FINISH_{result} {c} R")

    for c in letters + "QRBN12345678,":
        a(f"WIPE_LEFT {c} WIPE_LEFT _ L")
    a("WIPE_LEFT _ HALT _ L")

    return "\n".join(lines)


if __name__ == "__main__":
    code = generate_code()
    with open("solutions/38.txt", "w", encoding="utf-8") as f:
        f.write(code)
