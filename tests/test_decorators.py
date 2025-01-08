from basicbenchmark import basicbenchmark


@basicbenchmark(n_runs=10)
def dummy_func_no_args():
    pass


@basicbenchmark(n_runs=10)
def dummy_func_with_args(x, y):
    return x + y


@basicbenchmark(n_runs=10)
def dummy_func_with_kwargs(x, y=0):
    return x + y


@basicbenchmark(pre_run=True, n_runs=10)
def dummy_func_with_pre_run():
    pass


@basicbenchmark(n_runs=1)
def dummy_func_with_autorange():
    pass


def test_basic_benchmark_stats_with_no_args(capfd):
    dummy_func_no_args()

    captured = capfd.readouterr()
    assert captured.out[:47] == "dummy_func_no_args: 10 runs, mean time per run:"


def test_basic_benchmark_stats_with_args(capfd):
    func_return = dummy_func_with_args(1, 2)

    assert func_return == 3

    captured = capfd.readouterr()
    assert captured.out[:49] == "dummy_func_with_args: 10 runs, mean time per run:"


def test_basic_benchmark_stats_with_kwargs(capfd):
    func_return = dummy_func_with_kwargs(x=2)

    assert func_return == 2

    captured = capfd.readouterr()
    assert captured.out[:51] == "dummy_func_with_kwargs: 10 runs, mean time per run:"


def test_basic_benchmark_stats_with_pre_run(capfd):
    dummy_func_with_pre_run()

    captured = capfd.readouterr()
    assert captured.out[:52] == "dummy_func_with_pre_run: 10 runs, mean time per run:"
