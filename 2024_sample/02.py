import itertools
import operator


with open("2024_sample/02.txt") as f:
    lines = f.read().splitlines()

bools = [line == "TRUE" for line in lines]

answer1 = sum(i for i, b in enumerate(bools, 1) if b)
print(answer1)


def process_layer(bools):
    return [f(*pair) for pair, f in zip(itertools.batched(bools, 2), itertools.cycle([operator.and_, operator.or_]))]

answer2 = sum(process_layer(bools))
print(answer2)


answer3 = 0
layer = bools.copy()
while len(layer) > 1:
    answer3 += sum(layer)
    layer = process_layer(layer)
print(answer3)
