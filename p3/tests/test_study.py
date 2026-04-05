import pytest


def test_study1():
    def sat(s: str):
        return s.count("o") == 1000 and s.count("oo") == 0

    assert sat("o " * 1000)


@pytest.mark.skip(reason="not implemented yet")
def test_study2():
    def sat(s: str):
        return s.count("o") == 1000 and s.count("oo") == 0

    assert False
