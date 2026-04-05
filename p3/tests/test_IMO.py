from typing import List

import pytest


@pytest.mark.skip(reason="not implemented yet")
def test_exponentialcoinmoves():
    def sat(states: List[List[int]], n=16385):
        assert (
            states[0] == [1] * 5
            and all(len(li) == 5 for li in states)
            and all(i >= 0 for li in states for i in li)
        )
        for prev, cur in zip(states, states[1:]):
            for i in range(5):
                if cur[i] != prev[i]:
                    break
            assert cur[i] < prev[i]
            assert (
                cur[i + 1] - prev[i + 1] == 2 * (prev[i] - cur[i])
                and cur[i + 2 :] == prev[i + 2 :]  # k decrements
                or cur[i : i + 3] == [prev[i] - 1, prev[i + 2], prev[i + 1]]
                and cur[i + 3 :] == prev[i + 3 :]  # swap
            )

        return states[-1][-1] == 2**n

    assert sat(...)


@pytest.mark.skip(reason="not implemented yet")
def test_exponentialcoinmoves_1():
    def sat(states: List[List[int]], n=1):
        assert (
            states[0] == [1] * 5
            and all(len(li) == 5 for li in states)
            and all(i >= 0 for li in states for i in li)
        )
        for prev, cur in zip(states, states[1:]):
            for i in range(5):
                if cur[i] != prev[i]:
                    break
            assert cur[i] < prev[i]
            assert (
                cur[i + 1] - prev[i + 1] == 2 * (prev[i] - cur[i])
                and cur[i + 2 :] == prev[i + 2 :]  # k decrements
                or cur[i : i + 3] == [prev[i] - 1, prev[i + 2], prev[i + 1]]
                and cur[i + 3 :] == prev[i + 3 :]  # swap
            )

        return states[-1][-1] == 2**n

    assert sat(...)


@pytest.mark.skip(reason="not implemented yet")
def test_exponentialcoinmoves_2():
    def sat(states: List[List[int]], n=2):
        assert (
            states[0] == [1] * 5
            and all(len(li) == 5 for li in states)
            and all(i >= 0 for li in states for i in li)
        )
        for prev, cur in zip(states, states[1:]):
            for i in range(5):
                if cur[i] != prev[i]:
                    break
            assert cur[i] < prev[i]
            assert (
                cur[i + 1] - prev[i + 1] == 2 * (prev[i] - cur[i])
                and cur[i + 2 :] == prev[i + 2 :]  # k decrements
                or cur[i : i + 3] == [prev[i] - 1, prev[i + 2], prev[i + 1]]
                and cur[i + 3 :] == prev[i + 3 :]  # swap
            )

        return states[-1][-1] == 2**n

    assert sat(...)


@pytest.mark.skip(reason="not implemented yet")
def test_exponentialcoinmoves_3():
    def sat(states: List[List[int]], n=4):
        assert (
            states[0] == [1] * 5
            and all(len(li) == 5 for li in states)
            and all(i >= 0 for li in states for i in li)
        )
        for prev, cur in zip(states, states[1:]):
            for i in range(5):
                if cur[i] != prev[i]:
                    break
            assert cur[i] < prev[i]
            assert (
                cur[i + 1] - prev[i + 1] == 2 * (prev[i] - cur[i])
                and cur[i + 2 :] == prev[i + 2 :]  # k decrements
                or cur[i : i + 3] == [prev[i] - 1, prev[i + 2], prev[i + 1]]
                and cur[i + 3 :] == prev[i + 3 :]  # swap
            )

        return states[-1][-1] == 2**n

    assert sat(...)


@pytest.mark.skip(reason="not implemented yet")
def test_exponentialcoinmoves_4():
    def sat(states: List[List[int]], n=8):
        assert (
            states[0] == [1] * 5
            and all(len(li) == 5 for li in states)
            and all(i >= 0 for li in states for i in li)
        )
        for prev, cur in zip(states, states[1:]):
            for i in range(5):
                if cur[i] != prev[i]:
                    break
            assert cur[i] < prev[i]
            assert (
                cur[i + 1] - prev[i + 1] == 2 * (prev[i] - cur[i])
                and cur[i + 2 :] == prev[i + 2 :]  # k decrements
                or cur[i : i + 3] == [prev[i] - 1, prev[i + 2], prev[i + 1]]
                and cur[i + 3 :] == prev[i + 3 :]  # swap
            )

        return states[-1][-1] == 2**n

    assert sat(...)


