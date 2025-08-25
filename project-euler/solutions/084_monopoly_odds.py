import random
import collections

NUM_SQUARES = 40
NUM_TURNS = 1_000_000

GO = 0
JAIL = 10
C1 = 11
E3 = 24
H2 = 39
R1 = 5
G2J = 30

CC_SQUARES = [2, 17, 33]
CH_SQUARES = [7, 22, 36]

RAILWAYS = [5, 15, 25, 35]
UTILITIES = [12, 28]


def next_railway(pos: int) -> int:
    for railway in RAILWAYS:
        if railway > pos:
            return railway
    return RAILWAYS[0]


def next_utility(pos: int) -> int:
    for utility in UTILITIES:
        if utility > pos:
            return utility
    return UTILITIES[0]  # Wrap to first


def simulate() -> collections.Counter[int]:
    pos = 0
    doubles_count = 0
    counts: collections.Counter[int] = collections.Counter()

    for turn in range(NUM_TURNS):
        d1 = random.randint(1, 4)
        d2 = random.randint(1, 4)

        if d1 == d2:
            doubles_count += 1
        else:
            doubles_count = 0

        if doubles_count == 3:
            pos = JAIL
            doubles_count = 0
        else:
            pos = (pos + d1 + d2) % NUM_SQUARES

            if pos == G2J:  # Go To Jail square
                pos = JAIL
            elif pos in CC_SQUARES:  # Community Chest
                card = random.randint(1, 16)
                if card == 1:  # Advance to GO
                    pos = GO
                elif card == 2:  # Go to JAIL
                    pos = JAIL

            elif pos in CH_SQUARES:
                card = random.randint(1, 16)
                if card == 1:  # Advance to GO
                    pos = GO
                elif card == 2:  # Go to JAIL
                    pos = JAIL
                elif card == 3:  # Go to C1
                    pos = C1
                elif card == 4:  # Go to E3
                    pos = E3
                elif card == 5:  # Go to H2
                    pos = H2
                elif card == 6:  # Go to R1
                    pos = R1
                elif card == 7 or card == 8:  # Next Railway
                    pos = next_railway(pos)
                elif card == 9:  # Next Utility
                    pos = next_utility(pos)
                elif card == 10:  # Go back 3 squares
                    pos = (pos - 3) % NUM_SQUARES
                    if pos in CC_SQUARES:
                        cc_card = random.randint(1, 16)
                        if cc_card == 1:  # Advance to GO
                            pos = GO
                        elif cc_card == 2:  # Go to JAIL
                            pos = JAIL

        counts[pos] += 1

    return counts


counts = simulate()
top_3 = counts.most_common(3)
for i, (square, count) in enumerate(top_3):
    percentage = (count / NUM_TURNS) * 100

answer = "".join(f"{square:02d}" for square, _ in top_3)
