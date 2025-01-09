"""
Basic timing benchmarks of a callable.

benchmark: uses timeit to perform the benchmark, and supports auto ranging so that the number of runs do not need
to be provided. Will only return the average run time.

benchmark_stats: uses time.perf_counter to time the function calls, and provides some basic statistics.
Will output standard deviation of all runs, fastest single run and slowest single run, in addition to the average run time.
"""

import statistics
import time
import timeit
from typing import Any, Callable, Optional, Union


def benchmark(
    func: Callable,
    args: Optional[Union[list, tuple]] = None,
    kwargs: Optional[dict] = None,
    print_result: bool = True,
    n_runs: Optional[int] = None,
    pre_run: bool = False,
) -> float:
    """
    Perform a basic timing benchmark of a callable.

    A wrapper around using timeit.Timer.

    Parameters
    ----------
    func : Callable
        The function or callable to benchmark.
    args : tuple, optional
        Argument values to pass to `func`.
        The default is None.
    kwargs : dict, optional
        Keyword arguments to pass to `func`.
        The default is None.
    print_result : bool, optional
        If True, will print benchmark results to the console.
        The default is True.
    n_runs : int, optional
        The number of times to run the function.
        The default is None, which will autorange the number of runs.
    pre_run : bool, optional
        If True, will run the function once before recording times.
        The default is False.

    Returns
    -------
    float
        The mean time of all runs in seconds.
    """
    if kwargs is None:
        kwargs = {}

    if args is None:
        args = ()

    if pre_run:
        func(*args, **kwargs)

    t = timeit.Timer(lambda: func(*args, **kwargs))
    if n_runs:
        total_time = t.timeit(n_runs)
    else:
        n_runs, total_time = t.autorange()

    mean_time = total_time / n_runs

    if print_result:
        print_str = _print_time_benchmark(func.__name__, n_runs, mean_time)
        print(print_str)

    return mean_time


def benchmark_stats(
    func: Callable,
    args: Optional[Union[list, tuple]] = None,
    kwargs: Optional[dict] = None,
    print_result: bool = True,
    n_runs: Optional[int] = None,
    pre_run: bool = False,
) -> dict[str, float | None | Any]:
    """
    A simple time benchmark for a callable with basic statistics.

    Parameters
    ----------
    func : Callable
        The function or callable to benchmark.
    args : List, optional
        Argument values to pass to `func`. The default is None.
    kwargs : Dict, optional
        Keyword arguments to pass to `func`. The default is None.
    print_result : bool, optional
        If True will print benchmark results to the console, the mean runtime with standard deviation, fastest and slowest individual run.
    n_runs : int, optional
        The number of times to run the function. The default is None, which will run the function only 1 time.
    pre_run : bool, optional
        If True will run function once before recording times. The default is False.

    Returns
    -------
    dict
        A dictionary with the following keys:
            - return_value: the callable return value.
            - mean: the average time of `n_runs` calls of `func` in seconds.
            - stdev: standard deviation time of `n_runs` calls of `func` in seconds.
            - min: minimum (fastest) time of all `n_runs` calls of `func` in seconds.
            - max: maximum (slowest) time of all `n_runs` calls of `func` in seconds.
    """

    return_value = None
    times = []

    if kwargs is None:
        kwargs = {}

    if args is None:
        args = ()

    if n_runs is None:
        n_runs = 1

    if pre_run:
        func(*args, **kwargs)

    for _ in range(n_runs):
        t_start = time.perf_counter()
        return_value = func(*args, **kwargs)
        times.append(time.perf_counter() - t_start)

    mean_time = statistics.mean(times)

    if len(times) > 1:
        min_time = min(times)
        max_time = max(times)
    else:
        min_time, max_time = None, None

    try:
        stdev_time = statistics.stdev(times)
    except statistics.StatisticsError:
        stdev_time = None

    if print_result:
        print_str = _print_time_benchmark(
            func.__name__, n_runs, mean_time, stdev_time, min_time, max_time
        )
        print(print_str)

    return {
        "return_value": return_value,
        "mean": mean_time,
        "stdev": stdev_time,
        "min": min_time,
        "max": max_time,
    }


