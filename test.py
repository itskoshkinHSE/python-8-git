import pytest
from main import add_numbers, multiply_numbers, divide_numbers


def test_add_numbers():
    assert add_numbers(1, 2) == 3
    assert add_numbers(-1, -1) == -2
    assert add_numbers(0, 0) == 0


def test_multiply_numbers():
    assert multiply_numbers(3, 4) == 12
    assert multiply_numbers(-1, 5) == -5
    assert multiply_numbers(0, 100) == 0


def test_divide_numbers():
    assert divide_numbers(6, 3) == 2
    assert divide_numbers(5, 2) == 2.5
    with pytest.raises(ValueError):
        divide_numbers(5, 0)


def test_main_functionality():
    a = add_numbers(1, 2)
    b = multiply_numbers(3, 4)
    result = divide_numbers(b, a)
    assert result == 16 / 3