@pytest.mark.skip(reason="not implemented yet")
def test_norelativeprimes():
    def sat(nums: List[int], b=7, m=6):
        assert len(nums) == len(set(nums)) == m and min(nums) >= 0

        def gcd(i, j):
            r, s = max(i, j), min(i, j)
            while s >= 1:
                r, s = s, (r % s)
            return r

        for a in nums:
            nums = [(a + i + 1) ** 2 + (a + i + 1) + 1 for i in range(b)]
            assert all(any(i != j and gcd(i, j) > 1 for j in nums) for i in nums)

        return True

    assert sat(...)


@pytest.mark.skip(reason="not implemented yet")
def test_norelativeprimes_1():
    def sat(nums: List[int], b=7, m=26):
        assert len(nums) == len(set(nums)) == m and min(nums) >= 0

        def gcd(i, j):
            r, s = max(i, j), min(i, j)
            while s >= 1:
                r, s = s, (r % s)
            return r

        for a in nums:
            nums = [(a + i + 1) ** 2 + (a + i + 1) + 1 for i in range(b)]
            assert all(any(i != j and gcd(i, j) > 1 for j in nums) for i in nums)

        return True

    assert sat(...)


@pytest.mark.skip(reason="not implemented yet")
def test_norelativeprimes_2():
    def sat(nums: List[int], b=6, m=73):
        assert len(nums) == len(set(nums)) == m and min(nums) >= 0

        def gcd(i, j):
            r, s = max(i, j), min(i, j)
            while s >= 1:
                r, s = s, (r % s)
            return r

        for a in nums:
            nums = [(a + i + 1) ** 2 + (a + i + 1) + 1 for i in range(b)]
            assert all(any(i != j and gcd(i, j) > 1 for j in nums) for i in nums)

        return True

    assert sat(...)


@pytest.mark.skip(reason="not implemented yet")
def test_norelativeprimes_3():
    def sat(nums: List[int], b=17, m=37):
        assert len(nums) == len(set(nums)) == m and min(nums) >= 0

        def gcd(i, j):
            r, s = max(i, j), min(i, j)
            while s >= 1:
                r, s = s, (r % s)
            return r

        for a in nums:
            nums = [(a + i + 1) ** 2 + (a + i + 1) + 1 for i in range(b)]
            assert all(any(i != j and gcd(i, j) > 1 for j in nums) for i in nums)

        return True

    assert sat(...)


@pytest.mark.skip(reason="not implemented yet")
def test_norelativeprimes_4():
    def sat(nums: List[int], b=7, m=92):
        assert len(nums) == len(set(nums)) == m and min(nums) >= 0

        def gcd(i, j):
            r, s = max(i, j), min(i, j)
            while s >= 1:
                r, s = s, (r % s)
            return r

        for a in nums:
            nums = [(a + i + 1) ** 2 + (a + i + 1) + 1 for i in range(b)]
            assert all(any(i != j and gcd(i, j) > 1 for j in nums) for i in nums)

        return True

    assert sat(...)


@pytest.mark.skip(reason="not implemented yet")
def test_findrepeats():
    def sat(indices: List[int], a0=123):
        assert a0 >= 0 and a0 % 3 == 0, "Hint: a_0 is a multiple of 3."
        s = [a0]
        for i in range(max(indices)):
            s.append(
                int(s[-1] ** 0.5) if int(s[-1] ** 0.5) ** 2 == s[-1] else s[-1] + 3
            )
        return (
            len(indices) == len(set(indices)) == 1000
            and min(indices) >= 0
            and len({s[i] for i in indices}) == 1
        )

    assert sat(...)


@pytest.mark.skip(reason="not implemented yet")
def test_findrepeats_1():
    def sat(indices: List[int], a0=2827347):
        assert a0 >= 0 and a0 % 3 == 0, "Hint: a_0 is a multiple of 3."
        s = [a0]
        for i in range(max(indices)):
            s.append(
                int(s[-1] ** 0.5) if int(s[-1] ** 0.5) ** 2 == s[-1] else s[-1] + 3
            )
        return (
            len(indices) == len(set(indices)) == 1000
            and min(indices) >= 0
            and len({s[i] for i in indices}) == 1
        )

    assert sat(...)


