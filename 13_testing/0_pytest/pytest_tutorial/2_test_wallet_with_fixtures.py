"""
Unitests für die Wallet-Klasse mit Fixtures. Fixtures können als Parameter in den Test-Funktionen
definiert werden.

Nutzung:
    pytest 2_test_wallet_with_fixtures.py
"""

import pytest
from wallet import Wallet, InsufficientAmount


@pytest.fixture
def empty_wallet():
    return Wallet(initial_amount=0)


@pytest.fixture
def wallet():
    return Wallet(initial_amount=100)


def test_default_initial_amout(wallet):
    """Testen, ob ein neues Wallet einen Initialwert von 100 hat."""
    assert wallet.balance == 100


def test_add_cash(wallet):
    wallet.add_cash(200)
    assert wallet.balance == 300


if __name__ == "__main__":
    w = Wallet(initial_amount=400)
    w.spend_cash(400)
