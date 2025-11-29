with open("./2025/input/everybody_codes_e2025_q20_p1.txt") as f:
    lines = f.read().splitlines()
    # text = f.read().strip()

# lines = """T#TTT###T##
# .##TT#TT##.
# ..T###T#T..
# ...##TT#...
# ....T##....
# .....#.....""".splitlines()

nrows = len(lines)
ncols = len(lines[0])

pairs = 0
for r, row in enumerate(lines):
    # print("." * r + row.strip("."))
    for c, ch in enumerate("." * r + row.strip(".")):
        if ch != "T":
            continue

        # if r % 2 == 0:
        #     # R
        #     if c + 1 < ncols and lines[r][c + 1] == "T":
        #         print(f"{r=} {c+1=}")
        #         pairs += 1
        # else:
        if True:
            # UR
            if c + 1 < ncols and lines[r][c + 1] == "T":
                print(f"{r=} {c+1=}")
                pairs += 1

            parity = r % 2
            if c % 2 == parity:
                # if True:
                # Check parity first
                if r - 1 >= 0 and lines[r - 1][c] == "T":
                    print(f"{r-1=} {c=}")
                    pairs += 1

answer = pairs
print(answer)
# 99
# 71
# Your answer length is: incorrect
# The first character of your answer is: incorrect

# 100

# Your answer length is: correct
# The first character of your answer is: correct

# 116

# Your answer length is: correct
# The first character of your answer is: correct
