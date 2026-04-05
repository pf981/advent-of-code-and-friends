from typing import List

import pytest


@pytest.mark.skip(reason="not implemented yet")
def test_eightqueensorfewer():
    def sat(squares: List[List[int]], m=8, n=8):
        k = min(m, n)
        assert (
            all(i in range(m) and j in range(n) for i, j in squares)
            and len(squares) == k
        )
        return 4 * k == len(
            {
                t
                for i, j in squares
                for t in [("row", i), ("col", j), ("SE", i + j), ("NE", i - j)]
            }
        )

    assert sat(...)


@pytest.mark.skip(reason="not implemented yet")
def test_eightqueensorfewer_1():
    def sat(squares: List[List[int]], m=9, n=6):
        k = min(m, n)
        assert (
            all(i in range(m) and j in range(n) for i, j in squares)
            and len(squares) == k
        )
        return 4 * k == len(
            {
                t
                for i, j in squares
                for t in [("row", i), ("col", j), ("SE", i + j), ("NE", i - j)]
            }
        )

    assert sat(...)


@pytest.mark.skip(reason="not implemented yet")
def test_eightqueensorfewer_2():
    def sat(squares: List[List[int]], m=59, n=4):
        k = min(m, n)
        assert (
            all(i in range(m) and j in range(n) for i, j in squares)
            and len(squares) == k
        )
        return 4 * k == len(
            {
                t
                for i, j in squares
                for t in [("row", i), ("col", j), ("SE", i + j), ("NE", i - j)]
            }
        )

    assert sat(...)


@pytest.mark.skip(reason="not implemented yet")
def test_eightqueensorfewer_3():
    def sat(squares: List[List[int]], m=38, n=8):
        k = min(m, n)
        assert (
            all(i in range(m) and j in range(n) for i, j in squares)
            and len(squares) == k
        )
        return 4 * k == len(
            {
                t
                for i, j in squares
                for t in [("row", i), ("col", j), ("SE", i + j), ("NE", i - j)]
            }
        )

    assert sat(...)


@pytest.mark.skip(reason="not implemented yet")
def test_eightqueensorfewer_4():
    def sat(squares: List[List[int]], m=9, n=4):
        k = min(m, n)
        assert (
            all(i in range(m) and j in range(n) for i, j in squares)
            and len(squares) == k
        )
        return 4 * k == len(
            {
                t
                for i, j in squares
                for t in [("row", i), ("col", j), ("SE", i + j), ("NE", i - j)]
            }
        )

    assert sat(...)


@pytest.mark.skip(reason="not implemented yet")
def test_morequeens():
    def sat(squares: List[List[int]], m=9, n=9):
        k = min(m, n)
        assert all(i in range(m) and j in range(n) for i, j in squares), (
            "queen off board"
        )
        assert len(squares) == k, "Wrong number of queens"
        assert len({i for i, j in squares}) == k, "Queens on same row"
        assert len({j for i, j in squares}) == k, "Queens on same file"
        assert len({i + j for i, j in squares}) == k, "Queens on same SE diagonal"
        assert len({i - j for i, j in squares}) == k, "Queens on same NE diagonal"
        return True

    assert sat(...)


@pytest.mark.skip(reason="not implemented yet")
def test_morequeens_1():
    def sat(squares: List[List[int]], m=79, n=95):
        k = min(m, n)
        assert all(i in range(m) and j in range(n) for i, j in squares), (
            "queen off board"
        )
        assert len(squares) == k, "Wrong number of queens"
        assert len({i for i, j in squares}) == k, "Queens on same row"
        assert len({j for i, j in squares}) == k, "Queens on same file"
        assert len({i + j for i, j in squares}) == k, "Queens on same SE diagonal"
        assert len({i - j for i, j in squares}) == k, "Queens on same NE diagonal"
        return True

    assert sat(...)


@pytest.mark.skip(reason="not implemented yet")
def test_morequeens_2():
    def sat(squares: List[List[int]], m=80, n=88):
        k = min(m, n)
        assert all(i in range(m) and j in range(n) for i, j in squares), (
            "queen off board"
        )
        assert len(squares) == k, "Wrong number of queens"
        assert len({i for i, j in squares}) == k, "Queens on same row"
        assert len({j for i, j in squares}) == k, "Queens on same file"
        assert len({i + j for i, j in squares}) == k, "Queens on same SE diagonal"
        assert len({i - j for i, j in squares}) == k, "Queens on same NE diagonal"
        return True

    assert sat(...)


