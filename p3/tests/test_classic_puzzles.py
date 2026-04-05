from typing import List

import pytest


@pytest.mark.skip(reason="not implemented yet")
def test_towersofhanoi():
    def sat(moves: List[List[int]]):
        rods = ([8, 7, 6, 5, 4, 3, 2, 1], [], [])
        for [i, j] in moves:
            rods[j].append(rods[i].pop())
            assert rods[j][-1] == min(rods[j]), "larger disk on top of smaller disk"
        return rods[0] == rods[1] == []

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_towersofhanoiarbitrary():
    def sat(moves: List[List[int]], source=[[0, 7], [4, 5, 6], [1, 2, 3, 8]], target=[[0, 1, 2, 3, 8], [4, 5], [6, 7]]):
        state = [s[:] for s in source]
    
        for [i, j] in moves:
            state[j].append(state[i].pop())
            assert state[j] == sorted(state[j])
    
        return state == target

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_towersofhanoiarbitrary_1():
    def sat(moves: List[List[int]], source=[[1, 3, 5], [2, 8, 14], [0, 4, 6, 7, 9, 10, 11, 12, 13]], target=[[5, 12], [0, 3, 4, 7, 10, 11], [1, 2, 6, 8, 9, 13, 14]]):
        state = [s[:] for s in source]
    
        for [i, j] in moves:
            state[j].append(state[i].pop())
            assert state[j] == sorted(state[j])
    
        return state == target

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_towersofhanoiarbitrary_2():
    def sat(moves: List[List[int]], source=[[0, 1, 6, 7, 8, 9, 14, 16], [5, 15], [2, 3, 4, 10, 11, 12, 13]], target=[[1, 2, 4, 5, 13], [3, 6, 11, 12, 14], [0, 7, 8, 9, 10, 15, 16]]):
        state = [s[:] for s in source]
    
        for [i, j] in moves:
            state[j].append(state[i].pop())
            assert state[j] == sorted(state[j])
    
        return state == target

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_towersofhanoiarbitrary_3():
    def sat(moves: List[List[int]], source=[[2, 11, 12, 16], [1, 3, 6, 8, 9, 10, 13], [0, 4, 5, 7, 14, 15]], target=[[0, 2, 3, 5, 7, 8, 14, 16], [9, 11, 12, 13, 15], [1, 4, 6, 10]]):
        state = [s[:] for s in source]
    
        for [i, j] in moves:
            state[j].append(state[i].pop())
            assert state[j] == sorted(state[j])
    
        return state == target

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_towersofhanoiarbitrary_4():
    def sat(moves: List[List[int]], source=[[5, 6], [1, 2, 4], [0, 3]], target=[[2, 3, 4, 6], [0, 1], [5]]):
        state = [s[:] for s in source]
    
        for [i, j] in moves:
            state[j].append(state[i].pop())
            assert state[j] == sorted(state[j])
    
        return state == target

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_longestmonotonicsubstring():
    def sat(x: List[int], length=13, s="Dynamic programming solves this puzzle!!!"):
        return all(s[x[i]] <= s[x[i + 1]] and x[i + 1] > x[i] >= 0 for i in range(length - 1))

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_longestmonotonicsubstring_1():
    def sat(x: List[int], length=193, s="    !!\"\"\"#$$%&&')''((()!))****X**++,,,,---...///0111114445556888::::;s;;<<==,=>>>>ABBBBBCDEEEEEEEFGHIIKKKKLMNOOPPPQQQRRRRASUUUVVVWWXXZZZ[]]]!``aEaabbbccccPcdeeeeefghjjjjkkkllmmooooKpppppqsttwt'$ww=wLwwyyyyzz{"):
        return all(s[x[i]] <= s[x[i + 1]] and x[i + 1] > x[i] >= 0 for i in range(length - 1))

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_longestmonotonicsubstring_2():
    def sat(x: List[int], length=737, s="    _   !m!!!!!!!!!!!V!\"=\"\"\"\"\"l#####$$r$$$$$$$$$%%%%%&&&&&&y&''''''@'''''<(((())))))******+++++++p,,,,,!,-----w-----o-....,.......//////D000000000000111111111222222,23h33c33334444444'4455555555566666R6@9777777T7888888-8994999999999::::::::::;;;;;;;P;;;<<<:<<^<)<<sn<<<====u=*=>>>>>>>>>???A?j??8??.?@@O@@@@@@ArAA&ABBBBBBBBBCCCCCDDDEEEEEEEEE%E(EEEEEFF!FFG-GGGGGGGGHHCHHHIGIsIIIInIIIIJJJRJFJJKKKKKKa0K<KKLL.LLLLLLMMMnMMM_MMMNNNONNOOOOOPPPP4LPPPPQQ\\QQQbQQQ7QQRRRRR\"RRSSSSSSTTgTTTTUUtUUUUUVVVVVVVVVVVqVVVMWWRWWWWWWWW%XXXXXXXXXXYYYYYZZZZZZZZZ2y[S[[[I[[[[\\$g\"\\\\\\\\T]]]]]]]]]]^^o^^______________`?&`I`y````aaaaaabbbbcccccc3ddddIu;L*dddeeee#eee]ffff1f]=fffffffffgggghhxhhhhhhiigiiiiiiiDiiCiiiijLjjIljjjjjjjkklllllmmmmJymmmmnnnnMnnnnnnoooiobooXoopppppqy5qqqdqqrrIrrrrJrssssssssTsstt'ttttZttt@tttuluuuuu0uuuvvxvvvv\\vv3vvvvwwwwwwba.wwx4xxxxxxxxxxxxxJyyyyyyyyyyzzzzzzzz{{{{{{{{"):
        return all(s[x[i]] <= s[x[i + 1]] and x[i + 1] > x[i] >= 0 for i in range(length - 1))

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_longestmonotonicsubstring_3():
    def sat(x: List[int], length=0, s=""):
        return all(s[x[i]] <= s[x[i + 1]] and x[i + 1] > x[i] >= 0 for i in range(length - 1))

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_longestmonotonicsubstring_4():
    def sat(x: List[int], length=1, s="xwV"):
        return all(s[x[i]] <= s[x[i + 1]] and x[i + 1] > x[i] >= 0 for i in range(length - 1))

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_longestmonotonicsubstringtricky():
    def sat(x: List[int], length=20, s="Dynamic programming solves this classic job-interview puzzle!!!"):
        return all(s[x[i]] <= s[x[i + 1]] and x[i + 1] > x[i] for i in range(length - 1))

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_longestmonotonicsubstringtricky_1():
    def sat(x: List[int], length=535, s="RRRS  S !L!eSSSS!TTT+!TTTUU!!UU!UU\"U\"\"\"VVV\"\"\"VK#WW##gfW##X##6$$X$XX@$XXP%%%YY%+YY%&ZZ)%ZZ&#Z&[&[[[[\\'\\\\]\\\\]''']]']]]^^(^R^((^))^)^^*^_*_L____**;**_``*```++`+`+[+++``,m,,`,,-aa@aa[a-arb-b--b(vzbb-.b.6.ccc.cKcc.cc//c/cc//dddddd/0deeeee000e0f0ff0f01ff11f1<1gg;g12R2g22233gg33g333g3g445555566ghhh66799h9hhh9h999iEii/iYi::i::j:jvv:;;;;jj<j<<k===kkkk===ll=l=l>>l>ll0>l>m>m@mmm??0m^,?nn???n?sn@@oo@DobAAooAo7AAppppBqC$qqqqCCCCqqqqrDrrrrrrrDbrsDDDEsEs9asssfttEtttEEEtEEtFFtuuLFuuuFFFvF0FGvGGGvvvvRwwwwxGHxHHHx+HIxxIexxIIyyyPCyyyII,yIyyIzIJzJJQJzKzzKz{KK{{{{{[K{K{KK{?{KLLLLLLLMMM>NNNNNOOOOOOOOPPPQQQQQQQRRR"):
        return all(s[x[i]] <= s[x[i + 1]] and x[i + 1] > x[i] for i in range(length - 1))

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_longestmonotonicsubstringtricky_2():
    def sat(x: List[int], length=1, s="O!A{SeKv"):
        return all(s[x[i]] <= s[x[i + 1]] and x[i + 1] > x[i] for i in range(length - 1))

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_longestmonotonicsubstringtricky_3():
    def sat(x: List[int], length=61, s=" OW##P%T'UW)X+X-YY]^_`bd/044e5egk7lm779:<m?D@ADnnpDEFIpNNOqqwxx"):
        return all(s[x[i]] <= s[x[i + 1]] and x[i + 1] > x[i] for i in range(length - 1))

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_longestmonotonicsubstringtricky_4():
    def sat(x: List[int], length=19, s="1>C>DmJh5\"Ju,\"Q8zJ_u-O-VfnVTZ?W'm=jq.\\l&%m$cU.nqv2\\**.o\">]FZ5owil>l*kIM wcLd<*UX`\"_u'DC3R$8wr;jT]CW\"F$QKeRPMzZY'U42&Km dRr8b$T3x)w2v,_k(dR,F:`=c$MjE_Kf/KCXFg^ueiO.U%S8_](:GF;`2`^O%eAqSRAHW0dYg5!u<ZV@usa`-<<ET@xZ)&<6=ogIhp9jJ/`$/_jEa-N$oZVT6#]^]x5u!$ Xk?g=TMwVGZqTU(OeH!Jbgz!9`%yxq(GN+@yD6RM1M#:geJpIPw1l{xxK!z'tXS5-S+vvE(nO:I_`l14Gz@U^.Ra73g!iH\\\"0{*>F@K'q>2HgCc^:baOy[,9vJtFWPAed2w_7zHLl&.x^:XLwwtS+Ocr#, *qXmo9Sp,Z>{l&ElT>RNZ:.5f6,yedMqH8?jA=_@oK;X\\pm>r0Il0+k\\,&'u*(S`]>u?(4M\\3=0 F<Jh?v`wz85A=?q3FUP<HiW[t0QB-Dx=e=ggmY29G4[HR!4i-*y@s$0)E'XPud6)gt(O[RWVf]ci,4.(:  8H[**k[g* T`z.Y2)Oq5`R8H$$joU/xfl*e4 \\z>*MS8wqj0(HwK?gvpuma{V5inBL\",39`%*r$uPi=%:s!<?{FCb-zILUAT?kdy\"B;sfYu#DoVp-'+]z:/c8eo2v&UAoeXEe:w#JZHKR\\3Xmxf'9jlHli*PTR-y`sdqRnv=;E$s]m!%I*`<*&.5N)wrI\"C=4^9RP5'9[5\"uG(4YU{3_aPHffi<E*+nVYQq37UP(P#wU9;p0Si.vyM1e?tXWZ9dRho1i!(we-<waQrvITH6vkTCG2 9hxMvtZ8QdR%WQ[B^0X1B;Vm&g/o=;YlD5[`Oh"):
        return all(s[x[i]] <= s[x[i + 1]] and x[i + 1] > x[i] for i in range(length - 1))

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_quine():
    def sat(quine: str):
        return eval(quine) == quine

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_revquine():
    def sat(rev_quine: str):
        return eval(rev_quine[::-1]) == rev_quine

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_booleanpythagoreantriples():
    def sat(colors: List[int], n=100):
        assert set(colors) <= {0, 1} and len(colors) >= n
        squares = {i ** 2: colors[i] for i in range(1, len(colors))}
        return not any(c == d == squares.get(i + j) for i, c in squares.items() for j, d in squares.items())

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_booleanpythagoreantriples_1():
    def sat(colors: List[int], n=7824):
        assert set(colors) <= {0, 1} and len(colors) >= n
        squares = {i ** 2: colors[i] for i in range(1, len(colors))}
        return not any(c == d == squares.get(i + j) for i, c in squares.items() for j, d in squares.items())

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_booleanpythagoreantriples_2():
    def sat(colors: List[int], n=0):
        assert set(colors) <= {0, 1} and len(colors) >= n
        squares = {i ** 2: colors[i] for i in range(1, len(colors))}
        return not any(c == d == squares.get(i + j) for i, c in squares.items() for j, d in squares.items())

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_booleanpythagoreantriples_3():
    def sat(colors: List[int], n=1):
        assert set(colors) <= {0, 1} and len(colors) >= n
        squares = {i ** 2: colors[i] for i in range(1, len(colors))}
        return not any(c == d == squares.get(i + j) for i, c in squares.items() for j, d in squares.items())

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_clockangle():
    def sat(hands: List[int], target_angle=45):
        h, m = hands
        assert 0 < h <= 12 and 0 <= m < 60
        hour_angle = 30 * h + m / 2
        minute_angle = 6 * m
        return abs(hour_angle - minute_angle) in [target_angle, 360 - target_angle]

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_clockangle_1():
    def sat(hands: List[int], target_angle=39):
        h, m = hands
        assert 0 < h <= 12 and 0 <= m < 60
        hour_angle = 30 * h + m / 2
        minute_angle = 6 * m
        return abs(hour_angle - minute_angle) in [target_angle, 360 - target_angle]

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_clockangle_2():
    def sat(hands: List[int], target_angle=133):
        h, m = hands
        assert 0 < h <= 12 and 0 <= m < 60
        hour_angle = 30 * h + m / 2
        minute_angle = 6 * m
        return abs(hour_angle - minute_angle) in [target_angle, 360 - target_angle]

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_clockangle_3():
    def sat(hands: List[int], target_angle=138):
        h, m = hands
        assert 0 < h <= 12 and 0 <= m < 60
        hour_angle = 30 * h + m / 2
        minute_angle = 6 * m
        return abs(hour_angle - minute_angle) in [target_angle, 360 - target_angle]

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_clockangle_4():
    def sat(hands: List[int], target_angle=68):
        h, m = hands
        assert 0 < h <= 12 and 0 <= m < 60
        hour_angle = 30 * h + m / 2
        minute_angle = 6 * m
        return abs(hour_angle - minute_angle) in [target_angle, 360 - target_angle]

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_kirkman():
    def sat(daygroups: List[List[List[int]]]):
        assert len(daygroups) == 7
        assert all(len(groups) == 5 and {i for g in groups for i in g} == set(range(15)) for groups in daygroups)
        assert all(len(g) == 3 for groups in daygroups for g in groups)
        return len({(i, j) for groups in daygroups for g in groups for i in g for j in g}) == 15 * 15

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_monkeyandcoconuts():
    def sat(n: int):
        for i in range(5):
            assert n % 5 == 1
            n -= 1 + (n - 1) // 5
        return n > 0 and n % 5 == 1

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_no3colinear():
    def sat(coords: List[List[int]], side=10, num_points=20):
        for i1 in range(len(coords)):
            x1, y1 = coords[i1]
            assert 0 <= x1 < side and 0 <= y1 < side
            for i2 in range(i1):
                x2, y2 = coords[i2]
                for i3 in range(i2):
                    x3, y3 = coords[i3]
                    assert x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2) != 0
        return len({(a, b) for a, b in coords}) == len(coords) >= num_points

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_no3colinear_1():
    def sat(coords: List[List[int]], side=0, num_points=0):
        for i1 in range(len(coords)):
            x1, y1 = coords[i1]
            assert 0 <= x1 < side and 0 <= y1 < side
            for i2 in range(i1):
                x2, y2 = coords[i2]
                for i3 in range(i2):
                    x3, y3 = coords[i3]
                    assert x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2) != 0
        return len({(a, b) for a, b in coords}) == len(coords) >= num_points

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_no3colinear_2():
    def sat(coords: List[List[int]], side=1, num_points=1):
        for i1 in range(len(coords)):
            x1, y1 = coords[i1]
            assert 0 <= x1 < side and 0 <= y1 < side
            for i2 in range(i1):
                x2, y2 = coords[i2]
                for i3 in range(i2):
                    x3, y3 = coords[i3]
                    assert x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2) != 0
        return len({(a, b) for a, b in coords}) == len(coords) >= num_points

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_no3colinear_3():
    def sat(coords: List[List[int]], side=2, num_points=4):
        for i1 in range(len(coords)):
            x1, y1 = coords[i1]
            assert 0 <= x1 < side and 0 <= y1 < side
            for i2 in range(i1):
                x2, y2 = coords[i2]
                for i3 in range(i2):
                    x3, y3 = coords[i3]
                    assert x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2) != 0
        return len({(a, b) for a, b in coords}) == len(coords) >= num_points

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_postagestamp():
    def sat(stamps: List[int], target=80, max_stamps=4, options=[10, 32, 8]):
        for s in stamps:
            assert s in options
        return len(stamps) <= max_stamps and sum(stamps) == target

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_postagestamp_1():
    def sat(stamps: List[int], target=271, max_stamps=8, options=[37, 37, 12, 87, 39]):
        for s in stamps:
            assert s in options
        return len(stamps) <= max_stamps and sum(stamps) == target

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_postagestamp_2():
    def sat(stamps: List[int], target=3, max_stamps=3, options=[18, 1, 43, 81]):
        for s in stamps:
            assert s in options
        return len(stamps) <= max_stamps and sum(stamps) == target

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_postagestamp_3():
    def sat(stamps: List[int], target=19, max_stamps=2, options=[19, 14, 81]):
        for s in stamps:
            assert s in options
        return len(stamps) <= max_stamps and sum(stamps) == target

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_postagestamp_4():
    def sat(stamps: List[int], target=56, max_stamps=1, options=[25, 22, 8, 84, 60, 56, 54, 7, 8]):
        for s in stamps:
            assert s in options
        return len(stamps) <= max_stamps and sum(stamps) == target

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_sudoku():
    def sat(x: str, puz="____9_2___7__________1_8_4____2_78____4_____1____69____2_8___5__6__3_7___49______"):
        assert all(c == "_" or c == s for (c, s) in zip(puz, x))
    
        full = set('123456789')
        for i in range(9):
            assert {x[i] for i in range(9 * i, 9 * i + 9)} == full, "invalid row"
            assert {x[i] for i in range(i, i + 81, 9)} == full, "invalid column"
            assert {x[9 * a + b + i + 26 * (i % 3)] for a in range(3) for b in range(3)} == full, "invalid square"
    
        return True

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_sudoku_1():
    def sat(x: str, puz="__2__1_3__9_7_____5______8_6___5_______12____2____3_68________9_1_8__4____7____25"):
        assert all(c == "_" or c == s for (c, s) in zip(puz, x))
    
        full = set('123456789')
        for i in range(9):
            assert {x[i] for i in range(9 * i, 9 * i + 9)} == full, "invalid row"
            assert {x[i] for i in range(i, i + 81, 9)} == full, "invalid column"
            assert {x[9 * a + b + i + 26 * (i % 3)] for a in range(3) for b in range(3)} == full, "invalid square"
    
        return True

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_sudoku_2():
    def sat(x: str, puz="__721__56__27___________9______5____62______1_1___9___8_____________3197__61__32_"):
        assert all(c == "_" or c == s for (c, s) in zip(puz, x))
    
        full = set('123456789')
        for i in range(9):
            assert {x[i] for i in range(9 * i, 9 * i + 9)} == full, "invalid row"
            assert {x[i] for i in range(i, i + 81, 9)} == full, "invalid column"
            assert {x[9 * a + b + i + 26 * (i % 3)] for a in range(3) for b in range(3)} == full, "invalid square"
    
        return True

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_sudoku_3():
    def sat(x: str, puz="_____42______7_____4______9__49___626_8__3___3_7__65_4_5_3__1__1____8_7__________"):
        assert all(c == "_" or c == s for (c, s) in zip(puz, x))
    
        full = set('123456789')
        for i in range(9):
            assert {x[i] for i in range(9 * i, 9 * i + 9)} == full, "invalid row"
            assert {x[i] for i in range(i, i + 81, 9)} == full, "invalid column"
            assert {x[9 * a + b + i + 26 * (i % 3)] for a in range(3) for b in range(3)} == full, "invalid square"
    
        return True

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_sudoku_4():
    def sat(x: str, puz="___56_4_7__92_4_65___3______9____2___5_______7___8___1_________43_____5_____76__2"):
        assert all(c == "_" or c == s for (c, s) in zip(puz, x))
    
        full = set('123456789')
        for i in range(9):
            assert {x[i] for i in range(9 * i, 9 * i + 9)} == full, "invalid row"
            assert {x[i] for i in range(i, i + 81, 9)} == full, "invalid column"
            assert {x[9 * a + b + i + 26 * (i % 3)] for a in range(3) for b in range(3)} == full, "invalid square"
    
        return True

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_squaringthesquare():
    def sat(xy_sides: List[List[int]]):
        n = max(x + side for x, y, side in xy_sides)
        assert len({side for x, y, side in xy_sides}) == len(xy_sides) > 1
        for x, y, s in xy_sides:
            assert 0 <= y < y + s <= n and 0 <= x
            for x2, y2, s2 in xy_sides:
                assert s2 <= s or x2 >= x + s or x2 + s2 <= x or y2 >= y + s or y2 + s2 <= y
    
        return sum(side ** 2 for x, y, side in xy_sides) == n ** 2

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_necklacesplit():
    def sat(n: int, lace="bbrbrbbbbbbrrrrrrrbrrrrbbbrbrrbbbrbrrrbrrbrrbrbbrrrrrbrbbbrrrbbbrbbrbbbrbrbb"):
        sub = lace[n: n + len(lace) // 2]
        return n >= 0 and lace.count("r") == 2 * sub.count("r") and lace.count("b") == 2 * sub.count("b")

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_necklacesplit_1():
    def sat(n: int, lace="rbbrrbbrbrbbbrrrbbrbrbrrbbrbbbbbbrrrrrrrrbrrrbbrbrrbbbrbbrrrbbrbbrrbrrbrbbrbbbbbbrbbbrbrbrrbrbbrbrrbbrrbrrbrrbrrbrbrbrrrbbrbrbbrrbbbbrrrrrbbrbrbrrbr"):
        sub = lace[n: n + len(lace) // 2]
        return n >= 0 and lace.count("r") == 2 * sub.count("r") and lace.count("b") == 2 * sub.count("b")

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_necklacesplit_2():
    def sat(n: int, lace="brrrbrrbrbbbbbrrbbrr"):
        sub = lace[n: n + len(lace) // 2]
        return n >= 0 and lace.count("r") == 2 * sub.count("r") and lace.count("b") == 2 * sub.count("b")

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_necklacesplit_3():
    def sat(n: int, lace="bbbbrrbbbbrrbbrrrbbrrbbrrrrrrrbrbrbbbrrbrrrbbbbbbbrbrbrbbbbbbbrrbbrbbrbrrbrbrrbbbrrrrrbrrbbrrrbbrbrrrbbbbrbbbrrrrbrbrrbbrbrbrbbrrbrrrbrbrrbbbbbbrbrrrrbbrbbbrbrrbrbbrbrrbbbbrrrrrbrrrbbrrrrrrbrrrbrbbbrbbbrrrbbr"):
        sub = lace[n: n + len(lace) // 2]
        return n >= 0 and lace.count("r") == 2 * sub.count("r") and lace.count("b") == 2 * sub.count("b")

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_necklacesplit_4():
    def sat(n: int, lace="brrbbbrbbrrbrrbbrrbrrrbbrbbrrrbrbrbrrrrbbrrrbrrbbbbrbbbrrbbrrrbbrbrbbbbbrrbrrbbr"):
        sub = lace[n: n + len(lace) // 2]
        return n >= 0 and lace.count("r") == 2 * sub.count("r") and lace.count("b") == 2 * sub.count("b")

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_pandigitalsquare():
    def sat(n: int):
        s = str(n * n)
        for i in "0123456789":
            assert s.count(i) == 1
        return True

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_allpandigitalsquares():
    def sat(nums: List[int]):
        return [sorted([int(s) for s in str(n * n)]) for n in set(nums)] == [list(range(10))] * 174

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_cardgame24():
    def sat(expr: str, nums=[3, 7, 3, 7]):
        assert len(nums) == 4 and 1 <= min(nums) and max(nums) <= 13, "hint: nums is a list of four ints in 1..13"
        expr = expr.replace(" ", "")  # ignore whitespace
        digits = ""
        for i in range(len(expr)):
            if i == 0 or expr[i - 1] in "+*-/(":
                assert expr[i] in "123456789(", "Expr cannot contain **, //, or unary -"
            assert expr[i] in "1234567890()+-*/", "Expr can only contain `0123456789()+-*/`"
            digits += expr[i] if expr[i] in "0123456789" else " "
        assert sorted(int(s) for s in digits.split()) == sorted(nums), "Each number must occur exactly once"
        return abs(eval(expr) - 24.0) < 1e-6

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_cardgame24_1():
    def sat(expr: str, nums=[1, 3, 7, 13]):
        assert len(nums) == 4 and 1 <= min(nums) and max(nums) <= 13, "hint: nums is a list of four ints in 1..13"
        expr = expr.replace(" ", "")  # ignore whitespace
        digits = ""
        for i in range(len(expr)):
            if i == 0 or expr[i - 1] in "+*-/(":
                assert expr[i] in "123456789(", "Expr cannot contain **, //, or unary -"
            assert expr[i] in "1234567890()+-*/", "Expr can only contain `0123456789()+-*/`"
            digits += expr[i] if expr[i] in "0123456789" else " "
        assert sorted(int(s) for s in digits.split()) == sorted(nums), "Each number must occur exactly once"
        return abs(eval(expr) - 24.0) < 1e-6

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_cardgame24_2():
    def sat(expr: str, nums=[10, 7, 3, 1]):
        assert len(nums) == 4 and 1 <= min(nums) and max(nums) <= 13, "hint: nums is a list of four ints in 1..13"
        expr = expr.replace(" ", "")  # ignore whitespace
        digits = ""
        for i in range(len(expr)):
            if i == 0 or expr[i - 1] in "+*-/(":
                assert expr[i] in "123456789(", "Expr cannot contain **, //, or unary -"
            assert expr[i] in "1234567890()+-*/", "Expr can only contain `0123456789()+-*/`"
            digits += expr[i] if expr[i] in "0123456789" else " "
        assert sorted(int(s) for s in digits.split()) == sorted(nums), "Each number must occur exactly once"
        return abs(eval(expr) - 24.0) < 1e-6

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_cardgame24_3():
    def sat(expr: str, nums=[8, 3, 12, 1]):
        assert len(nums) == 4 and 1 <= min(nums) and max(nums) <= 13, "hint: nums is a list of four ints in 1..13"
        expr = expr.replace(" ", "")  # ignore whitespace
        digits = ""
        for i in range(len(expr)):
            if i == 0 or expr[i - 1] in "+*-/(":
                assert expr[i] in "123456789(", "Expr cannot contain **, //, or unary -"
            assert expr[i] in "1234567890()+-*/", "Expr can only contain `0123456789()+-*/`"
            digits += expr[i] if expr[i] in "0123456789" else " "
        assert sorted(int(s) for s in digits.split()) == sorted(nums), "Each number must occur exactly once"
        return abs(eval(expr) - 24.0) < 1e-6

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_cardgame24_4():
    def sat(expr: str, nums=[10, 12, 1, 7]):
        assert len(nums) == 4 and 1 <= min(nums) and max(nums) <= 13, "hint: nums is a list of four ints in 1..13"
        expr = expr.replace(" ", "")  # ignore whitespace
        digits = ""
        for i in range(len(expr)):
            if i == 0 or expr[i - 1] in "+*-/(":
                assert expr[i] in "123456789(", "Expr cannot contain **, //, or unary -"
            assert expr[i] in "1234567890()+-*/", "Expr can only contain `0123456789()+-*/`"
            digits += expr[i] if expr[i] in "0123456789" else " "
        assert sorted(int(s) for s in digits.split()) == sorted(nums), "Each number must occur exactly once"
        return abs(eval(expr) - 24.0) < 1e-6

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_easy63():
    def sat(s: str):
        return set(s) <= set("18-+*/") and s.count("8") == 2 and s.count("1") == 1 and eval(s) == 63

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_harder63():
    def sat(s: str):
        return set(s) <= set("18-+*/") and s.count("8") == 3 and s.count("1") == 1 and eval(s) == 63

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_waterpouring():
    def sat(moves: List[List[int]], capacities=[8, 5, 3], init=[8, 0, 0], goal=[4, 4, 0]):
        state = init.copy()
    
        for [i, j] in moves:
            assert min(i, j) >= 0, "Indices must be non-negative"
            assert i != j, "Cannot pour from same state to itself"
            n = min(capacities[j], state[i] + state[j])
            state[i], state[j] = state[i] + state[j] - n, n
    
        return state == goal

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_waterpouring_1():
    def sat(moves: List[List[int]], capacities=[724, 43, 611], init=[72, 2, 269], goal=[56, 0, 287]):
        state = init.copy()
    
        for [i, j] in moves:
            assert min(i, j) >= 0, "Indices must be non-negative"
            assert i != j, "Cannot pour from same state to itself"
            n = min(capacities[j], state[i] + state[j])
            state[i], state[j] = state[i] + state[j] - n, n
    
        return state == goal

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_waterpouring_2():
    def sat(moves: List[List[int]], capacities=[357, 298, 492], init=[8, 284, 72], goal=[0, 0, 364]):
        state = init.copy()
    
        for [i, j] in moves:
            assert min(i, j) >= 0, "Indices must be non-negative"
            assert i != j, "Cannot pour from same state to itself"
            n = min(capacities[j], state[i] + state[j])
            state[i], state[j] = state[i] + state[j] - n, n
    
        return state == goal

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_waterpouring_3():
    def sat(moves: List[List[int]], capacities=[511, 625, 553], init=[472, 153, 127], goal=[97, 625, 30]):
        state = init.copy()
    
        for [i, j] in moves:
            assert min(i, j) >= 0, "Indices must be non-negative"
            assert i != j, "Cannot pour from same state to itself"
            n = min(capacities[j], state[i] + state[j])
            state[i], state[j] = state[i] + state[j] - n, n
    
        return state == goal

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_waterpouring_4():
    def sat(moves: List[List[int]], capacities=[86, 259, 281], init=[47, 18, 35], goal=[35, 0, 65]):
        state = init.copy()
    
        for [i, j] in moves:
            assert min(i, j) >= 0, "Indices must be non-negative"
            assert i != j, "Cannot pour from same state to itself"
            n = min(capacities[j], state[i] + state[j])
            state[i], state[j] = state[i] + state[j] - n, n
    
        return state == goal

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_verbalarithmetic():
    def sat(li: List[int], words=['SEND', 'MORE', 'MONEY']):
        assert len(li) == len(words) and all(i > 0 and len(str(i)) == len(w) for i, w in zip(li, words))
        assert len({c for w in words for c in w}) == len({(d, c) for i, w in zip(li, words) for d, c in zip(str(i), w)})
        return sum(li[:-1]) == li[-1]

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_verbalarithmetic_1():
    def sat(li: List[int], words=['FORTY', 'TEN', 'TEN', 'SIXTY']):
        assert len(li) == len(words) and all(i > 0 and len(str(i)) == len(w) for i, w in zip(li, words))
        assert len({c for w in words for c in w}) == len({(d, c) for i, w in zip(li, words) for d, c in zip(str(i), w)})
        return sum(li[:-1]) == li[-1]

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_verbalarithmetic_2():
    def sat(li: List[int], words=['GREEN', 'ORANGE', 'COLORS']):
        assert len(li) == len(words) and all(i > 0 and len(str(i)) == len(w) for i, w in zip(li, words))
        assert len({c for w in words for c in w}) == len({(d, c) for i, w in zip(li, words) for d, c in zip(str(i), w)})
        return sum(li[:-1]) == li[-1]

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_verbalarithmetic_3():
    def sat(li: List[int], words=['fqjb', 'awqw', 'lfll', 'fvvvb']):
        assert len(li) == len(words) and all(i > 0 and len(str(i)) == len(w) for i, w in zip(li, words))
        assert len({c for w in words for c in w}) == len({(d, c) for i, w in zip(li, words) for d, c in zip(str(i), w)})
        return sum(li[:-1]) == li[-1]

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_verbalarithmetic_4():
    def sat(li: List[int], words=['tnnq', 'sna', 'ajjc', 'isun', 'usub', 'caiun']):
        assert len(li) == len(words) and all(i > 0 and len(str(i)) == len(w) for i, w in zip(li, words))
        assert len({c for w in words for c in w}) == len({(d, c) for i, w in zip(li, words) for d, c in zip(str(i), w)})
        return sum(li[:-1]) == li[-1]

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_slidingpuzzle():
    def sat(moves: List[int], start=[[5, 0, 2, 3], [1, 9, 6, 7], [4, 14, 8, 11], [12, 13, 10, 15]]):
    
        locs = {i: [x, y] for y, row in enumerate(start) for x, i in enumerate(row)}  # locations, 0 stands for blank
        for i in moves:
            assert abs(locs[0][0] - locs[i][0]) + abs(locs[0][1] - locs[i][1]) == 1
            locs[0], locs[i] = locs[i], locs[0]
        return all(locs[i] == [i % len(start[0]), i // len(start)] for i in locs)

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_slidingpuzzle_1():
    def sat(moves: List[int], start=[[1, 5, 0], [3, 2, 8], [6, 4, 7]]):
    
        locs = {i: [x, y] for y, row in enumerate(start) for x, i in enumerate(row)}  # locations, 0 stands for blank
        for i in moves:
            assert abs(locs[0][0] - locs[i][0]) + abs(locs[0][1] - locs[i][1]) == 1
            locs[0], locs[i] = locs[i], locs[0]
        return all(locs[i] == [i % len(start[0]), i // len(start)] for i in locs)

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_slidingpuzzle_2():
    def sat(moves: List[int], start=[[6, 0, 3], [7, 1, 4], [8, 2, 5]]):
    
        locs = {i: [x, y] for y, row in enumerate(start) for x, i in enumerate(row)}  # locations, 0 stands for blank
        for i in moves:
            assert abs(locs[0][0] - locs[i][0]) + abs(locs[0][1] - locs[i][1]) == 1
            locs[0], locs[i] = locs[i], locs[0]
        return all(locs[i] == [i % len(start[0]), i // len(start)] for i in locs)

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_slidingpuzzle_3():
    def sat(moves: List[int], start=[[0, 1], [2, 3]]):
    
        locs = {i: [x, y] for y, row in enumerate(start) for x, i in enumerate(row)}  # locations, 0 stands for blank
        for i in moves:
            assert abs(locs[0][0] - locs[i][0]) + abs(locs[0][1] - locs[i][1]) == 1
            locs[0], locs[i] = locs[i], locs[0]
        return all(locs[i] == [i % len(start[0]), i // len(start)] for i in locs)

    assert False


@pytest.mark.skip(reason="not implemented yet")
def test_slidingpuzzle_4():
    def sat(moves: List[int], start=[[2, 1], [0, 3]]):
    
        locs = {i: [x, y] for y, row in enumerate(start) for x, i in enumerate(row)}  # locations, 0 stands for blank
        for i in moves:
            assert abs(locs[0][0] - locs[i][0]) + abs(locs[0][1] - locs[i][1]) == 1
            locs[0], locs[i] = locs[i], locs[0]
        return all(locs[i] == [i % len(start[0]), i // len(start)] for i in locs)

    assert False
