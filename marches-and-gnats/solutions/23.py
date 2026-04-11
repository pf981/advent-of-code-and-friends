# // |,||;||||,||||||
# // |,XX;||||,||||
# // |XXXX||||,||||
# // XXXXXX|||,||||
# // ______|||,||||
# // Sort
# // Lookup table

# // ax,ay;bx,by
# // dx;dy
# // dx^2;dy^2
# // {dx^2}{dy^2}   // Concatenate by removing ";"
# // sqrt {dx^2}{dy^2}

# // How many perfect squares are there within some reasonable bound? There are like 50
# // Just hardcode them?

# // How to "compress"?
def generate_code() -> str:
    lines = []

    def a(s: str) -> None:
        lines.append(s)

    # Transform "ax,ay;bx,by" to "dx;dy"

    # "ax,ay;bx,by" to "ax,XX;bx,dy"
    a("INIT | INIT | R")
    a("INIT , PICKUP_AY_POP_BY , R")
    for action in ["POP", "APPEND"]:
        a(f"PICKUP_AY_{action}_BY _ PICKUP_AY_{action}_BY _ R")
        a(f"PICKUP_AY_{action}_BY ; PICKUP_AX_POP_BX X L")
        a(f"PICKUP_AY_{action}_BY | TRANSPORT_AY_{action}_BY X R")
        for c in "|;,":
            a(f"TRANSPORT_AY_{action}_BY {c} TRANSPORT_AY_{action}_BY {c} R")
    a("TRANSPORT_AY_APPEND_BY _ NEXT_AY_APPEND_BY | L")
    a("TRANSPORT_AY_POP_BY _ POP_BY _ L")
    a("POP_BY | NEXT_AY_POP_BY _ L")
    a("POP_BY , APPEND_BY , R")  # No BY left so append rather than pop
    a("APPEND_BY _ NEXT_AY_APPEND_BY | L")

    for action in ["POP", "APPEND"]:
        for c in "|;,":
            a(f"NEXT_AY_{action}_BY {c} NEXT_AY_{action}_BY {c} L")
        a(f"NEXT_AY_{action}_BY X PICKUP_AY_{action}_BY X R")

    # "ax,XX;bx,dy" to "XXXXXdx,dy"
    for action in ["POP", "APPEND"]:
        a(f"PICKUP_AX_{action}_BX X PICKUP_AX_{action}_BX X L")
        a(f"PICKUP_AX_{action}_BX , PICKUP_AX_{action}_BX X L")
        a(f"PICKUP_AX_{action}_BX | {action}_BX X R")
        a(f"PICKUP_AX_{action}_BX _ REMOVE_X_THEN_POP_LHS _ R")
        a(f"{action}_BX X {action}_BX X R")
    a("POP_BX | PICKUP_AX_POP_BX X L")
    a("POP_BX , PREPEND_THEN_PICKUP_AX_APPEND_BX , L")
    a("APPEND_BX | PREPEND_THEN_PICKUP_AX_APPEND_BX | L")
    a("PREPEND_THEN_PICKUP_AX_APPEND_BX X PICKUP_AX_APPEND_BX | L")

    # FIXME: This won't work. Max doesn't uniquely define triple.
    # Maybe: 0|||,||||E
    #        0|||,||||E
    #        03__,||||E
    # Remove min. "dx,dy" to "dx" or "dy" (whichever is greater)

    # ||||,||
    # |||X,X|
    # ||XX,XX
    # |XXX,XX
    #        ^ Wipe RHS

    # _||,||||
    # _|X,X|||
    # _XX,XX||
    # ^ Wipe LHS
    a("REMOVE_X_THEN_POP_LHS X REMOVE_X_THEN_POP_LHS _ R")
    a("REMOVE_X_THEN_POP_LHS | REMOVE_X_THEN_POP_LHS | R")
    a("REMOVE_X_THEN_POP_LHS , POP_LHS , L")

    a("POP_LHS , POP_LHS , L")
    a("POP_LHS | POP_RHS X R")
    a("POP_LHS X POP_LHS X L")
    a("POP_LHS _ WIPE_LHS _ R")

    a("POP_RHS , POP_RHS , R")
    a("POP_RHS | POP_LHS X L")
    a("POP_RHS X POP_RHS X R")
    a("POP_RHS _ WIPE_RHS _ L")

    # WIPE_LHS/RHS
    a("WIPE_LHS X WIPE_LHS _ R")
    a("WIPE_LHS , FIX_RHS _ R")

    a("WIPE_RHS X WIPE_RHS _ L")
    a("WIPE_RHS , FIX_LHS _ L")

    a("FIX_RHS X FIX_RHS | R")
    a("FIX_RHS | SEEK_LEFT_THEN_COUNT | L")

    a("FIX_LHS X FIX_LHS | L")
    a("FIX_LHS | SEEK_LEFT_THEN_COUNT | L")

    # Count and use lookup table
    a("SEEK_LEFT_THEN_COUNT | SEEK_LEFT_THEN_COUNT | L")
    a("SEEK_LEFT_THEN_COUNT _ COUNT_0 _ R")

    triples = set()
    for n in range(1, 100):
        for m in range(n + 1, 100):
            x = m * m - n * n
            y = 2 * m * n
            z = m * m + n * n
            if z > 300:
                continue
            triples.add((x, y, z))
    m = {max(x, y): z for x, y, z in triples}
    for count in range(max(m)):
        a(f"COUNT_{count} | COUNT_{count + 1} _ R")
    for count, result in m.items():
        a(f"COUNT_{count} _ OUTPUT_{result - 1} | R")

    for count in range(1, max(m)):
        a(f"OUTPUT_{count} _ OUTPUT_{count - 1} | R")
    a("OUTPUT_0 _ HALT _ R")

    return "\n".join(lines)


if __name__ == "__main__":
    code = generate_code()
    with open("solutions/23.txt", "w", encoding="utf-8") as f:
        f.write(code)
