def generate_code() -> str:
    lines = []

    def a(s):
        lines.append(s)

    letters = "abcdefghijklmnopqrstuvwxyz"

    # Append M
    for c in letters:
        a(f"INIT {c} INIT {c} R")
    a("INIT _ PREPEND_S M L")

    # Prepend S
    for c in letters:
        a(f"PREPEND_S {c} PREPEND_S {c} L")
    a("PREPEND_S _ PICKUP S R")

    a("PICKUP X PICKUP X R")
    a("PICKUP M WIPE_LEFT M L")  # Processed entire string

    # Append to right
    for c in letters:
        a(f"PICKUP {c} ADD_ONE_{c} X R")
        for c2 in letters:
            a(f"ADD_ONE_{c} {c2} ADD_ONE_{c} {c2} R")

        a(f"ADD_ONE_{c} X ADD_ONE_{c} X R")
        a(f"ADD_ONE_{c} M ADD_ONE_{c} M R")
        a(f"ADD_ONE_{c} | ADD_ONE_{c} | R")
        a(f"ADD_ONE_{c} _ FIND_NEXT_{c} | L")

    # Seek left with known letter and find next
    for c in letters:
        for c2 in letters + "X|M":
            a(f"FIND_NEXT_{c} {c2} FIND_NEXT_{c} {c2} L")
        a(f"FIND_NEXT_{c} S PICKUP_{c} S R")

        for c2 in letters + "X":
            if c2 == c:
                a(f"PICKUP_{c} {c2} ADD_ONE_{c} X R")
            else:
                a(f"PICKUP_{c} {c2} PICKUP_{c} {c2} R")

        a(f"PICKUP_{c} M APPEND_{c} M R")
        for c2 in letters + "|":
            a(f"APPEND_{c} {c2} APPEND_{c} {c2} R")
        a(f"APPEND_{c} _ FIND_NEXT {c} L")

    # Seek left with no letter and find next new letter
    for c in letters + "X|M":
        a(f"FIND_NEXT {c} FIND_NEXT {c} L")
    a("FIND_NEXT S PICKUP S R")

    # Finished processing entire string
    a("WIPE_LEFT M WIPE_LEFT M L")
    a("WIPE_LEFT X WIPE_LEFT _ L")
    a("WIPE_LEFT S WIPE_LEFT _ L")
    a("WIPE_LEFT _ SEEK_M_THEN_POP_ALL _ R")

    a("SEEK_M_THEN_POP_ALL _ SEEK_M_THEN_POP_ALL _ R")
    a("SEEK_M_THEN_POP_ALL M POP_ALL M R")

    a("POP_ALL X POP_ALL X R")
    a("POP_ALL | FIND_NEXT_CHAR_AND_POP X R")
    a("FIND_NEXT_CHAR_AND_POP | FIND_NEXT_CHAR_AND_POP | R")
    a("FIND_NEXT_CHAR_AND_POP X FIND_NEXT_CHAR_AND_POP | R")
    for c in letters:
        a(f"FIND_NEXT_CHAR_AND_POP {c} POP_ALL {c} R")

    a("POP_ALL _ SEEK_M_LEFT_THEN_POP_ALL_1 _ L")
    for is_completed in [0, 1]:
        a(
            f"SEEK_M_LEFT_THEN_POP_ALL_{is_completed} X SEEK_M_LEFT_THEN_POP_ALL_{is_completed} X L"
        )
        for c in letters + "|":
            a(
                f"SEEK_M_LEFT_THEN_POP_ALL_{is_completed} {c} SEEK_M_LEFT_THEN_POP_ALL_0 {c} L"
            )
    a("SEEK_M_LEFT_THEN_POP_ALL_0 M POP_ALL M R")
    a("SEEK_M_LEFT_THEN_POP_ALL_1 M WIPE_RIGHT_THEN_HALT _ R")

    # Finished popping one
    for c in letters:
        a(f"POP_ALL {c} PREPEND_{c}_THEN_CONTINUE ! L")
        for c2 in letters + "X|M":
            a(f"PREPEND_{c}_THEN_CONTINUE {c2} PREPEND_{c}_THEN_CONTINUE {c2} L")
        a(f"PREPEND_{c}_THEN_CONTINUE _ CONTINUE {c} R")

    # Resume popping from "!"
    for c in letters + "MX|":
        a(f"CONTINUE {c} CONTINUE {c} R")
    a("CONTINUE ! POP_ALL X R")

    # Processed all letters
    a("WIPE_RIGHT_THEN_HALT X WIPE_RIGHT_THEN_HALT _ R")
    a("WIPE_RIGHT_THEN_HALT _ HALT _ R")

    return "\n".join(lines)


if __name__ == "__main__":
    code = generate_code()
    with open("solutions/26.txt", "w", encoding="utf-8") as f:
        f.write(code)
