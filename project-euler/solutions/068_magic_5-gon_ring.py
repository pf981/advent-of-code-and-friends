import collections
import itertools
import operator
from collections.abc import Generator


def generate_rings() -> Generator[collections.deque[tuple[int, int, int]], None, None]:
    for perm in itertools.permutations(list(range(1, 10))):
        ring = collections.deque(
            [
                (10, perm[0], perm[1]),
                (perm[2], perm[1], perm[3]),
                (perm[4], perm[3], perm[5]),
                (perm[6], perm[5], perm[7]),
                (perm[8], perm[7], perm[0]),
            ]
        )

        if all(sum(line) == sum(ring[0]) for line in ring):
            index_of_smallest_line = min(enumerate(ring), key=operator.itemgetter(1))[0]
            ring.rotate(-index_of_smallest_line)
            yield ring


answer = max(
    int("".join(str(n) for n in itertools.chain.from_iterable(ring)))
    for ring in generate_rings()
)
print(answer)
