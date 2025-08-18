with open("2025_contest/07.txt") as f:
    inp = f.read()

tracks_s, swaps_s, test_index_s = inp.split("\n\n")

tracks = [-1] + [int(line) for line in tracks_s.splitlines()]
swaps = [[int(num) for num in line.split("-")] for line in swaps_s.splitlines()]
test_index = int(test_index_s)

cur_tracks = tracks.copy()
for i, j in swaps:
    cur_tracks[i], cur_tracks[j] = cur_tracks[j], cur_tracks[i]

answer1 = cur_tracks[test_index]
print(answer1)


# Part 2

cur_tracks = tracks.copy()
for (i, j), (k, _) in zip(swaps, swaps[1:] + [swaps[0]]):
    cur_tracks[k], cur_tracks[i], cur_tracks[j] = (
        cur_tracks[j],
        cur_tracks[k],
        cur_tracks[i],
    )

answer2 = cur_tracks[test_index]
print(answer2)

# Part 3

cur_tracks = tracks.copy()
for i, j in swaps:
    if j < i:
        i, j = j, i
    i2 = i
    j2 = j
    while i2 < j and j2 < len(cur_tracks):
        cur_tracks[i2], cur_tracks[j2] = cur_tracks[j2], cur_tracks[i2]
        i2 += 1
        j2 += 1

answer3 = cur_tracks[test_index]
print(answer3)
