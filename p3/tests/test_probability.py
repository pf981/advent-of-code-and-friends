from typing import List

import pytest


@pytest.mark.skip(reason="not implemented yet")
def test_birthdayparadox():
    def sat(n: int, year_len=365):
        prob = 1.0
        for i in range(n):
            prob *= (year_len - i) / year_len
        return (prob - 0.5) ** 2 <= 1/year_len

    assert sat(...)


@pytest.mark.skip(reason="not implemented yet")
def test_birthdayparadox_1():
    def sat(n: int, year_len=60182):
        prob = 1.0
        for i in range(n):
            prob *= (year_len - i) / year_len
        return (prob - 0.5) ** 2 <= 1/year_len

    assert sat(...)


@pytest.mark.skip(reason="not implemented yet")
def test_birthdayparadox_2():
    def sat(n: int, year_len=2):
        prob = 1.0
        for i in range(n):
            prob *= (year_len - i) / year_len
        return (prob - 0.5) ** 2 <= 1/year_len

    assert sat(...)


@pytest.mark.skip(reason="not implemented yet")
def test_birthdayparadox_3():
    def sat(n: int, year_len=3):
        prob = 1.0
        for i in range(n):
            prob *= (year_len - i) / year_len
        return (prob - 0.5) ** 2 <= 1/year_len

    assert sat(...)


@pytest.mark.skip(reason="not implemented yet")
def test_birthdayparadoxmontecarlo():
    def sat(n: int, year_len=365):
        import random
        random.seed(0)
        K = 1000  # number of samples
        prob = sum(len({random.randrange(year_len) for i in range(n)}) < n for j in range(K)) / K
        return (prob - 0.5) ** 2 <= year_len

    assert sat(...)


@pytest.mark.skip(reason="not implemented yet")
def test_birthdayparadoxmontecarlo_1():
    def sat(n: int, year_len=60182):
        import random
        random.seed(0)
        K = 1000  # number of samples
        prob = sum(len({random.randrange(year_len) for i in range(n)}) < n for j in range(K)) / K
        return (prob - 0.5) ** 2 <= year_len

    assert sat(...)


@pytest.mark.skip(reason="not implemented yet")
def test_birthdayparadoxmontecarlo_2():
    def sat(n: int, year_len=2):
        import random
        random.seed(0)
        K = 1000  # number of samples
        prob = sum(len({random.randrange(year_len) for i in range(n)}) < n for j in range(K)) / K
        return (prob - 0.5) ** 2 <= year_len

    assert sat(...)


@pytest.mark.skip(reason="not implemented yet")
def test_birthdayparadoxmontecarlo_3():
    def sat(n: int, year_len=3):
        import random
        random.seed(0)
        K = 1000  # number of samples
        prob = sum(len({random.randrange(year_len) for i in range(n)}) < n for j in range(K)) / K
        return (prob - 0.5) ** 2 <= year_len

    assert sat(...)


@pytest.mark.skip(reason="not implemented yet")
def test_ballotproblem():
    def sat(counts: List[int], target_prob=0.5):
        m, n = counts  # m = num 1's, n = num -1's
        probs = [1.0] + [0.0] * n  # probs[n] is probability for current m, starting with m = 1
        for i in range(2, m + 1):  # compute probs using dynamic programming for m = i
            old_probs = probs
            probs = [1.0] + [0.0] * n
            for j in range(1, min(n + 1, i)):
                probs[j] = (
                        j / (i + j) * probs[j - 1]  # last element is a -1 so use probs
                        +
                        i / (i + j) * old_probs[j]  # last element is a 1 so use old_probs, m = i - 1
                )
        return abs(probs[n] - target_prob) < 1e-6

    assert sat(...)


@pytest.mark.skip(reason="not implemented yet")
def test_ballotproblem_1():
    def sat(counts: List[int], target_prob=0.1791044776119403):
        m, n = counts  # m = num 1's, n = num -1's
        probs = [1.0] + [0.0] * n  # probs[n] is probability for current m, starting with m = 1
        for i in range(2, m + 1):  # compute probs using dynamic programming for m = i
            old_probs = probs
            probs = [1.0] + [0.0] * n
            for j in range(1, min(n + 1, i)):
                probs[j] = (
                        j / (i + j) * probs[j - 1]  # last element is a -1 so use probs
                        +
                        i / (i + j) * old_probs[j]  # last element is a 1 so use old_probs, m = i - 1
                )
        return abs(probs[n] - target_prob) < 1e-6

    assert sat(...)


@pytest.mark.skip(reason="not implemented yet")
def test_ballotproblem_2():
    def sat(counts: List[int], target_prob=0.03125):
        m, n = counts  # m = num 1's, n = num -1's
        probs = [1.0] + [0.0] * n  # probs[n] is probability for current m, starting with m = 1
        for i in range(2, m + 1):  # compute probs using dynamic programming for m = i
            old_probs = probs
            probs = [1.0] + [0.0] * n
            for j in range(1, min(n + 1, i)):
                probs[j] = (
                        j / (i + j) * probs[j - 1]  # last element is a -1 so use probs
                        +
                        i / (i + j) * old_probs[j]  # last element is a 1 so use old_probs, m = i - 1
                )
        return abs(probs[n] - target_prob) < 1e-6

    assert sat(...)


