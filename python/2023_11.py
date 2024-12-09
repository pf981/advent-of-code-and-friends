from aocd import get_data, submit


def get_distances_sum(empty_size):
    distance_sum = 0
    for g1, g2 in pairs:
        d_row = abs(g2[0] - g1[0])
        for row in empty_rows:
            if min(g1[0], g2[0]) < row < max(g1[0], g2[0]):
                d_row += empty_size - 1

        d_col = abs(g2[1] - g1[1])
        for col in empty_cols:
            if min(g1[1], g2[1]) < col < max(g1[1], g2[1]):
                d_col += empty_size - 1

        distance_sum += d_row + d_col

    return distance_sum


inp = get_data(day=11, year=2023)
grid = inp.splitlines()
empty_rows = [i for i, row in enumerate(grid) if '#' not in row]
empty_cols = [i for i, col in enumerate(zip(*grid)) if '#' not in col]
galaxies = [(row, col) for row, line in enumerate(grid) for col, c in enumerate(line) if c == '#']
pairs = [(galaxies[i], galaxies[i2]) for i in range(len(galaxies)) for i2 in range(i + 1, len(galaxies))]

answer1 = get_distances_sum(2)
print(answer1)

submit(answer1, part='a', day=11, year=2023)


# Part 2


answer2 = get_distances_sum(1_000_000)
print(answer2)

submit(answer2, part='b', day=11, year=2023)
