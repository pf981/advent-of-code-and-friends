from typing import List


def test_tutorial1():
    def sat(s: str):
        return "Hello " + s == "Hello world"

    assert sat("world")


def test_tutorial2():
    def sat(s: str):
        return "Hello " + s[::-1] == "Hello world"

    assert sat("world"[::-1])


def test_tutorial3():
    def sat(x: List[int]):
        return len(x) == 2 and sum(x) == 3

    assert sat([1, 2])


def test_tutorial4():
    def sat(s: List[str]):
        return len(set(s)) == 1000 and all(
            (x.count("a") > x.count("b")) and ("b" in x) for x in s
        )

    assert sat(["a" * i + "aab" for i in range(1000)])


def test_tutorial5():
    def sat(n: int):
        return str(n * n).startswith("123456789")

    import math

    assert sat(math.isqrt(123456789_5555555555))
