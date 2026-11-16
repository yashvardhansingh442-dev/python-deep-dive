"""Tests for pydeep.inputs, using scripted input instead of a keyboard."""

from collections.abc import Callable, Iterator

import pytest

from pydeep.inputs import read_days, read_income, read_numbers


def scripted(*answers: str) -> tuple[Callable[[str], str], list[str]]:
    """Return an input function that replays ``answers``, and a message log."""
    it: Iterator[str] = iter(answers)
    log: list[str] = []

    def fake_input(prompt: str) -> str:
        return next(it)

    return fake_input, log


def run(
    fn: Callable[..., object], *answers: str, **kwargs: object
) -> tuple[object, list[str]]:
    fake_input, log = scripted(*answers)
    result = fn(input_fn=fake_input, output_fn=log.append, **kwargs)
    return result, log


# ---- read_days --------------------------------------------------------------


def test_read_days_accepts_positive_integer() -> None:
    result, log = run(read_days, " 7 ")
    assert result == 7
    assert log == []


@pytest.mark.parametrize("bad", ["0", "-3", "2.5", "abc", "", "²", "٣"])
def test_read_days_rejects_bad_values_then_accepts(bad: str) -> None:
    result, log = run(read_days, bad, "4")
    assert result == 4
    assert len(log) == 1


# ---- read_numbers -----------------------------------------------------------


def test_read_numbers_accepts_commas_and_spaces() -> None:
    result, _ = run(read_numbers, "80, 90 100", prompt="Food: ", expected=3)
    assert result == [80.0, 90.0, 100.0]


def test_read_numbers_rejects_non_numbers() -> None:
    result, log = run(read_numbers, "10 abc", "10 20", prompt="x", expected=2)
    assert result == [10.0, 20.0]
    assert "numbers only" in log[0]


def test_read_numbers_rejects_wrong_count() -> None:
    result, log = run(read_numbers, "1 2 3", "1 2", prompt="x", expected=2)
    assert result == [1.0, 2.0]
    assert "exactly 2" in log[0]


def test_read_numbers_rejects_negative() -> None:
    result, log = run(read_numbers, "5 -1", "5 1", prompt="x", expected=2)
    assert result == [5.0, 1.0]
    assert "negative" in log[0]


@pytest.mark.parametrize("bad", ["nan 1", "1 inf", "-inf 1"])
def test_read_numbers_rejects_nan_and_inf(bad: str) -> None:
    result, log = run(read_numbers, bad, "1 2", prompt="x", expected=2)
    assert result == [1.0, 2.0]
    assert len(log) == 1


# ---- read_income ------------------------------------------------------------


def test_read_income_accepts_zero_and_positive() -> None:
    assert run(read_income, "0")[0] == 0.0
    assert run(read_income, "1500.50")[0] == 1500.5


@pytest.mark.parametrize("bad", ["abc", "-5", "nan", "inf", ""])
def test_read_income_rejects_bad_values(bad: str) -> None:
    result, log = run(read_income, bad, "100")
    assert result == 100.0
    assert len(log) == 1
