import pytest

from basicbenchmark.benchmark import _seconds_to_display_time


def test_seconds_to_display_time_seconds():
    assert _seconds_to_display_time(2.5) == (2.5, "s")


def test_seconds_to_display_time_milliseconds():
    assert _seconds_to_display_time(0.1) == (100.0, "ms")


def test_seconds_to_display_time_microseconds():
    assert _seconds_to_display_time(0.000001) == (1.0, "µs")


def test_seconds_to_display_time_nanoseconds():
    assert _seconds_to_display_time(0.000000001) == (1.0, "ns")


def test_seconds_to_display_time_forced_unit():
    assert _seconds_to_display_time(0.000001, force_unit="ms") == (0.001, "ms")


def test_seconds_to_display_time_edge_case_zero():
    assert _seconds_to_display_time(0) == (0.0, "ns")


def test_seconds_to_display_time_invalid_force_unit():
    with pytest.raises(ValueError):
        _seconds_to_display_time(1, force_unit="invalid_unit")