@pytest.mark.skip(reason="not implemented yet")
def test_findrepeats_2():
    def sat(indices: List[int], a0=2362263):
        assert a0 >= 0 and a0 % 3 == 0, "Hint: a_0 is a multiple of 3."
        s = [a0]
        for i in range(max(indices)):
            s.append(
                int(s[-1] ** 0.5) if int(s[-1] ** 0.5) ** 2 == s[-1] else s[-1] + 3
            )
        return (
            len(indices) == len(set(indices)) == 1000
            and min(indices) >= 0
            and len({s[i] for i in indices}) == 1
        )

    assert sat(...)


@pytest.mark.skip(reason="not implemented yet")
def test_findrepeats_3():
    def sat(indices: List[int], a0=1703235):
        assert a0 >= 0 and a0 % 3 == 0, "Hint: a_0 is a multiple of 3."
        s = [a0]
        for i in range(max(indices)):
            s.append(
                int(s[-1] ** 0.5) if int(s[-1] ** 0.5) ** 2 == s[-1] else s[-1] + 3
            )
        return (
            len(indices) == len(set(indices)) == 1000
            and min(indices) >= 0
            and len({s[i] for i in indices}) == 1
        )

    assert sat(...)


@pytest.mark.skip(reason="not implemented yet")
def test_findrepeats_4():
    def sat(indices: List[int], a0=962856):
        assert a0 >= 0 and a0 % 3 == 0, "Hint: a_0 is a multiple of 3."
        s = [a0]
        for i in range(max(indices)):
            s.append(
                int(s[-1] ** 0.5) if int(s[-1] ** 0.5) ** 2 == s[-1] else s[-1] + 3
            )
        return (
            len(indices) == len(set(indices)) == 1000
            and min(indices) >= 0
            and len({s[i] for i in indices}) == 1
        )

    assert sat(...)


@pytest.mark.skip(reason="not implemented yet")
def test_picknearneighbors():
    def sat(
        keep: List[bool],
        heights=[10, 2, 14, 1, 8, 19, 16, 6, 12, 3, 17, 0, 9, 18, 5, 7, 11, 13, 15, 4],
    ):
        n = int(len(heights) ** 0.5)
        assert sorted(heights) == list(range(n * n + n)), (
            "hint: heights is a permutation of range(n * n + n)"
        )
        kept = [i for i, k in zip(heights, keep) if k]
        assert len(kept) == 2 * n, "must keep 2n items"
        pi = sorted(range(2 * n), key=lambda i: kept[i])  # the sort indices
        return all(abs(pi[2 * i] - pi[2 * i + 1]) == 1 for i in range(n))

    assert sat(...)


@pytest.mark.skip(reason="not implemented yet")
def test_picknearneighbors_1():
    def sat(
        keep: List[bool],
        heights=[
            6,
            12,
            26,
            4,
            25,
            20,
            15,
            14,
            18,
            22,
            19,
            23,
            27,
            13,
            9,
            28,
            17,
            11,
            29,
            7,
            1,
            10,
            2,
            0,
            21,
            3,
            5,
            8,
            16,
            24,
        ],
    ):
        n = int(len(heights) ** 0.5)
        assert sorted(heights) == list(range(n * n + n)), (
            "hint: heights is a permutation of range(n * n + n)"
        )
        kept = [i for i, k in zip(heights, keep) if k]
        assert len(kept) == 2 * n, "must keep 2n items"
        pi = sorted(range(2 * n), key=lambda i: kept[i])  # the sort indices
        return all(abs(pi[2 * i] - pi[2 * i + 1]) == 1 for i in range(n))

    assert sat(...)


@pytest.mark.skip(reason="not implemented yet")
def test_picknearneighbors_2():
    def sat(keep: List[bool], heights=[6, 8, 0, 7, 4, 9, 10, 1, 5, 3, 11, 2]):
        n = int(len(heights) ** 0.5)
        assert sorted(heights) == list(range(n * n + n)), (
            "hint: heights is a permutation of range(n * n + n)"
        )
        kept = [i for i, k in zip(heights, keep) if k]
        assert len(kept) == 2 * n, "must keep 2n items"
        pi = sorted(range(2 * n), key=lambda i: kept[i])  # the sort indices
        return all(abs(pi[2 * i] - pi[2 * i + 1]) == 1 for i in range(n))

    assert sat(...)


