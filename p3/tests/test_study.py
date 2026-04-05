from typing import List


def test_study_1():
    def sat(s: str):
        return s.count("o") == 1000 and s.count("oo") == 0

    assert sat("o " * 1000)


def test_study_2():
    def sat(s: str):
        return s.count("o") == 1000 and s.count("oo") == 100 and s.count("ho") == 801

    assert sat("ho" * 800 + "h" + "o" * 200)


def test_study_3():
    def sat(li: List[int]):
        return sorted(li) == list(range(999)) and all(
            li[i] != i for i in range(len(li))
        )

    assert sat(list(range(1, 999)) + [0])


def test_study_4():
    def sat(li: List[int]):
        return len(li) == 10 and li.count(li[3]) == 2

    assert [0, 0, 0, 1, 1, 0, 0, 0, 0, 0]


def test_study_5():
    def sat(li: List[int]):
        return all([li.count(i) == i for i in range(10)])

    assert sat([i for ll in [[i] * i for i in range(10)] for i in ll])


def test_study_6():
    def sat(i: int):
        return i % 123 == 4 and i > 10**10

    import itertools

    assert sat(next(i for i in itertools.count(10**10 + 1) if i % 123 == 4))


def test_study_7():
    def sat(s: str):
        return str(8**2888).count(s) > 8 and len(s) == 3

    target = str(8**2888)
    assert sat(next(s for i in range(1000) if target.count(s := f"{i:<03}") > 8))


def test_study_8():
    def sat(ls: List[str]):
        return ls[1234] in ls[1235] and ls[1234] != ls[1235]

    assert sat([""] * 1235 + ["x"])


def test_study_9():
    def sat(li: List[int]):
        return ["The quick brown fox jumps over the lazy dog"[i] for i in li] == list(
            "The five boxing wizards jump quickly"
        )

    assert sat(
        [
            "The quick brown fox jumps over the lazy dog".index(c)
            for c in "The five boxing wizards jump quickly"
        ]
    )


def test_study_10():
    def sat(s: str):
        return s in str(8**1818) and s == s[::-1] and len(s) > 11

    target = str(8**1818)
    for w in range(12, len(target)):
        for i in range(len(target) - w):
            s = target[i : i + w]
            if s == s[::-1]:
                break
        else:
            continue
        break

    assert sat(s)


def test_study_11():
    def sat(ls: List[str]):
        return min(ls) == max(ls) == str(len(ls))

    assert sat(["1"])


def test_study_12():
    def sat(li: List[int]):
        return all(i + j == 9 for i, j in zip([4] + li, li)) and len(li) == 1000

    assert sat([5, 4] * 500)


def test_study_13():
    def sat(x: float):
        return str(x - 3.1415).startswith("123.456")

    assert sat(123.456 + 3.1415)


def test_study_14():
    def sat(li: List[int]):
        return all([sum(li[:i]) == i for i in range(20)])

    assert sat([1] * 20)


def test_study_15():
    def sat(li: List[int]):
        return all(sum(li[:i]) == 2**i - 1 for i in range(20))

    s = 0
    assert [(s := 2**i - 1 - s) for i in range(20)]


def test_study_16():
    def sat(s: str):
        return float(s) + len(s) == 4.5

    assert sat("1.5")


def test_study_17():
    def sat(i: int):
        return len(str(i + 1000)) > len(str(i + 1001))

    assert sat(-1 - 1000)


def test_study_18():
    def sat(ls: List[str]):
        return [
            s + t for s in ls for t in ls if s != t
        ] == "berlin berger linber linger gerber gerlin".split()

    assert sat(["ber", "lin", "ger"])


def test_study_19():
    def sat(li: List[int]):
        return {i + j for i in li for j in li} == {
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            17,
            18,
            19,
            20,
            34,
        }

    assert sat([0, 1, 2, 3, 17])


def test_study_20():
    def sat(li: List[int]):
        return all(j in {i - 1, i + 1, 3 * i} for i, j in zip([0] + li, li + [128]))

    assert sat(list(range(128)))


def test_study_21():
    def sat(li: List[int]):
        return all([li[i] != li[i + 1] for i in range(10)]) and len(set(li)) == 3

    assert sat([0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1])


def test_study_22():
    def sat(s: str):
        return s[::2] in s and len(set(s)) == 5

    assert sat("a" * 20 + "abacadae")


def test_study_23():
    def sat(ls: List[str]):
        return tuple(ls) in zip("dee", "doo", "dah!")

    assert sat(["d", "d", "d"])


def test_study_24():
    def sat(li: List[int]):
        return li.count(17) == 3 and li.count(3) >= 2

    assert sat([17] * 3 + [3] * 3)


def test_study_25():
    def sat(s: str):
        return sorted(s) == sorted("Permute me true") and s == s[::-1]

    assert sat("eurt emPme true")


def test_study_26():
    def sat(ls: List[str]):
        return "".join(ls) == str(8**88) and all(len(s) == 8 for s in ls)

    target = str(8**88)
    ls = [target[i : i + 8] for i in range(0, len(target), 8)]

    assert sat(ls)


def test_study_27():
    def sat(li: List[int]):
        return li[li[0]] != li[li[1]] and li[li[li[0]]] == li[li[li[1]]]

    assert sat([1, 2, 3, 3])


def test_study_28():
    def sat(li: List[int]):
        return (
            all(i in range(1000) and abs(i - j) >= 10 for i in li for j in li if i != j)
            and len(set(li)) == 100
        )

    assert sat(list(range(0, 1000, 10)))


def test_study_29():
    def sat(li: List[int]):
        return (
            all(
                i in range(1000) and abs(i * i - j * j) >= 10
                for i in li
                for j in li
                if i != j
            )
            and len(set(li)) > 995
        )

    assert sat(list(range(5, 1000)) + [2])


def test_study_30():
    def sat(li: List[int]):
        return all(
            [
                123 * li[i] % 1000 < 123 * li[i + 1] % 1000 and li[i] in range(1000)
                for i in range(20)
            ]
        )

    vals = sorted(range(1000), key=lambda i: 123 * i % 1000)
    assert sat(vals[:21])