@pytest.mark.skip(reason="not implemented yet")
def test_morequeens_3():
    def sat(squares: List[List[int]], m=56, n=16):
        k = min(m, n)
        assert all(i in range(m) and j in range(n) for i, j in squares), (
            "queen off board"
        )
        assert len(squares) == k, "Wrong number of queens"
        assert len({i for i, j in squares}) == k, "Queens on same row"
        assert len({j for i, j in squares}) == k, "Queens on same file"
        assert len({i + j for i, j in squares}) == k, "Queens on same SE diagonal"
        assert len({i - j for i, j in squares}) == k, "Queens on same NE diagonal"
        return True

    assert sat(...)


@pytest.mark.skip(reason="not implemented yet")
def test_morequeens_4():
    def sat(squares: List[List[int]], m=23, n=45):
        k = min(m, n)
        assert all(i in range(m) and j in range(n) for i, j in squares), (
            "queen off board"
        )
        assert len(squares) == k, "Wrong number of queens"
        assert len({i for i, j in squares}) == k, "Queens on same row"
        assert len({j for i, j in squares}) == k, "Queens on same file"
        assert len({i + j for i, j in squares}) == k, "Queens on same SE diagonal"
        assert len({i - j for i, j in squares}) == k, "Queens on same NE diagonal"
        return True

    assert sat(...)


@pytest.mark.skip(reason="not implemented yet")
def test_knightstour():
    def sat(tour: List[List[int]], m=8, n=8):
        assert all(
            {abs(i1 - i2), abs(j1 - j2)} == {1, 2}
            for [i1, j1], [i2, j2] in zip(tour, tour[1:])
        ), "legal moves"
        return sorted(tour) == [
            [i, j] for i in range(m) for j in range(n)
        ]  # cover every square once

    assert sat(...)


@pytest.mark.skip(reason="not implemented yet")
def test_knightstour_1():
    def sat(tour: List[List[int]], m=9, n=9):
        assert all(
            {abs(i1 - i2), abs(j1 - j2)} == {1, 2}
            for [i1, j1], [i2, j2] in zip(tour, tour[1:])
        ), "legal moves"
        return sorted(tour) == [
            [i, j] for i in range(m) for j in range(n)
        ]  # cover every square once

    assert sat(...)


@pytest.mark.skip(reason="not implemented yet")
def test_knightstour_2():
    def sat(tour: List[List[int]], m=7, n=7):
        assert all(
            {abs(i1 - i2), abs(j1 - j2)} == {1, 2}
            for [i1, j1], [i2, j2] in zip(tour, tour[1:])
        ), "legal moves"
        return sorted(tour) == [
            [i, j] for i in range(m) for j in range(n)
        ]  # cover every square once

    assert sat(...)


@pytest.mark.skip(reason="not implemented yet")
def test_knightstour_3():
    def sat(tour: List[List[int]], m=6, n=6):
        assert all(
            {abs(i1 - i2), abs(j1 - j2)} == {1, 2}
            for [i1, j1], [i2, j2] in zip(tour, tour[1:])
        ), "legal moves"
        return sorted(tour) == [
            [i, j] for i in range(m) for j in range(n)
        ]  # cover every square once

    assert sat(...)


@pytest.mark.skip(reason="not implemented yet")
def test_knightstour_4():
    def sat(tour: List[List[int]], m=7, n=8):
        assert all(
            {abs(i1 - i2), abs(j1 - j2)} == {1, 2}
            for [i1, j1], [i2, j2] in zip(tour, tour[1:])
        ), "legal moves"
        return sorted(tour) == [
            [i, j] for i in range(m) for j in range(n)
        ]  # cover every square once

    assert sat(...)


