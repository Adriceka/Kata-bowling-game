import pytest
from src.scoreCard import ScoreCard

@pytest.mark.state_n
def test_hitting_pins_regular():
    pins = "12345123451234512345"
    total = 60
    score_card = ScoreCard(pins)
    assert score_card.score() == total

@pytest.mark.state_n
def test_symbol_zero():
    pins = "9-9-9-9-9-9-9-9-9-9-"
    total = 90
    score_card = ScoreCard(pins)
    assert score_card.score() == total

    pins = "9-3561368153258-7181"
    total = 82
    score_card = ScoreCard(pins)
    assert score_card.score() == total

@pytest.mark.spare
def test_spare_not_extra():
    pins = "9-3/613/815/-/8-7/8-"
    total = 121
    score_card = ScoreCard(pins)
    assert score_card.score() == total

@pytest.mark.strike
def test_strike():
    pins = "X9-9-9-9-9-9-9-9-9-"
    total = 100
    score_card = ScoreCard(pins)
    assert score_card.score() == total

    pins = "X9-X9-9-9-9-9-9-9-"
    total = 110
    score_card = ScoreCard(pins)
    assert score_card.score() == total

@pytest.mark.strike
def test_two_strikes():
    pins = "XX9-9-9-9-9-9-9-9-"
    total = 120
    score_card = ScoreCard(pins)
    assert score_card.score() == total

@pytest.mark.strike
def test_three_strikes():
    pins = "XXX9-9-9-9-9-9-9-"
    total = 141
    score_card = ScoreCard(pins)
    assert score_card.score() == total

@pytest.mark.extra_rolls
def test_one_pin_in_extra_roll():
    pins = "9-3/613/815/-/8-7/8/8"
    total = 131
    score_card = ScoreCard(pins)
    assert score_card.score() == total

    pins = "5/5/5/5/5/5/5/5/5/5/5"
    total = 150
    score_card = ScoreCard(pins)
    assert score_card.score() == total

@pytest.mark.extra_rolls
def test_two_strikes_in_extra_rolls():
    pins = "9-9-9-9-9-9-9-9-9-XXX"
    total = 111
    score_card = ScoreCard(pins)
    assert score_card.score() == total

@pytest.mark.extra_rolls
def test_one_strike_in_extra_roll():
    pins = "8/549-XX5/53639/9/X"
    total = 149
    score_card = ScoreCard(pins)
    assert score_card.score() == total

@pytest.mark.extra_rolls
def test_spare_in_extra_roll():
    pins = "X5/X5/XX5/--5/X5/"
    total = 175
    score_card = ScoreCard(pins)
    assert score_card.score() == total

@pytest.mark.extra_rolls
def test_triple_strike_before_extra_rolls():
    pins = "XXXXXXXXXXXX"
    total = 300
    score_card = ScoreCard(pins)
    assert score_card.score() == total