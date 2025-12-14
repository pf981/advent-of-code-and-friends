def generate_code() -> str:
    lines = []

    def a(s):
        lines.append(s)

    letters = "abcdefghij"
    mats = "WMP"

    for c in mats:
        a(f"INIT {c} INIT {c} R")
    a("INIT @ WIPE_RIGHT _ R")

    for c in letters:
        a(f"INIT {c} PICKUP_{c} X R")
        for c2 in letters + mats:
            if c2 == c:
                a(f"PICKUP_{c} {c2} PICKUP_{c} X R")
            else:
                a(f"PICKUP_{c} {c2} PICKUP_{c} {c2} R")

        a(f"PICKUP_{c} @ CONVERT_{c} @ R")
        for c2 in letters + mats + ",":
            if c2 == c:
                a(f"CONVERT_{c} {c2} GRAB {c2} R")
            else:
                a(f"CONVERT_{c} {c2} CONVERT_{c} {c2} R")

        a(f"CONVERT_{c} : SKIP_THEN_CONVERT_{c} : R")
        for c2 in letters + mats:
            a(f"SKIP_THEN_CONVERT_{c} {c2} CONVERT_{c} {c2} R")

        a(f"CONVERT_{c} _ SEEK_@_LEFT_AND_CONVERT_{c} _ L")
        for c2 in letters + mats + ":,":
            a(f"SEEK_@_LEFT_AND_CONVERT_{c} {c2} SEEK_@_LEFT_AND_CONVERT_{c} {c2} L")
        a(f"SEEK_@_LEFT_AND_CONVERT_{c} @ CONVERT_{c} @ R")

    a("GRAB : GRAB : R")
    for c in letters:
        a(f"GRAB {c} CONVERT_{c} {c} R")
    for c in mats:
        a(f"GRAB {c} REPLACE_X_{c} {c} L")

        for c2 in letters + mats + ":,@":
            a(f"REPLACE_X_{c} {c2} REPLACE_X_{c} {c2} L")
        a(f"REPLACE_X_{c} X REPLACE_X_{c} {c} L")
        a(f"REPLACE_X_{c} _ INIT _ R")

    for c in letters + mats + ":,":
        a(f"WIPE_RIGHT {c} WIPE_RIGHT _ R")
    a("WIPE_RIGHT _ HALT _ R")

    return "\n".join(lines)


if __name__ == "__main__":
    code = generate_code()
    with open("solutions/29.txt", "w", encoding="utf-8") as f:
        f.write(code)
