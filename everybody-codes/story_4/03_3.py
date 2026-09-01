import collections

with open("./story_4/input/everybody_codes_e4_q03_p3.txt") as f:
    lines = f.read().splitlines()

for line in lines:
    if line.startswith("width"):
        width = int(line.split("=")[1])
    elif line.startswith("height"):
        height = int(line.split("=")[1])
    elif line.startswith("horizontal-offsets"):
        horizontal_offs = list(map(int, line.split("=")[1]))
    elif line.startswith("vertical-offsets"):
        vertical_offs = list(map(int, line.split("=")[1]))
    else:
        assert False

nrows = height
ncols = width

row_counts = collections.Counter()  # (offset, parity, color) -> count
r_period = 2 * len(horizontal_offs)
for r in range(r_period):
    wall = horizontal_offs[r % len(horizontal_offs)]
    wall2 = horizontal_offs[(r + 1) % len(horizontal_offs)]
    if wall != wall2:
        continue

    color = (
        sum(horizontal_offs[i % len(horizontal_offs)] == wall for i in range(1, r + 1))
        % 2
    )

    row_counts[(wall, r % 2, color)] += (nrows - 1 - r) // r_period + 1


col_counts = collections.Counter()  # (offset, parity, color) -> count
c_period = 2 * len(vertical_offs)
for c in range(c_period):
    wall = vertical_offs[c % len(vertical_offs)]
    wall2 = vertical_offs[(c + 1) % len(vertical_offs)]
    if wall != wall2:
        continue

    color = sum(vertical_offs[i % len(vertical_offs)] == 0 for i in range(1, c + 1)) % 2

    col_counts[(wall, c % 2, color)] += (ncols - 1 - c) // c_period + 1

counts = [0, 0]
for (r_wall, r_parity, r_color), r_count in row_counts.items():
    for (c_wall, c_parity, c_color), c_count in col_counts.items():
        if r_parity == c_wall and c_parity == r_wall:
            counts[(r_color + c_color) % 2] += r_count * c_count

answer = max(counts)
print(answer)