@pytest.mark.skip(reason="not implemented yet")
def test_ballotproblem_3():
    def sat(counts: List[int], target_prob=0.5803571428571429):
        m, n = counts  # m = num 1's, n = num -1's
        probs = [1.0] + [0.0] * n  # probs[n] is probability for current m, starting with m = 1
        for i in range(2, m + 1):  # compute probs using dynamic programming for m = i
            old_probs = probs
            probs = [1.0] + [0.0] * n
            for j in range(1, min(n + 1, i)):
                probs[j] = (
                        j / (i + j) * probs[j - 1]  # last element is a -1 so use probs
                        +
                        i / (i + j) * old_probs[j]  # last element is a 1 so use old_probs, m = i - 1
                )
        return abs(probs[n] - target_prob) < 1e-6

    assert sat(...)


@pytest.mark.skip(reason="not implemented yet")
def test_ballotproblem_4():
    def sat(counts: List[int], target_prob=0.7142857142857143):
        m, n = counts  # m = num 1's, n = num -1's
        probs = [1.0] + [0.0] * n  # probs[n] is probability for current m, starting with m = 1
        for i in range(2, m + 1):  # compute probs using dynamic programming for m = i
            old_probs = probs
            probs = [1.0] + [0.0] * n
            for j in range(1, min(n + 1, i)):
                probs[j] = (
                        j / (i + j) * probs[j - 1]  # last element is a -1 so use probs
                        +
                        i / (i + j) * old_probs[j]  # last element is a 1 so use old_probs, m = i - 1
                )
        return abs(probs[n] - target_prob) < 1e-6

    assert sat(...)


@pytest.mark.skip(reason="not implemented yet")
def test_binomialprobabilities():
    def sat(counts: List[int], p=0.5, target_prob=0.0625):
        from itertools import product
        a, b = counts
        n = a + b
        prob = (p ** a) * ((1-p) ** b)
        tot = sum([prob for sample in product([0, 1], repeat=n) if sum(sample) == a])
        return abs(tot - target_prob) < 1e-6

    assert sat(...)


@pytest.mark.skip(reason="not implemented yet")
def test_binomialprobabilities_1():
    def sat(counts: List[int], p=0.7588822808660473, target_prob=0.41658075878732215):
        from itertools import product
        a, b = counts
        n = a + b
        prob = (p ** a) * ((1-p) ** b)
        tot = sum([prob for sample in product([0, 1], repeat=n) if sum(sample) == a])
        return abs(tot - target_prob) < 1e-6

    assert sat(...)


@pytest.mark.skip(reason="not implemented yet")
def test_binomialprobabilities_2():
    def sat(counts: List[int], p=0.6569421516251613, target_prob=0.01872902529162693):
        from itertools import product
        a, b = counts
        n = a + b
        prob = (p ** a) * ((1-p) ** b)
        tot = sum([prob for sample in product([0, 1], repeat=n) if sum(sample) == a])
        return abs(tot - target_prob) < 1e-6

    assert sat(...)


@pytest.mark.skip(reason="not implemented yet")
def test_binomialprobabilities_3():
    def sat(counts: List[int], p=0.20001220211746595, target_prob=0.13419930454361995):
        from itertools import product
        a, b = counts
        n = a + b
        prob = (p ** a) * ((1-p) ** b)
        tot = sum([prob for sample in product([0, 1], repeat=n) if sum(sample) == a])
        return abs(tot - target_prob) < 1e-6

    assert sat(...)


@pytest.mark.skip(reason="not implemented yet")
def test_binomialprobabilities_4():
    def sat(counts: List[int], p=0.004837079863490135, target_prob=3.5517791266002235e-13):
        from itertools import product
        a, b = counts
        n = a + b
        prob = (p ** a) * ((1-p) ** b)
        tot = sum([prob for sample in product([0, 1], repeat=n) if sum(sample) == a])
        return abs(tot - target_prob) < 1e-6

    assert sat(...)


@pytest.mark.skip(reason="not implemented yet")
def test_exponentialprobability():
    def sat(p_stop: float, steps=10, target_prob=0.5):
        prob = sum(p_stop*(1-p_stop)**t for t in range(steps))
        return abs(prob - target_prob) < 1e-6

    assert sat(...)


@pytest.mark.skip(reason="not implemented yet")
def test_exponentialprobability_1():
    def sat(p_stop: float, steps=43, target_prob=0.2661542669448821):
        prob = sum(p_stop*(1-p_stop)**t for t in range(steps))
        return abs(prob - target_prob) < 1e-6

    assert sat(...)


@pytest.mark.skip(reason="not implemented yet")
def test_exponentialprobability_2():
    def sat(p_stop: float, steps=91, target_prob=0.03729141037377781):
        prob = sum(p_stop*(1-p_stop)**t for t in range(steps))
        return abs(prob - target_prob) < 1e-6

    assert sat(...)


@pytest.mark.skip(reason="not implemented yet")
def test_exponentialprobability_3():
    def sat(p_stop: float, steps=11, target_prob=0.9742781783529525):
        prob = sum(p_stop*(1-p_stop)**t for t in range(steps))
        return abs(prob - target_prob) < 1e-6

    assert sat(...)


@pytest.mark.skip(reason="not implemented yet")
def test_exponentialprobability_4():
    def sat(p_stop: float, steps=65, target_prob=0.8318555442956944):
        prob = sum(p_stop*(1-p_stop)**t for t in range(steps))
        return abs(prob - target_prob) < 1e-6

    assert sat(...)
