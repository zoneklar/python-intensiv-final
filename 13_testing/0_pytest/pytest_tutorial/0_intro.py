"""
# Pytest Tutorials:

## Pytest Primer
https://realpython.com/pytest-python-testing/

## Django Pytest
https://djangostars.com/blog/django-pytest-testing/

## good pytest tutorial
https://semaphoreci.com/community/tutorials/testing-python-applications-with-pytest

call this: python -m pytest 0_intro.py
"""

import pytest


def capital_case(x):
    if not isinstance(x, str):
        raise TypeError("Please provide a string argument")
    return x.capitalize()  # test => Test


def capital_case_old(x):
    return x.capitalize()


def test_capital_case():
    assert capital_case("hamburg") == "Hamburg", "String muss capitalizized sein"
    assert (
        capital_case("hamburg city") == "Hamburg city"
    ), "String muss capitalizized sein"


def test_capital_case_exception():
    """Testen, ob bei falschem Typ ein TypeError ausgelöst wird."""
    with pytest.raises(TypeError):
        capital_case(42)
