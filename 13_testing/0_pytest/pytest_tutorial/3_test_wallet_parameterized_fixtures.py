"""
Unit tests for the Wallet class using parameterized tests and fixtures.

Nutzung:
python -m pytest 3_test_wallet_parameterized_fixtures.py -v
"""

import pytest
from wallet import Wallet, InsufficientAmount


@pytest.fixture
def empty_wallet():
    return Wallet(initial_amount=0)


@pytest.mark.parametrize(
    "earned, spent, expected",
    [
        (30, 10, 20),
        (20, 2, 18),
    ],
)
def test_transactions(empty_wallet, earned, spent, expected):
    empty_wallet.add_cash(earned)
    empty_wallet.spend_cash(spent)
    assert empty_wallet.balance == expected


if __name__ == "__main__":
    w = Wallet(initial_amount=400)
    w.spend_cash(400)
