from typing import List

import pytest


@pytest.mark.skip(reason="not implemented yet")
def test_lzw():
    def sat(seq: List[int], compressed_len=17, text="Hellooooooooooooooooooooo world!"):
        index = [chr(i) for i in range(256)]
        pieces = [""]
        for i in seq:
            pieces.append((pieces[-1] + pieces[-1][0]) if i == len(index) else index[i])
            index.append(pieces[-2] + pieces[-1][0])
        return "".join(pieces) == text and len(seq) <= compressed_len

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_lzw_1():
    def sat(seq: List[int], compressed_len=0, text=""):
        index = [chr(i) for i in range(256)]
        pieces = [""]
        for i in seq:
            pieces.append((pieces[-1] + pieces[-1][0]) if i == len(index) else index[i])
            index.append(pieces[-2] + pieces[-1][0])
        return "".join(pieces) == text and len(seq) <= compressed_len

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_lzw_2():
    def sat(seq: List[int], compressed_len=45, text="cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc"):
        index = [chr(i) for i in range(256)]
        pieces = [""]
        for i in seq:
            pieces.append((pieces[-1] + pieces[-1][0]) if i == len(index) else index[i])
            index.append(pieces[-2] + pieces[-1][0])
        return "".join(pieces) == text and len(seq) <= compressed_len

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_lzw_3():
    def sat(seq: List[int], compressed_len=154, text="cupewoquabipemecacichytogycykythyzydizutextojokosapysetextethilabequypagichichimipyhuquithyzuwukychycokigomylotextoquochachikalocejiwyzagodothilythetiquypirabafusubasufylejulitudosisyrahezitextoluquevy"):
        index = [chr(i) for i in range(256)]
        pieces = [""]
        for i in seq:
            pieces.append((pieces[-1] + pieces[-1][0]) if i == len(index) else index[i])
            index.append(pieces[-2] + pieces[-1][0])
        return "".join(pieces) == text and len(seq) <= compressed_len

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_lzw_4():
    def sat(seq: List[int], compressed_len=2, text="si"):
        index = [chr(i) for i in range(256)]
        pieces = [""]
        for i in seq:
            pieces.append((pieces[-1] + pieces[-1][0]) if i == len(index) else index[i])
            index.append(pieces[-2] + pieces[-1][0])
        return "".join(pieces) == text and len(seq) <= compressed_len

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_packingham():
    def sat(words: List[str], num=100, bits=100, dist=34):
        assert len(words) == num and all(len(word) == bits and set(word) <= {"0", "1"} for word in words)
        return all(sum([a != b for a, b in zip(words[i], words[j])]) >= dist for i in range(num) for j in range(i))

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_packingham_1():
    def sat(words: List[str], num=5, bits=81, dist=30):
        assert len(words) == num and all(len(word) == bits and set(word) <= {"0", "1"} for word in words)
        return all(sum([a != b for a, b in zip(words[i], words[j])]) >= dist for i in range(num) for j in range(i))

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_packingham_2():
    def sat(words: List[str], num=78, bits=64, dist=16):
        assert len(words) == num and all(len(word) == bits and set(word) <= {"0", "1"} for word in words)
        return all(sum([a != b for a, b in zip(words[i], words[j])]) >= dist for i in range(num) for j in range(i))

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_packingham_3():
    def sat(words: List[str], num=28, bits=11, dist=1):
        assert len(words) == num and all(len(word) == bits and set(word) <= {"0", "1"} for word in words)
        return all(sum([a != b for a, b in zip(words[i], words[j])]) >= dist for i in range(num) for j in range(i))

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_packingham_4():
    def sat(words: List[str], num=8, bits=75, dist=24):
        assert len(words) == num and all(len(word) == bits and set(word) <= {"0", "1"} for word in words)
        return all(sum([a != b for a, b in zip(words[i], words[j])]) >= dist for i in range(num) for j in range(i))

    assert False
