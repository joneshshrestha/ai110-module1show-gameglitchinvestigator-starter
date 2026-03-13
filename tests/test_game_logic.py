from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[1]))

from logic_utils import check_guess, get_range_for_difficulty, parse_guess


def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"


def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"


def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"


def test_hint_message_when_guess_too_high():
    # Regression: original code showed "Go HIGHER!" when guess was above secret.
    # Correct hint when guess > secret is "Go LOWER!".
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert (
        "LOWER" in message
    ), f"Expected 'LOWER' in hint for a too-high guess, got: {message!r}"


def test_hint_message_when_guess_too_low():
    # Regression: original code showed "Go LOWER!" when guess was below secret.
    # Correct hint when guess < secret is "Go HIGHER!".
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert (
        "HIGHER" in message
    ), f"Expected 'HIGHER' in hint for a too-low guess, got: {message!r}"


def test_difficulty_ranges_match_progression():
    # Regression check: Easy < Normal < Hard range width.
    easy_low, easy_high = get_range_for_difficulty("Easy")
    normal_low, normal_high = get_range_for_difficulty("Normal")
    hard_low, hard_high = get_range_for_difficulty("Hard")

    assert (easy_low, easy_high) == (1, 20)
    assert (normal_low, normal_high) == (1, 50)
    assert (hard_low, hard_high) == (1, 100)


# --- Regression: parse_guess was raising NotImplementedError (moved from app.py) ---


def test_parse_guess_valid_integer():
    # Bug: parse_guess raised NotImplementedError before being implemented in logic_utils.
    ok, value, err = parse_guess("42")
    assert ok is True
    assert value == 42
    assert err is None


def test_parse_guess_valid_float_string():
    # Floats like "3.7" should be truncated to int, not rejected.
    ok, value, err = parse_guess("3.7")
    assert ok is True
    assert value == 3
    assert err is None


def test_parse_guess_empty_string():
    ok, value, err = parse_guess("")
    assert ok is False
    assert value is None
    assert err is not None


def test_parse_guess_none_input():
    ok, value, err = parse_guess(None)
    assert ok is False
    assert value is None
    assert err is not None


def test_parse_guess_non_numeric_string():
    ok, value, err = parse_guess("abc")
    assert ok is False
    assert value is None
    assert err is not None


# --- Regression: New Game reset used hardcoded (1, 100) instead of difficulty range ---


def test_new_game_secret_within_easy_range():
    # Bug: after a New Game, secret was always drawn from (1, 100) regardless of difficulty.
    # get_range_for_difficulty must return (1, 20) for Easy so secrets stay in that range.
    import random

    low, high = get_range_for_difficulty("Easy")
    for _ in range(50):
        secret = random.randint(low, high)
        assert 1 <= secret <= 20, (
            f"Easy secret {secret} is outside (1, 20) — "
            "likely caused by hardcoded (1, 100) range in new-game reset"
        )


def test_new_game_secret_within_hard_range():
    # Hard range is (1, 100); secrets must never exceed 100.
    import random

    low, high = get_range_for_difficulty("Hard")
    for _ in range(50):
        secret = random.randint(low, high)
        assert 1 <= secret <= 100
