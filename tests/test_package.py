"""Smoke test: the package installs and imports. Real tests come with real code."""

import pydeep


def test_version_is_set() -> None:
    assert pydeep.__version__ == "0.1.0"
