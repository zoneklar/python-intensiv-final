import pytest
from chatbot.helper import clean_message, count_words


@pytest.mark.parametrize(
    "text, expected",
    [
        ("Hallo Welt", 2),
        (" ein  Test ", 2),
        ("", 0),
    ],
)
def test_count_words(text, expected):
    assert count_words(text) == expected


def test_clean_message():
    assert clean_message("  HALLO  ") == "hallo"
