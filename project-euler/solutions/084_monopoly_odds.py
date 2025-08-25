from enum import Enum, auto
import random


class Card(Enum):
    ADVANCE_TO_GO = auto()
    GO_TO_JAIL = auto()
    GOT_TO_JAIL = auto()
    GO_TO_C1 = auto()
    GO_TO_E3 = auto()
    GO_TO_H2 = auto()
    GO_TO_R1 = auto()
    GO_TO_NEXT_R = auto()
    GO_TO_NEXT_U = auto()
    GO_BACK_3_SQUARES = auto()


community_chest = [Card.ADVANCE_TO_GO, Card.GO_TO_JAIL]
chance = [
    Card.ADVANCE_TO_GO,
    Card.GOT_TO_JAIL,
    Card.GO_TO_C1,
    Card.GO_TO_E3,
    Card.GO_TO_H2,
    Card.GO_TO_R1,
    Card.GO_TO_NEXT_R,
    Card.GO_TO_NEXT_R,
    Card.GO_TO_NEXT_U,
    Card.GO_BACK_3_SQUARES,
]
squares = [
    "GO",
    "A1",
    "CC1",
    "A2",
    "T1",
    "R1",
    "B1",
    "CH1",
    "B2",
    "B3",
    "JAIL",
    "C1",
    "U1",
    "C2",
    "C3",
    "R2",
    "D1",
    "CC2",
    "D2",
    "D3",
    "FP",
    "E1",
    "CH2",
    "E2",
    "E3",
    "R3",
    "F1",
    "F2",
    "U2",
    "F3",
    "G2J",
    "G1",
    "G2",
    "CC3",
    "G3",
    "R4",
    "CH3",
    "H1",
    "T2",
    "H2",
]

squares.index("G2J")


def simulate(n_games: int = 10, n_turns: int = 10) -> list[int]:
    frequencies = [0] * len(squares)
    for _ in range(n_games):
        random.shuffle(community_chest)
        random.shuffle(chance)

        community_chest_i = 0
        chance_i = 0

        pos = random.randint(0, len(squares) - 2)
        pos += pos >= 30

        for _ in range(n_turns):
            roll = random.randint(1, 4) + random.randint(1, 4)
            pos += roll
            pos %= len(squares)

            match squares[pos]:
                case "CC1" | "CC2":
                    community_chest_i += 1
                    community_chest_i %= len(community_chest)

    return frequencies


random.seed(0)