@pytest.mark.skip(reason="not implemented yet")
def test_uncrossedknightspath():
    def sat(path: List[List[int]], m=8, n=8, target=35):
        def legal_move(m):
            (a, b), (i, j) = m
            return {abs(i - a), abs(j - b)} == {1, 2}

        def legal_quad(
            m1, m2
        ):  # non-overlapping test: parallel or bounding box has (width - 1) * (height - 1) >= 5
            (i1, j1), (i2, j2) = m1
            (a1, b1), (a2, b2) = m2
            return (
                len({(i1, j1), (i2, j2), (a1, b1), (a2, b2)})
                < 4  # adjacent edges in path, ignore
                or (i1 - i2) * (b1 - b2) == (j1 - j2) * (a1 - a2)  # parallel
                or (max(a1, a2, i1, i2) - min(a1, a2, i1, i2))
                * (max(b1, b2, j1, j2) - min(b1, b2, j1, j2))
                >= 5
                # far
            )

        assert all(i in range(m) and j in range(n) for i, j in path), "move off board"
        assert len({(i, j) for i, j in path}) == len(path), "visited same square twice"

        moves = list(zip(path, path[1:]))
        assert all(legal_move(m) for m in moves), "illegal move"
        assert all(legal_quad(m1, m2) for m1 in moves for m2 in moves), (
            "intersecting move pair"
        )

        return len(path) >= target

    assert sat(...)


@pytest.mark.skip(reason="not implemented yet")
def test_uncrossedknightspath_1():
    def sat(path: List[List[int]], m=3, n=3, target=2):
        def legal_move(m):
            (a, b), (i, j) = m
            return {abs(i - a), abs(j - b)} == {1, 2}

        def legal_quad(
            m1, m2
        ):  # non-overlapping test: parallel or bounding box has (width - 1) * (height - 1) >= 5
            (i1, j1), (i2, j2) = m1
            (a1, b1), (a2, b2) = m2
            return (
                len({(i1, j1), (i2, j2), (a1, b1), (a2, b2)})
                < 4  # adjacent edges in path, ignore
                or (i1 - i2) * (b1 - b2) == (j1 - j2) * (a1 - a2)  # parallel
                or (max(a1, a2, i1, i2) - min(a1, a2, i1, i2))
                * (max(b1, b2, j1, j2) - min(b1, b2, j1, j2))
                >= 5
                # far
            )

        assert all(i in range(m) and j in range(n) for i, j in path), "move off board"
        assert len({(i, j) for i, j in path}) == len(path), "visited same square twice"

        moves = list(zip(path, path[1:]))
        assert all(legal_move(m) for m in moves), "illegal move"
        assert all(legal_quad(m1, m2) for m1 in moves for m2 in moves), (
            "intersecting move pair"
        )

        return len(path) >= target

    assert sat(...)


@pytest.mark.skip(reason="not implemented yet")
def test_uncrossedknightspath_2():
    def sat(path: List[List[int]], m=4, n=4, target=5):
        def legal_move(m):
            (a, b), (i, j) = m
            return {abs(i - a), abs(j - b)} == {1, 2}

        def legal_quad(
            m1, m2
        ):  # non-overlapping test: parallel or bounding box has (width - 1) * (height - 1) >= 5
            (i1, j1), (i2, j2) = m1
            (a1, b1), (a2, b2) = m2
            return (
                len({(i1, j1), (i2, j2), (a1, b1), (a2, b2)})
                < 4  # adjacent edges in path, ignore
                or (i1 - i2) * (b1 - b2) == (j1 - j2) * (a1 - a2)  # parallel
                or (max(a1, a2, i1, i2) - min(a1, a2, i1, i2))
                * (max(b1, b2, j1, j2) - min(b1, b2, j1, j2))
                >= 5
                # far
            )

        assert all(i in range(m) and j in range(n) for i, j in path), "move off board"
        assert len({(i, j) for i, j in path}) == len(path), "visited same square twice"

        moves = list(zip(path, path[1:]))
        assert all(legal_move(m) for m in moves), "illegal move"
        assert all(legal_quad(m1, m2) for m1 in moves for m2 in moves), (
            "intersecting move pair"
        )

        return len(path) >= target

    assert sat(...)


