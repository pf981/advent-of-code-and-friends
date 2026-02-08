"""
|||||||:hello-world-how-are-you
h||||||:|ello-world-how-are-you
...
hello-w:|||||||orld-how-are-you
hello+|||||||:world-how-are-you
hello+w||||||:|orld-how-are-you
...
hello+world-h:|||||||ow-are-you
hello+world+|||||||:how-are-you
hello+world+h||||||:|ow-are-you
hello+world+how-are:|||||||-you
hello+world+how-are+|||||||:you
hello+world+how-are+you||||:|||
hello+world+how-are+you
"""

"""
Exchange
FIND_FIRST_LETTER (right until "h") AKA INIT
|||||||:hello-world-how-are-you
EXCHANGE_h (left until first |)
h||||||:|ello-world-how-are-you
...
FIND_FIRST_LETTER
hello-w:|||||||orld-how-are-you

hello-w:||||||||rld-how-are-you
               ^
EXCHANGE_o

hello-w:||||||||rld-how-are-you
      ^      (EXCHANGE_o hit letter)
UNEXCHANGE_o  (also replaces : with :)
hello-w|||||||||rld-how-are-you
hello-w||||||||orld-how-are-you
NEXT_UNEXCHANGE (seek left)
hello-|||||||||orld-how-are-you
UNEXCHANGE_w
hello-||||||||world-how-are-you
NEXT_UNEXCHANGE (seek left)
hello-||||||||world-how-are-you
     ^   (NEXT_UNEXCHANGE hit +)
hello+||||||||world-how-are-you
WRAP   (replace last | with :)
hello+|||||||:world-how-are-you

hello+|||||||:world-how-are-you
hello+w||||||:|orld-how-are-you
...
hello+world-h:|||||||ow-are-you
hello+world+|||||||:how-are-you
hello+world+h||||||:|ow-are-you
hello+world+how-are:|||||||-you
hello+world+how-are+|||||||:you
hello+world+how-are+you||||:|||
hello+world+how-are+you
"""


def generate_code() -> str:
    lines = []

    def a(s):
        lines.append(s)

    letters = "abcdefghijklmnopqrstuvwxyz"

    for c in "|:":
        a(f"INIT {c} INIT {c} R")

    for c in letters + "-":
        a(f"INIT {c} EXCHANGE_{c} | L")

        a(f"EXCHANGE_{c} : EXCHANGE_{c} : L")
        a(f"EXCHANGE_{c} | EXCHANGE_{c} | L")

        for c2 in letters + "_-+":
            a(f"EXCHANGE_{c} {c2} PLACE_{c} {c2} R")
        a(f"PLACE_{c} | INIT {c} R")

        if c == "-":
            # Wrap occurs on word boundary
            a("PLACE_- : PLACEBACK_COLON + R")
        else:
            # Wrap required
            a(f"PLACE_{c} : UNEXCHANGE_{c} | R")
            a(f"UNEXCHANGE_{c} | UNEXCHANGE_{c} | R")
            for c2 in letters + "-_":
                a(f"UNEXCHANGE_{c} {c2} UNPLACE_{c} {c2} L")
            a(f"UNPLACE_{c} | NEXT_UNEXCHANGE {c} L")

    a("NEXT_UNEXCHANGE | NEXT_UNEXCHANGE | L")
    a("NEXT_UNEXCHANGE - PLACEBACK_COLON + R")  # Wrap complete
    a("PLACEBACK_COLON | PLACEBACK_COLON | R")
    for c in letters:
        a(f"NEXT_UNEXCHANGE {c} UNEXCHANGE_{c} | R")
        a(f"PLACEBACK_COLON {c} PLACE_COLON {c} L")
    a("PLACE_COLON | INIT : R")

    a("INIT _ WIPE_LEFT _ L")
    a("WIPE_LEFT | WIPE_LEFT _ L")
    a("WIPE_LEFT : WIPE_LEFT _ L")
    for c in letters:
        a(f"WIPE_LEFT {c} HALT {c} L")

    return "\n".join(lines)


if __name__ == "__main__":
    code = generate_code()
    with open("solutions/21.txt", "w", encoding="utf-8") as f:
        f.write(code)
