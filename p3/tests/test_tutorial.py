from typing import List

import pytest


@pytest.mark.skip(reason="not implemented yet")
def test_tutorial1():
    def sat(s: str):
        return "Hello " + s == "Hello world"

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_tutorial2():
    def sat(s: str):
        return "Hello " + s[::-1] == "Hello world"

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_tutorial3():
    def sat(x: List[int]):
        return len(x) == 2 and sum(x) == 3

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_tutorial4():
    def sat(s: List[str]):
        return len(set(s)) == 1000 and all((x.count("a") > x.count("b")) and ('b' in x) for x in s)

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_tutorial5():
    def sat(n: int):
        return str(n * n).startswith("123456789")

    assert False
