import itertools


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

    return bingos


with open("./input/2026/12.txt") as f:
    text = f.read()

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
