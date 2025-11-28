from aocd import get_data

inp = get_data(day=13, year=2017)

import re

scanners = [[int(x) for x in re.findall(r'\d+', line)] for line in inp.split('\n')]

trip_severity = 0
scanner_properties = []
for depth, r in scanners:
    severity = depth * r
    period = (r - 2) * 2 + 2
    is_caught = (depth % period) == 0

    if is_caught:
        trip_severity += severity
    scanner_properties.append((depth, period))

answer = trip_severity
print(answer)

import itertools

def find_smallest_delay(scanner_properties):
    for t in itertools.count():
        if all((depth + t) % period for depth, period in scanner_properties):
            return t

answer = find_smallest_delay(scanner_properties)
print(answer)
