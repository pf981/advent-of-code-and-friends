from typing import List

import pytest


@pytest.mark.skip(reason="not implemented yet")
def test_fermatslasttheorem():
    def sat(nums: List[int]):
        a, b, c, n = nums
        return (a ** n + b ** n == c ** n) and min(a, b, c) > 0 and n > 2

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_gcd():
    def sat(n: int, a=15482, b=23223, lower_bound=5):
        return a % n == 0 and b % n == 0 and n >= lower_bound

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_gcd_1():
    def sat(n: int, a=9, b=9, lower_bound=6):
        return a % n == 0 and b % n == 0 and n >= lower_bound

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_gcd_2():
    def sat(n: int, a=232610, b=3131721474, lower_bound=15000):
        return a % n == 0 and b % n == 0 and n >= lower_bound

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_gcd_3():
    def sat(n: int, a=247586288427023352, b=372021520735824432, lower_bound=1709054537):
        return a % n == 0 and b % n == 0 and n >= lower_bound

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_gcd_4():
    def sat(n: int, a=8797233, b=2370036150831, lower_bound=8364173):
        return a % n == 0 and b % n == 0 and n >= lower_bound

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_gcd_multi():
    def sat(n: int, nums=[77410, 23223, 54187], lower_bound=2):
        return all(i % n == 0 for i in nums) and n >= lower_bound

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_gcd_multi_1():
    def sat(n: int, nums=[14, 551755893, 902110495], lower_bound=1):
        return all(i % n == 0 for i in nums) and n >= lower_bound

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_gcd_multi_2():
    def sat(n: int, nums=[287260676668, 33263981357337, 47314720, 295717, 2957170], lower_bound=98647):
        return all(i % n == 0 for i in nums) and n >= lower_bound

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_gcd_multi_3():
    def sat(n: int, nums=[452452, 111673658096, 83221402264, 5027670648, 61177116, 154154, 116116, 1508784124848, 17036343324, 29091062, 100726626], lower_bound=977):
        return all(i % n == 0 for i in nums) and n >= lower_bound

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_gcd_multi_4():
    def sat(n: int, nums=[8154539588421190, 128861795], lower_bound=64216730):
        return all(i % n == 0 for i in nums) and n >= lower_bound

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_lcm():
    def sat(n: int, a=15, b=27, upper_bound=150):
        return n % a == 0 and n % b == 0 and 0 < n <= upper_bound

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_lcm_1():
    def sat(n: int, a=41234205765, b=597597185, upper_bound=73349253728):
        return n % a == 0 and n % b == 0 and 0 < n <= upper_bound

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_lcm_2():
    def sat(n: int, a=7601351956456, b=2974663988, upper_bound=389421039754872576):
        return n % a == 0 and n % b == 0 and 0 < n <= upper_bound

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_lcm_3():
    def sat(n: int, a=201717041833890, b=3585167190, upper_bound=731493653565433):
        return n % a == 0 and n % b == 0 and 0 < n <= upper_bound

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_lcm_4():
    def sat(n: int, a=79680, b=661339968, upper_bound=410128528659):
        return n % a == 0 and n % b == 0 and 0 < n <= upper_bound

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_lcm_multi():
    def sat(n: int, nums=[15, 27, 102], upper_bound=5000):
        return all(n % i == 0 for i in nums) and 0 < n <= upper_bound

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_lcm_multi_1():
    def sat(n: int, nums=[46477686772963437, 15649966299, 37939312240, 14036122804591, 39209330717234], upper_bound=82396663973139497934429093888):
        return all(n % i == 0 for i in nums) and 0 < n <= upper_bound

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_lcm_multi_2():
    def sat(n: int, nums=[55040126016, 4373970014334], upper_bound=219074883886936):
        return all(n % i == 0 for i in nums) and 0 < n <= upper_bound

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_lcm_multi_3():
    def sat(n: int, nums=[9140, 4882496600, 119119770064, 107772494796, 102424668, 3656, 1188591500932, 116992, 14700627932, 997397016], upper_bound=238661269929569213628364588516267312050595558326272):
        return all(n % i == 0 for i in nums) and 0 < n <= upper_bound

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_lcm_multi_4():
    def sat(n: int, nums=[173261568, 4270662976], upper_bound=17025943527197098):
        return all(n % i == 0 for i in nums) and 0 < n <= upper_bound

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_smallexponentbigsolution():
    def sat(n: int, b=2, target=5):
        return (b ** n) % n == target

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_smallexponentbigsolution_1():
    def sat(n: int, b=2, target=3):
        return (b ** n) % n == target

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_smallexponentbigsolution_2():
    def sat(n: int, b=1, target=2):
        return (b ** n) % n == target

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_smallexponentbigsolution_3():
    def sat(n: int, b=69, target=2):
        return (b ** n) % n == target

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_threecubes():
    def sat(nums: List[int], target=983):
        assert target % 9 not in [4, 5], "Hint"
        return len(nums) == 3 and sum([i ** 3 for i in nums]) == target

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_threecubes_1():
    def sat(nums: List[int], target=114):
        assert target % 9 not in [4, 5], "Hint"
        return len(nums) == 3 and sum([i ** 3 for i in nums]) == target

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_threecubes_2():
    def sat(nums: List[int], target=390):
        assert target % 9 not in [4, 5], "Hint"
        return len(nums) == 3 and sum([i ** 3 for i in nums]) == target

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_threecubes_3():
    def sat(nums: List[int], target=579):
        assert target % 9 not in [4, 5], "Hint"
        return len(nums) == 3 and sum([i ** 3 for i in nums]) == target

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_threecubes_4():
    def sat(nums: List[int], target=69294):
        assert target % 9 not in [4, 5], "Hint"
        return len(nums) == 3 and sum([i ** 3 for i in nums]) == target

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_foursquares():
    def sat(nums: List[int], n=12345):
        return len(nums) <= 4 and sum(i ** 2 for i in nums) == n

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_foursquares_1():
    def sat(nums: List[int], n=1):
        return len(nums) <= 4 and sum(i ** 2 for i in nums) == n

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_foursquares_2():
    def sat(nums: List[int], n=0):
        return len(nums) <= 4 and sum(i ** 2 for i in nums) == n

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_foursquares_3():
    def sat(nums: List[int], n=1321806837666853665854863414407013350963513):
        return len(nums) <= 4 and sum(i ** 2 for i in nums) == n

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_foursquares_4():
    def sat(nums: List[int], n=254723967601711775999551029856500295000994603):
        return len(nums) <= 4 and sum(i ** 2 for i in nums) == n

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_factoring():
    def sat(i: int, n=241864633):
        return 1 < i < n and n % i == 0

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_factoring_1():
    def sat(i: int, n=16):
        return 1 < i < n and n % i == 0

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_factoring_2():
    def sat(i: int, n=1522605027922533360535618378132637429718068114961380688657908494580122963258952897654000350692006139):
        return 1 < i < n and n % i == 0

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_factoring_3():
    def sat(i: int, n=35794234179725868774991807832568455403003778024228226193532908190484670252364677411513516111204504060317568667):
        return 1 < i < n and n % i == 0

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_factoring_4():
    def sat(i: int, n=3363):
        return 1 < i < n and n % i == 0

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_discretelog():
    def sat(n: int, g=44337, p=69337, t=38187):
        return pow(g, n, p) == t

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_discretelog_1():
    def sat(n: int, g=7, p=204706270385532838059744535166974274803608394340123459695798674591526591372685229510652847339705797622075505069831043486651682279, t=127402180119973946824269244334322849749382042586931621654557735290322914679095998681860978813046595166455458144280588076766033781):
        return pow(g, n, p) == t

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_discretelog_2():
    def sat(n: int, g=13, p=21, t=1):
        return pow(g, n, p) == t

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_discretelog_3():
    def sat(n: int, g=101873924449108026052, p=576036946901458671597, t=330515716425197141833):
        return pow(g, n, p) == t

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_discretelog_4():
    def sat(n: int, g=1696881788, p=8006168143, t=7111327686):
        return pow(g, n, p) == t

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_gcd17():
    def sat(n: int):
        i = n ** 17 + 9
        j = (n + 1) ** 17 + 9
    
        while i != 0:  # compute gcd using Euclid's algorithm
            (i, j) = (j % i, i)
    
        return n >= 0 and j != 1

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_znam():
    def sat(li: List[int], k=5):
        def prod(nums):
            ans = 1
            for i in nums:
                ans *= i
            return ans
    
        return min(li) > 1 and len(li) == k and all((1 + prod(li[:i] + li[i + 1:])) % li[i] == 0 for i in range(k))

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_znam_1():
    def sat(li: List[int], k=6):
        def prod(nums):
            ans = 1
            for i in nums:
                ans *= i
            return ans
    
        return min(li) > 1 and len(li) == k and all((1 + prod(li[:i] + li[i + 1:])) % li[i] == 0 for i in range(k))

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_znam_2():
    def sat(li: List[int], k=7):
        def prod(nums):
            ans = 1
            for i in nums:
                ans *= i
            return ans
    
        return min(li) > 1 and len(li) == k and all((1 + prod(li[:i] + li[i + 1:])) % li[i] == 0 for i in range(k))

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_znam_3():
    def sat(li: List[int], k=8):
        def prod(nums):
            ans = 1
            for i in nums:
                ans *= i
            return ans
    
        return min(li) > 1 and len(li) == k and all((1 + prod(li[:i] + li[i + 1:])) % li[i] == 0 for i in range(k))

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_collatzcycleunsolved():
    def sat(n: int):
        m = n
        while n > 4:
            n = 3 * n + 1 if n % 2 else n // 2
            if n == m:
                return True

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_collatzgeneralizedunsolved():
    def sat(start: int):
        n = start  # could be positive or negative ...
        while abs(n) > 1000:
            n = 3 * n + 1 if n % 2 else n // 2
            if n == start:
                return True

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_collatzdelay():
    def sat(n: int, t=197, upper=20):
        m = n
        for i in range(t):
            if n <= 1:
                return False
            n = 3 * n + 1 if n % 2 else n // 2
        return n == 1 and m <= 2 ** upper

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_collatzdelay_1():
    def sat(n: int, t=1000, upper=150):
        m = n
        for i in range(t):
            if n <= 1:
                return False
            n = 3 * n + 1 if n % 2 else n // 2
        return n == 1 and m <= 2 ** upper

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_collatzdelay_2():
    def sat(n: int, t=2000, upper=206):
        m = n
        for i in range(t):
            if n <= 1:
                return False
            n = 3 * n + 1 if n % 2 else n // 2
        return n == 1 and m <= 2 ** upper

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_collatzdelay_3():
    def sat(n: int, t=2283, upper=238):
        m = n
        for i in range(t):
            if n <= 1:
                return False
            n = 3 * n + 1 if n % 2 else n // 2
        return n == 1 and m <= 2 ** upper

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_lehmer():
    def sat(n: int):
        return pow(2, n, n) == 3

    assert False
