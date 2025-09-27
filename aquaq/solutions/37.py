import collections
import dataclasses
import itertools
import string


@dataclasses.dataclass
class Knowledge:
    must_be: list[str | None]
    must_not_be: list[set[str]]
    letter_min_counts: dict[str, int]
    letter_max_counts: dict[str, int]

    def __init__(self):
        self.must_be = [None] * 5
        self.must_not_be = [set() for _ in range(5)]
        self.letter_min_counts = {c: 0 for c in string.ascii_lowercase}
        self.letter_max_counts = {c: 5 for c in string.ascii_lowercase}


def is_valid(word: str, knowledge: Knowledge) -> bool:
    counts = collections.Counter(word)
    for c in string.ascii_lowercase:
        if not (
            knowledge.letter_min_counts[c]
            <= counts[c]
            <= knowledge.letter_max_counts[c]
        ):
            return False

    for c, must, must_not in zip(word, knowledge.must_be, knowledge.must_not_be):
        if must and c != must:
            return False
        if c in must_not:
            return False

    return True


with open("./input/37.txt") as f:
    text = f.read()

with open("./input/words.txt") as f:
    words = f.read().splitlines()

# text = """guess,result
# guess,0 0 0 0 2
# twins,0 1 0 0 2
# bowls,0 2 1 0 2
# worms,2 2 2 0 2
# works,2 2 2 0 2
# mince,2 2 2 2 2
# """

# text = """guess,result
# buxom,0 0 0 0 0
# three,2 2 1 1 2
# """

candidates = {word for word in words if len(word) == 5}

knowledge = Knowledge()
cur_candidates = candidates.copy()

final_words = []
for line in text.splitlines()[1:]:
    if not line:
        continue
    guess, outcomes_str = line.split(",")
    outcomes = [int(s) for s in outcomes_str.split()]

    new_min_counts: collections.Counter[str] = collections.Counter()
    apply_max_count: set[str] = set()
    for i, (c, outcome) in enumerate(zip(guess, outcomes)):
        if outcome == 2:
            knowledge.must_be[i] = c
            knowledge.must_not_be[i] = set(string.ascii_lowercase) - {c}
            new_min_counts[c] += 1
        elif outcome == 1:
            knowledge.must_not_be[i] |= {c}
            new_min_counts[c] += 1
        elif outcome == 0:
            knowledge.must_not_be[i] |= {c}
            apply_max_count.add(c)
        else:
            raise ValueError("Invalid outcome: {outcome}")

    for c, count in new_min_counts.items():
        knowledge.letter_min_counts[c] = max(knowledge.letter_min_counts[c], count)
    for c in apply_max_count:
        knowledge.letter_max_counts[c] = knowledge.letter_min_counts[c]

    print(f"{guess=} {outcomes=}")
    print(f"{knowledge=}")

    cur_candidates = {
        candidate for candidate in cur_candidates if is_valid(candidate, knowledge)
    }
    print(f"{cur_candidates=}")

    assert cur_candidates
    if len(cur_candidates) == 1:
        final_words.append(list(cur_candidates)[0])
        knowledge = Knowledge()
        cur_candidates = candidates.copy()

# final_words
answer = sum(ord(c) - ord("a") for c in itertools.chain.from_iterable(final_words))
print(answer)


# knowledge
# is_valid("these", knowledge)
