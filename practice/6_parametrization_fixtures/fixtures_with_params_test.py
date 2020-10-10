import pytest


# Parameterization by fixture
def test_parametrized_with_fixture(fixture_with_params):
    print("\nThe value from fixture = ", fixture_with_params)
    assert fixture_with_params > 2


# Parameterisation with one parameter
@pytest.mark.parametrize("test_input", [1, 2, 3])
def test_parametrize_with_mark_single(test_input):
    assert test_input < 3


# Using multiple parameters
@pytest.mark.parametrize("test_input, expected", [("3+5", 8), ("2+4", 6), ("6*9", 42)],
                         ids=["Three + Five", "Two + Four", "Six by Nine"])
def test_parametrize_with_mark_multiple(test_input, expected):
    assert eval(test_input) == expected


# Nested parameterization
@pytest.mark.parametrize("x", [0, 1])
@pytest.mark.parametrize("y", [2, 3])
def test_foo(x, y):
    print(x, y)