@pytest.mark.skip(reason="not implemented yet")
def test_picknearneighbors_3():
    def sat(
        keep: List[bool],
        heights=[
            46,
            61,
            80,
            16,
            71,
            32,
            13,
            12,
            2,
            75,
            62,
            56,
            17,
            28,
            67,
            54,
            22,
            27,
            38,
            63,
            69,
            84,
            70,
            57,
            86,
            72,
            66,
            8,
            41,
            3,
            23,
            88,
            83,
            58,
            36,
            50,
            65,
            30,
            34,
            25,
            39,
            20,
            78,
            79,
            59,
            4,
            21,
            73,
            45,
            37,
            48,
            77,
            10,
            44,
            14,
            43,
            42,
            0,
            33,
            29,
            7,
            52,
            5,
            60,
            68,
            9,
            26,
            49,
            40,
            76,
            31,
            6,
            85,
            74,
            24,
            51,
            1,
            89,
            11,
            47,
            18,
            19,
            81,
            87,
            35,
            64,
            82,
            15,
            55,
            53,
        ],
    ):
        n = int(len(heights) ** 0.5)
        assert sorted(heights) == list(range(n * n + n)), (
            "hint: heights is a permutation of range(n * n + n)"
        )
        kept = [i for i, k in zip(heights, keep) if k]
        assert len(kept) == 2 * n, "must keep 2n items"
        pi = sorted(range(2 * n), key=lambda i: kept[i])  # the sort indices
        return all(abs(pi[2 * i] - pi[2 * i + 1]) == 1 for i in range(n))

    assert sat(...)


@pytest.mark.skip(reason="not implemented yet")
def test_picknearneighbors_4():
    def sat(
        keep: List[bool],
        heights=[
            26,
            11,
            62,
            24,
            56,
            80,
            39,
            77,
            23,
            86,
            53,
            73,
            3,
            44,
            45,
            70,
            75,
            0,
            13,
            40,
            4,
            87,
            30,
            7,
            50,
            34,
            59,
            22,
            17,
            41,
            71,
            10,
            29,
            89,
            36,
            31,
            52,
            9,
            2,
            51,
            28,
            61,
            21,
            1,
            15,
            72,
            84,
            88,
            79,
            19,
            27,
            63,
            55,
            83,
            57,
            18,
            5,
            12,
            37,
            16,
            49,
            8,
            6,
            65,
            32,
            20,
            47,
            82,
            42,
            33,
            81,
            58,
            35,
            67,
            48,
            74,
            78,
            85,
            14,
            68,
            43,
            25,
            46,
            69,
            76,
            64,
            38,
            54,
            66,
            60,
        ],
    ):
        n = int(len(heights) ** 0.5)
        assert sorted(heights) == list(range(n * n + n)), (
            "hint: heights is a permutation of range(n * n + n)"
        )
        kept = [i for i, k in zip(heights, keep) if k]
        assert len(kept) == 2 * n, "must keep 2n items"
        pi = sorted(range(2 * n), key=lambda i: kept[i])  # the sort indices
        return all(abs(pi[2 * i] - pi[2 * i + 1]) == 1 for i in range(n))

    assert sat(...)


@pytest.mark.skip(reason="not implemented yet")
def test_findproductivelist():
    def sat(li: List[int], n=18):
        assert n % 3 == 0, "Hint: n is a multiple of 3"
        return len(li) == n and all(
            li[(i + 2) % n] == 1 + li[(i + 1) % n] * li[i] for i in range(n)
        )

    assert sat(...)


@pytest.mark.skip(reason="not implemented yet")
def test_findproductivelist_1():
    def sat(li: List[int], n=3):
        assert n % 3 == 0, "Hint: n is a multiple of 3"
        return len(li) == n and all(
            li[(i + 2) % n] == 1 + li[(i + 1) % n] * li[i] for i in range(n)
        )

    assert sat(...)


@pytest.mark.skip(reason="not implemented yet")
def test_findproductivelist_2():
    def sat(li: List[int], n=6):
        assert n % 3 == 0, "Hint: n is a multiple of 3"
        return len(li) == n and all(
            li[(i + 2) % n] == 1 + li[(i + 1) % n] * li[i] for i in range(n)
        )

    assert sat(...)


