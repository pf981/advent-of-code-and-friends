import itertools


# If a single number is 2+ bingos on a single card, does it count twice?
def count_bingos(card, call) -> bool:
    bingos = 0
    pos = next(
        ((r, c) for r in range(5) for c in range(5) if card[r][c] == call),
        None,
    )
    if pos is None:
        return False

    r0, c0 = pos
    card[r0][c0] = -1

    # Row
    if all(c == -1 for c in card[r0]):
        bingos += 1

    # Col
    if all(card[r][c0] == -1 for r in range(5)):
        bingos += 1

    # Diag up
    if r0 == 4 - c0 and all(card[r][4 - r] == -1 for r in range(5)):
        bingos += 1

    # Diag down
    if r0 == c0 and all(card[r][r] == -1 for r in range(5)):
        bingos += 1

    return min(bingos, 1)  # FIXME
    # return bingos


with open("./input/2026/12.txt") as f:
    text = f.read()
# text = """62 121 64 51 86 85 36 31 8 113 71 72 75 101 115 44 52 78 26 80 116 98 79 17 77
# 110 91 10 9 55 74 107 67 93 54 81 25 58 82 56 5 89 32 14 119 48 35 109 47 21
# 6 69 40 92 68 18 105 66 41 90 22 30 63 57 15 28 125 76 49 65 123 20 16 99 24
# 108 96 53 87 60 38 73 59 94 83 100 33 111 46 4 106 124 27 104 84 88 42 1 118 12
# 70 37 39 112 19 7 97 11 114 95 3 120 50 2 61 117 122 102 13 45 103 29 34 23 43

# 82 39 88 103 71 76 108 109 104 34 49 58 85 107 121 105 67 18 77 118 30 117 26 29 55
# 6 43 23 96 100 2 47 11 37 24 4 73 120 81 60 112 106 12 92 57 1 54 16 40 31
# 13 17 3 111 78 56 115 102 124 33 8 122 75 61 25 89 64 20 119 46 113 87 116 44 53
# 66 38 94 91 36 93 5 45 32 62 42 69 63 28 14 72 86 74 79 9 50 84 80 35 41
# 10 97 21 83 70 48 90 7 125 15 52 22 51 101 99 19 68 110 114 123 27 65 95 98 59"""

host, cards_s = text.split("\n\n")
host = list(map(int, host.split()))
cards = []
for line in cards_s.splitlines():
    nums = list(map(int, line.split()))
    batch = itertools.batched(nums, 5)
    cards.append([list(b) for b in batch])

bingos = 0
for i, call in enumerate(host, 1):
    for card in cards:
        bingos += count_bingos(card, call)
    if bingos >= 5:
        break

answer = call
print(answer)
# 563 incorrect
