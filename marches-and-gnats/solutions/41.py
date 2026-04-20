# _111221
# _111221M
# _111221M
# ^
# _111221M
#  ^
#  1x1
# __11221M
#   ^
#   2x1
# ____221M31


def generate_code() -> str:
    lines = []
    digits = "1234567890"

    def a(s: str) -> None:
        lines.append(s)

    for digit in digits:
        a(f"INIT {digit} INIT {digit} R")
    a("INIT _ NEXT M L")

    for digit in digits + "M":
        a(f"NEXT {digit} NEXT {digit} L")
    a("NEXT _ PICKUP _ R")

    for digit in digits:
        a(f"PICKUP {digit} 1x{digit} _ R")

        for n in range(1, 10):
            for digit2 in digits + "M":
                if digit2 == digit:
                    a(f"{n}x{digit} {digit2} {n + 1}x{digit} _ R")
                else:
                    a(f"{n}x{digit} {digit2} PLACE_{n}x{digit} {digit2} R")
                a(f"PLACE_{n}x{digit} {digit2} PLACE_{n}x{digit} {digit2} R")
            a(f"PLACE_{n}x{digit} _ PLACE_{digit} {n} R")
        a(f"PLACE_{digit} _ NEXT {digit} L")

    a("PICKUP M HALT _ R")

    return "\n".join(lines)


if __name__ == "__main__":
    code = generate_code()
    with open("solutions/41.txt", "w", encoding="utf-8") as f:
        f.write(code)