@pytest.mark.skip(reason="not implemented yet")
def test_findproductivelist_3():
    def sat(li: List[int], n=9):
        assert n % 3 == 0, "Hint: n is a multiple of 3"
        return len(li) == n and all(
            li[(i + 2) % n] == 1 + li[(i + 1) % n] * li[i] for i in range(n)
        )

    assert sat(...)


@pytest.mark.skip(reason="not implemented yet")
def test_findproductivelist_4():
    def sat(li: List[int], n=12):
        assert n % 3 == 0, "Hint: n is a multiple of 3"
        return len(li) == n and all(
            li[(i + 2) % n] == 1 + li[(i + 1) % n] * li[i] for i in range(n)
        )

    assert sat(...)


@pytest.mark.skip(reason="not implemented yet")
def test_halftag():
    def sat(li: List[int], tags=[3, 0, 3, 2, 0, 1, 0, 3, 1, 1, 2, 2, 0, 2, 1, 3]):
        n = max(tags) + 1
        assert sorted(tags) == sorted(list(range(n)) * 4), (
            "hint: each tag occurs exactly four times"
        )
        assert len(li) == len(set(li)) and min(li) >= 0
        return sum(li) * 2 == sum(range(4 * n)) and sorted([tags[i] for i in li]) == [
            i // 2 for i in range(2 * n)
        ]

    assert sat(...)


@pytest.mark.skip(reason="not implemented yet")
def test_halftag_1():
    def sat(li: List[int], tags=[2, 3, 1, 0, 3, 3, 0, 2, 1, 3, 1, 0, 1, 2, 2, 0]):
        n = max(tags) + 1
        assert sorted(tags) == sorted(list(range(n)) * 4), (
            "hint: each tag occurs exactly four times"
        )
        assert len(li) == len(set(li)) and min(li) >= 0
        return sum(li) * 2 == sum(range(4 * n)) and sorted([tags[i] for i in li]) == [
            i // 2 for i in range(2 * n)
        ]

    assert sat(...)


@pytest.mark.skip(reason="not implemented yet")
def test_halftag_2():
    def sat(
        li: List[int],
        tags=[
            4,
            1,
            6,
            5,
            6,
            4,
            2,
            1,
            6,
            2,
            3,
            1,
            4,
            6,
            5,
            2,
            3,
            5,
            0,
            5,
            0,
            3,
            0,
            0,
            4,
            2,
            3,
            1,
        ],
    ):
        n = max(tags) + 1
        assert sorted(tags) == sorted(list(range(n)) * 4), (
            "hint: each tag occurs exactly four times"
        )
        assert len(li) == len(set(li)) and min(li) >= 0
        return sum(li) * 2 == sum(range(4 * n)) and sorted([tags[i] for i in li]) == [
            i // 2 for i in range(2 * n)
        ]

    assert sat(...)


@pytest.mark.skip(reason="not implemented yet")
def test_halftag_3():
    def sat(li: List[int], tags=[0, 2, 1, 1, 1, 1, 2, 2, 0, 0, 0, 2]):
        n = max(tags) + 1
        assert sorted(tags) == sorted(list(range(n)) * 4), (
            "hint: each tag occurs exactly four times"
        )
        assert len(li) == len(set(li)) and min(li) >= 0
        return sum(li) * 2 == sum(range(4 * n)) and sorted([tags[i] for i in li]) == [
            i // 2 for i in range(2 * n)
        ]

    assert sat(...)


@pytest.mark.skip(reason="not implemented yet")
def test_halftag_4():
    def sat(
        li: List[int],
        tags=[
            1,
            2,
            6,
            0,
            6,
            2,
            4,
            7,
            4,
            0,
            0,
            5,
            0,
            3,
            2,
            1,
            7,
            5,
            5,
            3,
            1,
            7,
            2,
            7,
            6,
            6,
            3,
            3,
            1,
            4,
            4,
            5,
        ],
    ):
        n = max(tags) + 1
        assert sorted(tags) == sorted(list(range(n)) * 4), (
            "hint: each tag occurs exactly four times"
        )
        assert len(li) == len(set(li)) and min(li) >= 0
        return sum(li) * 2 == sum(range(4 * n)) and sorted([tags[i] for i in li]) == [
            i // 2 for i in range(2 * n)
        ]

    assert sat(...)
