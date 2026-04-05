from typing import List

import pytest


@pytest.mark.skip(reason="not implemented yet")
def test_quadraticroot():
    def sat(x: float, coeffs=[2.5, 1.3, -0.5]):
        a, b, c = coeffs
        return abs(a * x**2 + b * x + c) < 1e-6

    assert sat(...)


@pytest.mark.skip(reason="not implemented yet")
def test_quadraticroot_1():
    def sat(
        x: float,
        coeffs=[0.0685642998539026, -0.10446230957339113, -0.11141402891228723],
    ):
        a, b, c = coeffs
        return abs(a * x**2 + b * x + c) < 1e-6

    assert sat(...)


@pytest.mark.skip(reason="not implemented yet")
def test_quadraticroot_2():
    def sat(
        x: float, coeffs=[0.2622487694588566, 0.48521166316030495, -41.749384651642444]
    ):
        a, b, c = coeffs
        return abs(a * x**2 + b * x + c) < 1e-6

    assert sat(...)


@pytest.mark.skip(reason="not implemented yet")
def test_quadraticroot_3():
    def sat(
        x: float, coeffs=[145.72190605632582, 0.027358325157428014, -5.149342624051854]
    ):
        a, b, c = coeffs
        return abs(a * x**2 + b * x + c) < 1e-6

    assert sat(...)


@pytest.mark.skip(reason="not implemented yet")
def test_quadraticroot_4():
    def sat(
        x: float, coeffs=[1.1222556871110754, -0.007015312913509468, -309237.6867547677]
    ):
        a, b, c = coeffs
        return abs(a * x**2 + b * x + c) < 1e-6

    assert sat(...)


@pytest.mark.skip(reason="not implemented yet")
def test_allquadraticroots():
    def sat(roots: List[float], coeffs=[1.3, -0.5]):
        b, c = coeffs
        r1, r2 = roots
        return abs(r1 + r2 + b) + abs(r1 * r2 - c) < 1e-6

    assert sat(...)


@pytest.mark.skip(reason="not implemented yet")
def test_allquadraticroots_1():
    def sat(roots: List[float], coeffs=[-1.468548989307175, -0.9453828447181172]):
        b, c = coeffs
        r1, r2 = roots
        return abs(r1 + r2 + b) + abs(r1 * r2 - c) < 1e-6

    assert sat(...)


@pytest.mark.skip(reason="not implemented yet")
def test_allquadraticroots_2():
    def sat(roots: List[float], coeffs=[-2.0230245559088815, -0.23831699388987454]):
        b, c = coeffs
        r1, r2 = roots
        return abs(r1 + r2 + b) + abs(r1 * r2 - c) < 1e-6

    assert sat(...)


@pytest.mark.skip(reason="not implemented yet")
def test_allquadraticroots_3():
    def sat(roots: List[float], coeffs=[-33.7903719275386, -5.03161654339928]):
        b, c = coeffs
        r1, r2 = roots
        return abs(r1 + r2 + b) + abs(r1 * r2 - c) < 1e-6

    assert sat(...)


@pytest.mark.skip(reason="not implemented yet")
def test_allquadraticroots_4():
    def sat(roots: List[float], coeffs=[9.155105839032705, -0.9467446341738642]):
        b, c = coeffs
        r1, r2 = roots
        return abs(r1 + r2 + b) + abs(r1 * r2 - c) < 1e-6

    assert sat(...)


@pytest.mark.skip(reason="not implemented yet")
def test_cubicroot():
    def sat(x: float, coeffs=[2.0, 1.0, 0.0, 8.0]):
        return abs(sum(c * x ** (3 - i) for i, c in enumerate(coeffs))) < 1e-6

    assert sat(...)


@pytest.mark.skip(reason="not implemented yet")
def test_cubicroot_1():
    def sat(
        x: float,
        coeffs=[
            0.009597657937719273,
            -10.297175825569942,
            0.15891220226280925,
            10.530249049250433,
        ],
    ):
        return abs(sum(c * x ** (3 - i) for i, c in enumerate(coeffs))) < 1e-6

    assert sat(...)


