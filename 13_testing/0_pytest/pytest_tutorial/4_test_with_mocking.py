"""
Unittests mit Mocking

Mocking erlaubt dir, externe oder teure Aufrufe im Test zu simulieren und
stattdessen zu kontrollieren, ob sie korrekt aufgerufen wurde.

- Verwende Mock, wenn du das Zielobjekt direkt besitzt (z. B. Methoden
deiner eigenen Klasse).

- Verwende patch, wenn du externe Aufrufe oder Module temporär
  austauschen willst.

python -m pytest 4_test_with_mocking.py

"""

import pytest
from unittest.mock import Mock, patch
from wallet import Wallet


@pytest.fixture
def wallet():
    return Wallet(20)


def test_add_cash_extended(wallet):
    """Api Mock Beispiel"""
    wallet.update_payment_service = Mock(return_value=200)
    wallet.add_cash_extended(100)
    assert wallet.balance == 120
    wallet.update_payment_service.assert_called_once_with(100)


def test_add_cash_test(wallet):
    with patch("wallet.Wallet.ask_api_echo") as mock_get:
        mock_get.return_value = (
            200,
            {"echo": "TEST"},
        )

        status_code, response = wallet.ask_api_echo("test")
        assert response["echo"] == "TEST"  # Check the 'echo' key in the response
        assert status_code == 200
        # überweisen von Geld und testen, ob Betrag da, wenn echo TEST ist
        wallet.add_cash_test(100)
        assert wallet.balance == 120
