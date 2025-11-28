from aocd import get_data

inp = get_data(day=15, year=2017)

import itertools
import re


def count_matches(starts):
    a_factor = 16807
    b_factor = 48271
    denominator = 2147483647
    mod = pow(2, 16)

    a, b = starts
    match_count1 = 0
    for i in range(40000000):
        a = (a_factor * a) % denominator
        b = (b_factor * b) % denominator
        match_count1 += (a % mod) == (b % mod)

    a, b = starts
    match_count2 = 0
    for i in range(5000000):
        while (a := (a_factor * a) % denominator) % 4 != 0:
            pass
        while (b := (b_factor * b) % denominator) % 8 != 0:
            pass
        match_count2 += (a % mod) == (b % mod)

    return match_count1, match_count2

  
match_count1, match_count2 = count_matches([int(x) for x in re.findall(r'\d+', inp)])

answer = match_count1
print(answer)

answer = match_count2
print(answer)
