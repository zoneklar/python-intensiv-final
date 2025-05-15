import pytest
from chatbot.bot import Chatbot
from unittest.mock import patch


@pytest.fixture
def bot():
    return Chatbot("TestBot")


def test_greet(bot):
    assert bot.greet() == "Hallo! Ich bin TestBot. Wie kann ich helfen?"


@pytest.mark.parametrize(
    "status, expected",
    [
        (200, "Antwort empfangen"),
        (500, "Fehler"),
    ],
)
def test_ask_api_mock(bot, status, expected):
    with patch("chatbot.bot.requests.get") as mock_get:
        mock_get.return_value.status_code = status
        antwort = bot.ask_api("Hallo?")
        assert expected in antwort


def test_remember(bot):
    bot.remember("hallo welt")
    bot.remember("guten tag")
    assert "hallo welt" in bot.history
    assert len(bot.history) == 2


def test_has_seen(bot):
    bot.remember("ich mag Käse")
    bot.remember("hast du Brot?")
    assert bot.has_seen("Käse") is True
    assert bot.has_seen("Milch") is False


@pytest.mark.parametrize(
    "msg, expected",
    [
        ("Hi", "Bitte etwas ausführlicher."),
        ("Hallo wie geht's?", "Danke für die ausführliche Nachricht."),
    ],
)
def test_respond_length_hint(bot, msg, expected):
    assert bot.respond_length_hint(msg) == expected


def test_get_from_history_valid(bot):
    bot.remember("Hallo")
    assert bot.get_from_history(0) == "Hallo"


def test_get_from_history_invalid(bot):
    bot.remember("Nur eine Nachricht")
    with pytest.raises(IndexError, match="Ungültiger Index"):
        bot.get_from_history(3)
