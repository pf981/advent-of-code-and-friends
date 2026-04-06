def generate_code() -> str:
    lines = []

    def a(s: str) -> None:
        lines.append(s)

    nums = "0123456789"

    # FIXME: DEBUG - For testing only. Skip straight to Cols

    # Use for testing cols
    # for c in nums:
    #     a(f"INIT {c} SEEK_LEFT_THEN_CHECK_COL_1_FOR_1 {c} L")

    # Use for testing squares
    for c in nums + "|=":
        a(f"INIT {c} INIT {c} R")
    a("INIT _ SEEK_LEFT_REPLACE_abcabcabcdefdefdefghighigh i L")
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
    cur_col_final_skip = {1: 1, 2: 2, 3: 3, 4: 5, 5: 6, 6: 7, 7: 9, 8: 10, 9: 11}
    for target in nums[1:]:
        for col, skip in cur_col_final_skip.items():
            if target == "9":
                new_col = col + 1
                new_target = "1"
            else:
                new_col = col
                new_target = int(target) + 1

            if new_col == 10:
                break

            for suffix in ["", "_FOUND"]:
                a(
                    f"CHECK_COL_{target}_SKIP_{skip}{suffix} _ SEEK_LEFT_THEN_CHECK_COL_{new_col}_FOR_{new_target} _ L"
                )

    for suffix in ["", "_FOUND"]:
        a(
            f"CHECK_COL_9_SKIP_11{suffix} _ SEEK_LEFT_REPLACE_abcabcabcdefdefdefghighigh i L"
        )

    # Check squares

    # Transform = and | into abcdefghi

    # 143a657b028c
    # 682a314b579c
    # 571a289b346c

    # 726d493e851f
    # 315d862e497f
    # 894d571e263f

    # 457g136h982i
    # 068g925h734i
    # 239g748h615i

    full_suffix = "abcabcabcdefdefdefghighigh"
    for i in range(1, len(full_suffix) + 1):
        suffix = full_suffix[:i]
        for c in nums:
            a(f"SEEK_LEFT_REPLACE_{suffix} {c} SEEK_LEFT_REPLACE_{suffix} {c} L")

        to_c = suffix[-1]
        from_c = "=" if to_c in "cfi" else "|"
        if i == 1:
            a(f"SEEK_LEFT_REPLACE_{suffix} {from_c} CHECK_SQUARE_FOR_1 {to_c} L")
        else:
            a(
                f"SEEK_LEFT_REPLACE_{suffix} {from_c} SEEK_LEFT_REPLACE_{suffix[: i - 1]} {to_c} L"
            )

    # CHECK_SQUARE_a_FOR_1
    # CHECK_SQUARE_a_FOR_1_NEXT -> go to next a then CHECK_SQUARE_a_FOR_1 L
    # CHECK_SQUARE_a_FOR_1_FOUND, CHECK_SQUARE_a_FOR_1_FOUND_NEXT_NEXT, CHECK_SQUARE_a_FOR_1_FOUND_NEXT
    for target in nums[1:]:
        for c in nums:
            if c == target:
                a(
                    f"CHECK_SQUARE_FOR_{target} {c} CHECK_SQUARE_FOR_{target}_FOUND {c} L"
                )
                a(f"CHECK_SQUARE_FOR_{target}_FOUND {c} SEEK_LEFT_THEN_WIPE N L")
            else:
                a(f"CHECK_SQUARE_FOR_{target} {c} CHECK_SQUARE_FOR_{target} {c} L")
                a(
                    f"CHECK_SQUARE_FOR_{target}_FOUND {c} CHECK_SQUARE_FOR_{target}_FOUND {c} L"
                )
        for stopper in "abcdefghi_X":
            if stopper == target:
                continue
            for suffix in ["", "_FOUND"]:
                a(
                    f"CHECK_SQUARE_FOR_{target}{suffix} {stopper} CHECK_SQUARE_FOR_{target}{suffix}_NEXT {c} R"
                )

        # NEXT
        for suffix in ["", "_FOUND"]:
            for c in nums:
                a(
                    f"CHECK_SQUARE_FOR_{target}{suffix}_NEXT {c} CHECK_SQUARE_FOR_{target}{suffix}_NEXT {c} R"
                )
            for square in "abcdefghi":
                a(
                    f"CHECK_SQUARE_FOR_{target}{suffix}_NEXT {square} CHECK_SQUARE_FOR_{target}{suffix}_NEXT_{square} {square} R"
                )
                for c in nums + "abcdefghi":
                    if c == square:
                        a(
                            f"CHECK_SQUARE_FOR_{target}{suffix}_NEXT_{square} {c} CHECK_SQUARE_FOR_{target}{suffix} {c} L"
                        )
                    else:
                        a(
                            f"CHECK_SQUARE_FOR_{target}{suffix}_NEXT_{square} {c} CHECK_SQUARE_FOR_{target}{suffix}_NEXT_{square} {c} R"
                        )

    # Wipe
    for c in nums + "|=abcdefghi":
        a(f"SEEK_LEFT_THEN_WIPE {c} SEEK_LEFT_THEN_WIPE {c} L")
    a("SEEK_LEFT_THEN_WIPE _ WIPE _ R")

    for c in nums + "|=abcdefghi":
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
# x = (
#     "534|678|912="
#     "672|195|348="
#     "198|342|567="
#     "859|761|423="
#     "426|853|791="
#     "713|924|856="
#     "961|537|284="
#     "287|419|635="
#     "345|286|179"
# )
# print(x) # Y
# 534|678|912=672|195|348=198|342|567=859|761|423=426|853|791=713|924|856=961|537|284=287|419|635=345|286|179
