from stacks.balanced_symbols import balanced_symbols
from stacks.par_checker import par_checker
from stacks.rev_string import rev_string


def test_rev_string_reverses_string():
    assert rev_string("apple") == "elppa"


def test_rev_string_handles_empty_string():
    assert rev_string("") == ""


def test_par_checker_accepts_balanced_parentheses():
    assert par_checker("((()()))") is True


def test_par_checker_rejects_unmatched_closing_parenthesis():
    assert par_checker(")(") is False


def test_par_checker_rejects_unmatched_opening_parenthesis():
    assert par_checker("(()") is False


def test_balanced_symbols_accepts_nested_symbols():
    assert balanced_symbols("[{()}]") is True


def test_balanced_symbols_rejects_wrong_nesting():
    assert balanced_symbols("([)]") is False


def test_balanced_symbols_accepts_empty_string():
    assert balanced_symbols("") is True