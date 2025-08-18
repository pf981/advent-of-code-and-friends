import downloader

lines = downloader.get_puzzle(16).splitlines()

grid = []
row_checksums = []
col_checksums = [int(s, 16) for s in lines[-1].split()]
for line in lines[:-1]:
    nums = [int(s, 16) for s in line.split()]
    grid.append(nums[:-1])
    row_checksums.append(nums[-1])

for i, (row, checksum) in enumerate(zip(grid, row_checksums)):
    expected = sum(row) % 256
    if checksum != expected:
        bad_row = i
        break

for i, (col, checksum) in enumerate(zip(zip(*grid), col_checksums)):
    expected = sum(col) % 256
    if checksum != expected:
        bad_col = i
        delta = (expected - checksum) % 256
        break

bad_byte = grid[bad_row][bad_col]

answer = bad_byte * (bad_byte - delta)
print(answer)
