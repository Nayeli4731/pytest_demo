import pytest


""" def test_multiplication():
    assert 0 * 5 == 0

def test_multiplication():
    assert 1 * 5 == 5

def test_multiplication():
    assert 2 * 5 == 10

def test_multiplication():
    assert -4 * -5 == -15 """


@pytest.mark.parametrize("a,b,expected", [(0, 5, 0), (1, 5, 5), (2, 5, 11), (-3, 5, -15), (-4, -5, 20)])
def test_multiplication(a, b, expected):
    assert a * b == expected
