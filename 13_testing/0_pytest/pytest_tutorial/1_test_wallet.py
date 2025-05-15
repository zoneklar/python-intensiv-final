"""
Unit tests for the Wallet class.

Nutzung:
    python -m pytest 1_test_wallet.py -v
"""

import pytest
from wallet import Wallet, InsufficientAmount


def test_default_initial_amout():
    """Testen, ob ein neues Wallet einen Initialwert von 100 hat."""
    w = Wallet(initial_amount=100)
    assert w.balance == 100


def test_add_cash():
    w = Wallet(initial_amount=100)
    w.add_cash(200)
    assert w.balance == 300


if __name__ == "__main__":
    w = Wallet(initial_amount=400)
    w.spend_cash(400)
