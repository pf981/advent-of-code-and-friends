def generate_code() -> str:
    lines = []

    def p(s):
        lines.append(s)

    p("HEADS ABB")
    for a in "AB":
        for b in "AB":
            p(f"START {a}{b}* {a}{b} __* RLS")

            for a2 in "AB":
                for b2 in "AB":
                    a_out = "@" if a2 == a else "_"
                    b_out = "@" if b2 == b else "_"
                    p(f"{a2}{b2} {a}{b}* {a}{b} {a_out}*{b_out} RLL")

            p(f"{a}{b} @@* STOP *** SSS")

            for a2 in "AB":
                out = "@" if a == b else "_"
                p(f"{a}{b} {a2}@* STOP **{out} SSS")
                p(f"{a}{b} {a2}_* STOP **{out} SSS")

            p(f"{a}{b} __* STOP *** SSS")
            p(f"{a}{b} _@* STOP *** SSS")

            p(f"{a}{b} @__ STOP *** SSS")

    return "\n".join(lines)


if __name__ == "__main__":
    code = generate_code()
    with open("gridos_tournament_1/02_1.txt", "w", encoding="utf-8") as f:
        f.write(code)
