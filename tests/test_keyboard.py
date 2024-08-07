import pytest

from src.keyboard import Keyboard


@pytest.fixture
def kb():
    return Keyboard('Dark Project KD87A', 9600, 5)


def test_constructor(kb):
    assert kb.name == "Dark Project KD87A"
    assert kb.price == 9600
    assert kb.quantity == 5


def test_calculate_total_price(kb):
    assert kb.calculate_total_price() == 48000


def test_apply_discount(kb):
    kb.pay_rate = 0.8
    kb.apply_discount()
    assert kb.price == 7680


def test_str(kb):
    assert str(kb) == "Dark Project KD87A"


def test_str_lang(kb):
    assert str(kb.language) == "EN"


def test_change_lang(kb):
    kb.change_lang()
    assert str(kb.language) == "RU"
