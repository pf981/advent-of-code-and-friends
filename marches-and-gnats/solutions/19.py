def generate_code() -> str:
    lines = []

    def a(s: str) -> None:
        lines.append(s)

    nums = "0123456789"

    # FIXME: DEBUG - For testing only. Skip straight to Cols
    for c in nums:
        a(f"INIT {c} SEEK_LEFT_THEN_CHECK_COL_1_FOR_1 {c} L")
    # FIXME: Remove above, Uncomment below

    # for c in nums:
    #     if c == "1":
    #         a(f"INIT {c} CHECK_ROW_1_FOUND {c} R")
    #     else:
    #         a(f"INIT {c} CHECK_ROW_1 {c} R")

    # Check rows
    for target in nums[1:]:
        for c in nums + "|":
            if c == target:
                a(f"CHECK_ROW_{target}_FOUND {c} SEEK_LEFT_THEN_WIPE N L")
                a(f"CHECK_ROW_{target} {c} CHECK_ROW_{target}_FOUND {c} R")
            else:
                a(f"CHECK_ROW_{target}_FOUND {c} CHECK_ROW_{target}_FOUND {c} R")
                a(f"CHECK_ROW_{target} {c} CHECK_ROW_{target} {c} R")

        # Finished row
        a(f"CHECK_ROW_{target} = CHECK_ROW_{target} = R")
        a(f"CHECK_ROW_{target}_FOUND = CHECK_ROW_{target} = R")

        # Finished board
        if target == "9":
            a(f"CHECK_ROW_{target} _ SEEK_LEFT_THEN_CHECK_COL_1_FOR_1 _ L")
            a(f"CHECK_ROW_{target}_FOUND _ SEEK_LEFT_THEN_CHECK_COL_1_FOR_1 _ L")
        else:
            a(f"CHECK_ROW_{target} _ SEEK_LEFT_THEN_CHECK_ROW_{int(target) + 1} _ L")
            a(
                f"CHECK_ROW_{target}_FOUND _ SEEK_LEFT_THEN_CHECK_ROW_{int(target) + 1} _ L"
            )

        if target != "1":
            for c in nums + "|=":
                a(
                    f"SEEK_LEFT_THEN_CHECK_ROW_{target} {c} SEEK_LEFT_THEN_CHECK_ROW_{target} {c} L"
                )
            a(f"SEEK_LEFT_THEN_CHECK_ROW_{target} _ CHECK_ROW_{target} _ R")

    # Check cols
    for col in range(1, 10):
        for target in range(1, 10):
            for c in nums + "|=":
                a(
                    f"SEEK_LEFT_THEN_CHECK_COL_{col}_FOR_{target} {c} SEEK_LEFT_THEN_CHECK_COL_{col}_FOR_{target} {c} L"
                )
            initial_skip = [None, 0, 1, 2, 4, 5, 6, 8, 9, 10][col]
            a(
                f"SEEK_LEFT_THEN_CHECK_COL_{col}_FOR_{target} _ CHECK_COL_{target}_SKIP_{initial_skip} _ R"
            )

    for skip in range(13):
        for target in nums[1:]:
            for c in nums + "|=":
                if skip == 0:
                    if c == target:
                        a(
                            f"CHECK_COL_{target}_SKIP_{skip} {c} CHECK_COL_{target}_SKIP_{11}_FOUND {c} R"
                        )
                        a(
                            f"CHECK_COL_{target}_SKIP_{skip}_FOUND {c} SEEK_LEFT_THEN_WIPE N L"
                        )
                    else:
                        a(
                            f"CHECK_COL_{target}_SKIP_{skip} {c} CHECK_COL_{target}_SKIP_{11} {c} R"
                        )
                        a(
                            f"CHECK_COL_{target}_SKIP_{skip}_FOUND {c} CHECK_COL_{target}_SKIP_{11}_FOUND {c} R"
                        )
                else:
                    a(
                        f"CHECK_COL_{target}_SKIP_{skip} {c} CHECK_COL_{target}_SKIP_{skip - 1} {c} R"
                    )
                    a(
                        f"CHECK_COL_{target}_SKIP_{skip}_FOUND {c} CHECK_COL_{target}_SKIP_{skip - 1}_FOUND {c} R"
                    )

    # When you hit the end of board when checking columns
    # initial_skip = [None, 0, 1, 2, 4, 5, 6, 8, 9, 10][col]
    cur_col_final_skip = {1: 1, 2: 2, 3: 3, 4: 5, 5: 6, 6: 7, 7: 9, 8: 10, 9: 11}
    for target in nums[1:]:
        for col, skip in cur_col_final_skip.items():
            if target == "9":
                new_col = col + 1
                new_target = "1"
            else:
                new_col = col
                new_target = int(target) + 1

            for suffix in ["", "_FOUND"]:
                a(
                    f"CHECK_COL_{target}_SKIP_{skip}{suffix} _ SEEK_LEFT_THEN_CHECK_COL_{new_col}_FOR_{new_target} _ L"
                )

    # Check squares

    # Wipe
    for c in nums + "|=":
        a(f"SEEK_LEFT_THEN_WIPE {c} SEEK_LEFT_THEN_WIPE {c} L")
    a("SEEK_LEFT_THEN_WIPE _ WIPE _ R")

    for c in nums + "|=":
        a(f"WIPE {c} WIPE _ R")
    for c in "YN":
        a(f"WIPE {c} WIPE {c} R")
    a("WIPE _ HALT _ R")

    return "\n".join(lines)


if __name__ == "__main__":
    code = generate_code()
    with open("solutions/19.txt", "w", encoding="utf-8") as f:
        f.write(code)
# x = (
#     "143|657|028="
#     + "682|314|579="
#     + "571|289|346="
#     + "726|493|851="
#     + "315|862|497="
#     + "894|571|263="
#     + "457|136|982="
#     + "068|925|734="
#     + "239|748|615"
# )
# 143|657|028=682|314|579=571|289|346=726|493|851=315|862|497=894|571|263=457|136|982=068|925|734=239|748|615
