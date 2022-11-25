import pytest
from utils import Utils


def test_addition():
    assert 1 + 1 == 2


def test_sub():
    assert 1 - 1 == 2


def test_square():
    assert Utils.pow(2) == 4
