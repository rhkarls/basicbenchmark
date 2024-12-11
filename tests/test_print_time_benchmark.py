from basicbenchmark.benchmark import _print_time_benchmark


def test_prints_benchmark_with_mean_time():
    assert (
        _print_time_benchmark("test_func", 10, 0.002)
        == "test_func: 10 runs, mean time per run: 2.00 ms."
    )


def test_prints_benchmark_with_mean_and_stdev_time():
    assert (
        _print_time_benchmark("test_func", 10, 0.002, 0.0001)
        == "test_func: 10 runs, mean time per run: 2.00±0.10 ms."
    )


def test_prints_benchmark_with_mean_stdev_and_min_max_time():
    assert (
        _print_time_benchmark("test_func", 10, 0.002, 0.0001, 0.001, 0.003)
        == "test_func: 10 runs, mean time per run: 2.00±0.10 ms.\nFastest run: 1.00 ms. Slowest run: 3.00 ms."
    )


def test_prints_benchmark_with_mean_and_min_max_time():
    assert (
        _print_time_benchmark("test_func", 10, 0.002, min_time=0.001, max_time=0.003)
        == "test_func: 10 runs, mean time per run: 2.00 ms.\nFastest run: 1.00 ms. Slowest run: 3.00 ms."
    )
