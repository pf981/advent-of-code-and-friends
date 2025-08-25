import collections
import graphlib
import re


def connections(attempt):
    for i, digit1 in enumerate(attempt):
        for digit2 in attempt[i + 1 :]:
            yield digit1, digit2


def make_graph(all_attempts):
    graph = collections.defaultdict(set)

    for attempt in all_attempts:
        for before, after in connections(attempt):
            graph[before].add(after)

    return graph


with open("data/0079_keylog.txt") as in_file:
    text = in_file.read()

all_attempts = re.findall(r"(\d\d\d)", text)
possible_digits = set(digit for attempt in all_attempts for digit in attempt)
graph = make_graph(all_attempts)
sorted_graph = graphlib.TopologicalSorter(graph).static_order()

answer = "".join([next(iter(item)) for item in sorted_graph])[::-1]
print(answer)