def _print_time_benchmark(
    func_name,
    n_runs,
    mean_time,
    stdev_time=None,
    min_time=None,
    max_time=None,
):
    """
    Format and print the benchmark results to the console.

    Parameters
    ----------
    func_name : str
        The name of the function being benchmarked.
    n_runs : int
        The number of times the function was run.
    mean_time : float
        The mean time per run in seconds.
    stdev_time : float, optional
        The standard deviation of the run times in seconds. Default is None.
    min_time : float, optional
        The fastest run time in seconds. Default is None.
    max_time : float, optional
        The slowest run time in seconds. Default is None.

    Returns
    -------
    str
        A formatted string with the benchmark results in a readable time unit.
    """

    mean_print_time, mean_time_unit = _seconds_to_display_time(mean_time)

    if stdev_time:
        stdev_print_time, _ = _seconds_to_display_time(
            stdev_time, force_unit=mean_time_unit
        )
        stdev_print_str = f"±{stdev_print_time:.2f}"
    else:
        stdev_print_str = ""

    if min_time and max_time:
        min_print_time, _ = _seconds_to_display_time(
            min_time, force_unit=mean_time_unit
        )
        max_print_time, _ = _seconds_to_display_time(
            max_time, force_unit=mean_time_unit
        )
        min_max_print_str = f"\n\tFastest run: {min_print_time:.2f} {mean_time_unit}. Slowest run: {max_print_time:.2f} {mean_time_unit}."
    else:
        min_max_print_str = ""

    return f"{func_name}: {n_runs:,} runs, mean time per run: {mean_print_time:.2f}{stdev_print_str} {mean_time_unit}.{min_max_print_str}"


def _seconds_to_display_time(seconds, force_unit=None):
    """
    Format a value in seconds to the most appropriate unit (s, ms, µs, ns).

    Parameters
    ----------
    seconds : float or int
        The time in seconds to convert to a more human-readable time.
    force_unit : str, optional
        Argument to force the conversion to a specific time unit, must be one of
        s, ms, µs, us, ns.

    Returns
    -------
    time : float
        The time convert from seconds to `unit`.
    unit : str
        The unit string, one of s, ms, µs, ns.

    Examples
    --------
    input_seconds = [
    2.5,  # 2.5 s
    0.1,  # 100 ms
    0.001,  # 1 ms
    0.000001,  # 1 us
    0.000000001,  # 1 ns
    0.0000000001  # 0.1 ns
    ]

    for time_s in input_seconds:
        print(f"Input: {time_s} seconds. Output: {_seconds_to_display_time(time_s)}")

    Input: 2.5 seconds. Output: (2.5, 's')
    Input: 0.1 seconds. Output: (100.0, 'ms')
    Input: 0.001 seconds. Output: (1.0, 'ms')
    Input: 1e-06 seconds. Output: (1.0, 'µs')
    Input: 1e-09 seconds. Output: (1.0, 'ns')
    Input: 1e-10 seconds. Output: (0.1, 'ns')

    _seconds_to_display_time(0.000001)
    (1.0, 'µs')
    _seconds_to_display_time(0.000001, force_unit='ms')
    (0.001, 'ms')
    """

    factor_to_s = {"s": 1, "ms": 1e-3, "µs": 1e-6, "ns": 1e-9}

    if force_unit:
        if force_unit not in ["s", "ms", "µs", "us", "ns"]:
            raise ValueError(
                f'Argument force_unit must be one of "s", "ms", "µs", "us", "ns", '
                f"the provided value {force_unit} is not accepted. "
            )
        if force_unit == "us":
            force_unit = "µs"
        return seconds / factor_to_s[force_unit], force_unit

    for unit, factor in factor_to_s.items():
        if seconds >= factor:
            return seconds / factor, unit

    return seconds / factor_to_s["ns"], "ns"
