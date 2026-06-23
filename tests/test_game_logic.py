"""
Regression tests targeting the bugs fixed in check_guess (logic_utils.py).

check_guess(guess, secret) returns a (outcome, message) tuple:
    - "Win"      -> guess equals secret
    - "Too High" -> guess is greater than secret  (hint must point LOWER)
    - "Too Low"  -> guess is less than secret      (hint must point HIGHER)
"""

from logic_utils import check_guess


# --- Outcome correctness -----------------------------------------------------

def test_winning_guess_returns_win():
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"


def test_guess_above_secret_is_too_high():
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"


def test_guess_below_secret_is_too_low():
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


# --- Bug #1: hint direction was backwards ------------------------------------
# Previously "Too High" told the player to go HIGHER and "Too Low" told them
# to go LOWER. The fix flips these so the guidance matches the outcome.

def test_too_high_hint_points_lower():
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message.upper()
    assert "HIGHER" not in message.upper()


def test_too_low_hint_points_higher():
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message.upper()
    assert "LOWER" not in message.upper()


# --- Bug #2: TypeError when secret was compared as a string ------------------
# The old app cast secret to str on alternating attempts, crashing with
# "'>' not supported between instances of 'int' and 'str'". check_guess must
# now handle plain int-vs-int comparisons without raising.

def test_int_comparison_does_not_raise():
    # Should simply return a result, not blow up.
    check_guess(70, 30)
    check_guess(30, 70)
    check_guess(50, 50)


def test_boundary_one_above_and_below():
    assert check_guess(51, 50)[0] == "Too High"
    assert check_guess(49, 50)[0] == "Too Low"
