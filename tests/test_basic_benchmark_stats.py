import pytest

from basicbenchmark import benchmark_stats


def test_basic_benchmark_stats_with_no_args():
    def dummy_func():
        pass

    result, func_return_value = benchmark_stats(dummy_func, n_runs=10)
    assert isinstance(result["mean"], (int, float))
    assert isinstance(result["stdev"], (int, float))
    assert isinstance(result["min"], (int, float))
    assert isinstance(result["max"], (int, float))

    assert result["mean"] == pytest.approx(0, abs=0.001)
    assert result["min"] == pytest.approx(0, abs=0.001)
    assert result["max"] == pytest.approx(0, abs=0.001)


def test_basic_benchmark_stats_with_args():
    def dummy_func(x, y):
        return x + y

    result, func_return_value = benchmark_stats(dummy_func, args=(1, 2), n_runs=10)

    assert func_return_value == 3

    assert isinstance(result["mean"], (int, float))
    assert isinstance(result["stdev"], (int, float))
    assert isinstance(result["min"], (int, float))
    assert isinstance(result["max"], (int, float))

    assert result["mean"] == pytest.approx(0, abs=0.001)
    assert result["min"] == pytest.approx(0, abs=0.001)
    assert result["max"] == pytest.approx(0, abs=0.001)


def test_basic_benchmark_stats_with_kwargs():
    def dummy_func(x, y=0):
        return x + y

    result, func_return_value = benchmark_stats(dummy_func, kwargs={"x": 2}, n_runs=10)

    assert func_return_value == 2

    assert isinstance(result["mean"], (int, float))
    assert isinstance(result["stdev"], (int, float))
    assert isinstance(result["min"], (int, float))
    assert isinstance(result["max"], (int, float))

    assert result["mean"] == pytest.approx(0, abs=0.001)
    assert result["min"] == pytest.approx(0, abs=0.001)
    assert result["max"] == pytest.approx(0, abs=0.001)


def test_basic_benchmark_stats_with_pre_run():
    def dummy_func():
        pass

    result, func_return_value = benchmark_stats(dummy_func, pre_run=True, n_runs=10)
    assert isinstance(result["mean"], (int, float))
    assert isinstance(result["stdev"], (int, float))
    assert isinstance(result["min"], (int, float))
    assert isinstance(result["max"], (int, float))

    assert result["mean"] == pytest.approx(0, abs=0.001)
    assert result["min"] == pytest.approx(0, abs=0.001)
    assert result["max"] == pytest.approx(0, abs=0.001)


def test_basic_benchmark_stats_with_autorange():
    def dummy_func():
        pass

    result, func_return_value = benchmark_stats(dummy_func, n_runs=1)
    assert isinstance(result["mean"], (int, float))
    assert result["stdev"] is None
    assert result["min"] is None
    assert result["max"] is None

    assert result["mean"] == pytest.approx(0, abs=0.001)