@pytest.mark.skip(reason="not implemented yet")
def test_cubicroot_2():
    def sat(
        x: float,
        coeffs=[
            -0.17749172356645268,
            -1.3894267878542186,
            0.03752944532850555,
            0.2624916128068381,
        ],
    ):
        return abs(sum(c * x ** (3 - i) for i, c in enumerate(coeffs))) < 1e-6

    assert sat(...)


@pytest.mark.skip(reason="not implemented yet")
def test_cubicroot_3():
    def sat(
        x: float,
        coeffs=[
            0.41725114111706524,
            155.2589446092116,
            -0.10619077904258341,
            -0.024129284994425074,
        ],
    ):
        return abs(sum(c * x ** (3 - i) for i, c in enumerate(coeffs))) < 1e-6

    assert sat(...)


@pytest.mark.skip(reason="not implemented yet")
def test_cubicroot_4():
    def sat(
        x: float,
        coeffs=[
            -2.3153234528266906,
            11.247619504308075,
            -72.3705721705674,
            53.97429005428236,
        ],
    ):
        return abs(sum(c * x ** (3 - i) for i, c in enumerate(coeffs))) < 1e-6

    assert sat(...)


@pytest.mark.skip(reason="not implemented yet")
def test_allcubicroots():
    def sat(roots: List[float], coeffs=[1.0, -2.0, -1.0]):
        r1, r2, r3 = roots
        a, b, c = coeffs
        return (
            abs(r1 + r2 + r3 + a)
            + abs(r1 * r2 + r1 * r3 + r2 * r3 - b)
            + abs(r1 * r2 * r3 + c)
            < 1e-6
        )

    assert sat(...)


@pytest.mark.skip(reason="not implemented yet")
def test_allcubicroots_1():
    def sat(
        roots: List[float],
        coeffs=[291.6393860094841, -235.56805995170293, 46.827662118172],
    ):
        r1, r2, r3 = roots
        a, b, c = coeffs
        return (
            abs(r1 + r2 + r3 + a)
            + abs(r1 * r2 + r1 * r3 + r2 * r3 - b)
            + abs(r1 * r2 * r3 + c)
            < 1e-6
        )

    assert sat(...)


@pytest.mark.skip(reason="not implemented yet")
def test_allcubicroots_2():
    def sat(
        roots: List[float],
        coeffs=[-0.25228902661371166, -0.1500677342820565, 0.04095001209455085],
    ):
        r1, r2, r3 = roots
        a, b, c = coeffs
        return (
            abs(r1 + r2 + r3 + a)
            + abs(r1 * r2 + r1 * r3 + r2 * r3 - b)
            + abs(r1 * r2 * r3 + c)
            < 1e-6
        )

    assert sat(...)


@pytest.mark.skip(reason="not implemented yet")
def test_allcubicroots_3():
    def sat(
        roots: List[float],
        coeffs=[-0.7564145326509102, -0.6902422688120567, 0.4732575941427041],
    ):
        r1, r2, r3 = roots
        a, b, c = coeffs
        return (
            abs(r1 + r2 + r3 + a)
            + abs(r1 * r2 + r1 * r3 + r2 * r3 - b)
            + abs(r1 * r2 * r3 + c)
            < 1e-6
        )

    assert sat(...)


@pytest.mark.skip(reason="not implemented yet")
def test_allcubicroots_4():
    def sat(
        roots: List[float],
        coeffs=[5.119999240806329, -7.551441647258393, -21.440710634524915],
    ):
        r1, r2, r3 = roots
        a, b, c = coeffs
        return (
            abs(r1 + r2 + r3 + a)
            + abs(r1 * r2 + r1 * r3 + r2 * r3 - b)
            + abs(r1 * r2 * r3 + c)
            < 1e-6
        )

    assert sat(...)
