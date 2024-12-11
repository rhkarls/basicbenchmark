import pytest

from basicbenchmark.benchmark import benchmark


def test_basic_benchmark_with_no_args():
    def dummy_func():
        pass

    assert benchmark(dummy_func, n_runs=10) == pytest.approx(0, abs=0.001)


def test_basic_benchmark_with_args():
    def dummy_func(x, y):
        return x + y

    assert benchmark(dummy_func, args=(1, 2), n_runs=10) == pytest.approx(0, abs=0.001)


def test_basic_benchmark_with_kwargs():
    def dummy_func(x, y=0):
        return x + y

    assert benchmark(dummy_func, kwargs={"x": 2}, n_runs=10) == pytest.approx(
        0, abs=0.001
    )


def test_basic_benchmark_with_pre_run():
    def dummy_func():
        pass

    assert benchmark(dummy_func, pre_run=True, n_runs=10) == pytest.approx(0, abs=0.001)


def test_basic_benchmark_with_autorange():
    def dummy_func():
        pass

    assert benchmark(dummy_func) == pytest.approx(0, abs=0.001)