@pytest.mark.skip(reason="not implemented yet")
def test_uncrossedknightspath_3():
    def sat(path: List[List[int]], m=5, n=5, target=10):
        def legal_move(m):
            (a, b), (i, j) = m
            return {abs(i - a), abs(j - b)} == {1, 2}

        def legal_quad(
            m1, m2
        ):  # non-overlapping test: parallel or bounding box has (width - 1) * (height - 1) >= 5
            (i1, j1), (i2, j2) = m1
            (a1, b1), (a2, b2) = m2
            return (
                len({(i1, j1), (i2, j2), (a1, b1), (a2, b2)})
                < 4  # adjacent edges in path, ignore
                or (i1 - i2) * (b1 - b2) == (j1 - j2) * (a1 - a2)  # parallel
                or (max(a1, a2, i1, i2) - min(a1, a2, i1, i2))
                * (max(b1, b2, j1, j2) - min(b1, b2, j1, j2))
                >= 5
                # far
            )

        assert all(i in range(m) and j in range(n) for i, j in path), "move off board"
        assert len({(i, j) for i, j in path}) == len(path), "visited same square twice"

        moves = list(zip(path, path[1:]))
        assert all(legal_move(m) for m in moves), "illegal move"
        assert all(legal_quad(m1, m2) for m1 in moves for m2 in moves), (
            "intersecting move pair"
        )

        return len(path) >= target

    assert sat(...)


@pytest.mark.skip(reason="not implemented yet")
def test_uncrossedknightspath_4():
    def sat(path: List[List[int]], m=6, n=5, target=9):
        def legal_move(m):
            (a, b), (i, j) = m
            return {abs(i - a), abs(j - b)} == {1, 2}

        def legal_quad(
            m1, m2
        ):  # non-overlapping test: parallel or bounding box has (width - 1) * (height - 1) >= 5
            (i1, j1), (i2, j2) = m1
            (a1, b1), (a2, b2) = m2
            return (
                len({(i1, j1), (i2, j2), (a1, b1), (a2, b2)})
                < 4  # adjacent edges in path, ignore
                or (i1 - i2) * (b1 - b2) == (j1 - j2) * (a1 - a2)  # parallel
                or (max(a1, a2, i1, i2) - min(a1, a2, i1, i2))
                * (max(b1, b2, j1, j2) - min(b1, b2, j1, j2))
                >= 5
                # far
            )

        assert all(i in range(m) and j in range(n) for i, j in path), "move off board"
        assert len({(i, j) for i, j in path}) == len(path), "visited same square twice"

        moves = list(zip(path, path[1:]))
        assert all(legal_move(m) for m in moves), "illegal move"
        assert all(legal_quad(m1, m2) for m1 in moves for m2 in moves), (
            "intersecting move pair"
        )

        return len(path) >= target

    assert sat(...)


@pytest.mark.skip(reason="not implemented yet")
def test_unsolved_uncrossedknightspath():
    def sat(path: List[List[int]], m=10, n=10, target=62):
        def legal_move(m):
            (a, b), (i, j) = m
            return {abs(i - a), abs(j - b)} == {1, 2}

        def legal_quad(
            m1, m2
        ):  # non-overlapping test: parallel or bounding box has (width - 1) * (height - 1) >= 5
            (i1, j1), (i2, j2) = m1
            (a1, b1), (a2, b2) = m2
            return (
                len({(i1, j1), (i2, j2), (a1, b1), (a2, b2)})
                < 4  # adjacent edges in path, ignore
                or (i1 - i2) * (b1 - b2) == (j1 - j2) * (a1 - a2)  # parallel
                or (max(a1, a2, i1, i2) - min(a1, a2, i1, i2))
                * (max(b1, b2, j1, j2) - min(b1, b2, j1, j2))
                >= 5
                # far
            )

        assert all(i in range(m) and j in range(n) for i, j in path), "move off board"
        assert len({(i, j) for i, j in path}) == len(path), "visited same square twice"

        moves = list(zip(path, path[1:]))
        assert all(legal_move(m) for m in moves), "illegal move"
        assert all(legal_quad(m1, m2) for m1 in moves for m2 in moves), (
            "intersecting move pair"
        )

        return len(path) >= target

    assert sat(...)


