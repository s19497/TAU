import pytest

from src.main import MyClass


@pytest.mark.parametrize("test_input,expected", [(0, 0), (1, 1), (2, 1), (19, 4181)])
def test_edge(test_input, expected):
    assert MyClass.fib(test_input) == expected
