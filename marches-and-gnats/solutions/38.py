import itertools


def generate_code() -> str:
    lines = []
    letters = "abcdefgh"

    def a(s):
        lines.append(s)

    def is_check(kx: str, ky: int, piece: str, px: str, py: int) -> bool:
        kx = letters.index(kx)
        px = letters.index(px)

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
    prod = itertools.product(letters, range(1, 9), "QRBN", letters, range(1, 9))
    for kx, ky, piece, px, py in prod:
        if (kx, ky) == (px, py):
            continue

        result = "NY"[is_check(kx, ky, piece, px, py)]

        a(f"INIT {kx} {kx} _ R")
        a(f"{kx} {ky} {kx}{ky} _ R")
        a(f"{kx}{ky} , {kx}{ky} _ R")
        a(f"{kx}{ky} {piece} {kx}{ky}{piece} _ R")
        a(f"{kx}{ky}{piece} {px} {kx}{ky}{piece}{px} _ R")
        a(f"{kx}{ky}{piece}{px} {py} HALT {result} R")

    # Too many states: 2377. Maximum is 1024.
    return "\n".join(list(dict.fromkeys(lines)))


if __name__ == "__main__":
    code = generate_code()
    with open("solutions/38.txt", "w", encoding="utf-8") as f:
        f.write(code)