@pytest.mark.skip(reason="not implemented yet")
def test_unsolved_uncrossedknightspath_1():
    def sat(path: List[List[int]], m=11, n=11, target=77):
        def legal_move(m):
            (a, b), (i, j) = m
            return {abs(i - a), abs(j - b)} == {1, 2}

        def legal_quad(
            m1, m2
        ):  # non-overlapping test: parallel or bounding box has (width - 1) * (height - 1) >= 5
            (i1, j1), (i2, j2) = m1
            (a1, b1), (a2, b2) = m2
            return (
                len({(i1, j1), (i2, j2), (a1, b1), (a2, b2)})
                < 4  # adjacent edges in path, ignore
                or (i1 - i2) * (b1 - b2) == (j1 - j2) * (a1 - a2)  # parallel
                or (max(a1, a2, i1, i2) - min(a1, a2, i1, i2))
                * (max(b1, b2, j1, j2) - min(b1, b2, j1, j2))
                >= 5
                # far
            )

        assert all(i in range(m) and j in range(n) for i, j in path), "move off board"
        assert len({(i, j) for i, j in path}) == len(path), "visited same square twice"

        moves = list(zip(path, path[1:]))
        assert all(legal_move(m) for m in moves), "illegal move"
        assert all(legal_quad(m1, m2) for m1 in moves for m2 in moves), (
            "intersecting move pair"
        )

        return len(path) >= target

    assert sat(...)


@pytest.mark.skip(reason="not implemented yet")
def test_unsolved_uncrossedknightspath_2():
    def sat(path: List[List[int]], m=12, n=12, target=95):
        def legal_move(m):
            (a, b), (i, j) = m
            return {abs(i - a), abs(j - b)} == {1, 2}

        def legal_quad(
            m1, m2
        ):  # non-overlapping test: parallel or bounding box has (width - 1) * (height - 1) >= 5
            (i1, j1), (i2, j2) = m1
            (a1, b1), (a2, b2) = m2
            return (
                len({(i1, j1), (i2, j2), (a1, b1), (a2, b2)})
                < 4  # adjacent edges in path, ignore
                or (i1 - i2) * (b1 - b2) == (j1 - j2) * (a1 - a2)  # parallel
                or (max(a1, a2, i1, i2) - min(a1, a2, i1, i2))
                * (max(b1, b2, j1, j2) - min(b1, b2, j1, j2))
                >= 5
                # far
            )

        assert all(i in range(m) and j in range(n) for i, j in path), "move off board"
        assert len({(i, j) for i, j in path}) == len(path), "visited same square twice"

        moves = list(zip(path, path[1:]))
        assert all(legal_move(m) for m in moves), "illegal move"
        assert all(legal_quad(m1, m2) for m1 in moves for m2 in moves), (
            "intersecting move pair"
        )

        return len(path) >= target

    assert sat(...)


@pytest.mark.skip(reason="not implemented yet")
def test_unsolved_uncrossedknightspath_3():
    def sat(path: List[List[int]], m=13, n=13, target=114):
        def legal_move(m):
            (a, b), (i, j) = m
            return {abs(i - a), abs(j - b)} == {1, 2}

        def legal_quad(
            m1, m2
        ):  # non-overlapping test: parallel or bounding box has (width - 1) * (height - 1) >= 5
            (i1, j1), (i2, j2) = m1
            (a1, b1), (a2, b2) = m2
            return (
                len({(i1, j1), (i2, j2), (a1, b1), (a2, b2)})
                < 4  # adjacent edges in path, ignore
                or (i1 - i2) * (b1 - b2) == (j1 - j2) * (a1 - a2)  # parallel
                or (max(a1, a2, i1, i2) - min(a1, a2, i1, i2))
                * (max(b1, b2, j1, j2) - min(b1, b2, j1, j2))
                >= 5
                # far
            )

        assert all(i in range(m) and j in range(n) for i, j in path), "move off board"
        assert len({(i, j) for i, j in path}) == len(path), "visited same square twice"

        moves = list(zip(path, path[1:]))
        assert all(legal_move(m) for m in moves), "illegal move"
        assert all(legal_quad(m1, m2) for m1 in moves for m2 in moves), (
            "intersecting move pair"
        )

        return len(path) >= target

    assert sat(...)
