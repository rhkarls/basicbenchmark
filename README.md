# basicbenchmark

[![PyPI - Version](https://img.shields.io/pypi/v/basicbenchmark.svg)](https://pypi.org/project/basicbenchmark)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/basicbenchmark.svg)](https://pypi.org/project/basicbenchmark)
[![tests and linting](https://github.com/rhkarls/basicbenchmark/actions/workflows/run_tests.yml/badge.svg)](https://github.com/rhkarls/basicbenchmark/actions/workflows/run_tests.yml)
[![codecov](https://codecov.io/github/rhkarls/basicbenchmark/graph/badge.svg?token=69XQYRBK5I)](https://codecov.io/github/rhkarls/basicbenchmark)

basicbenchmark is a simple benchmarking tool for timing Python callables.

It's so basic, that probably you don't need it. But if you do, here it is.
It runs a callable a number of times and returns the average time it took.
Optionally, you can also get some basic statistics: fastest and slowest run time, and the standard deviation.

No dependencies, just a simple wrapper around python standard library `timeit.Timer` and `time.perf_counter`.

## Installation

```bash
pip install basicbenchmark
```

## Usage

The package provides two functions: `benchmark` and `benchmark_stats`.

The `benchmark` function takes a callable, optional arguments and keyword arguments, and runs it a number of times, returning only the average time it took to run the callable in seconds.
It supports auto ranging the number of runs to get an accurate result, as it is a wrapper around `timeit.Timer`, or you can specify the number of runs yourself with the `n_runs` argument.

The `benchmark_stats` function takes the same input arguments as `benchmark`, but instead return a dictionary with the average time, the standard deviation, the fastest and the slowest time in seconds.
This is useful if you want to know more about the distribution of the times it took to run the callable, and not just the average. In some cases the fastest time is of more interest than the average.

Both functions print the results to the console in more readable time units, but this can be disabled by setting the `print_result` argument to `False`.
Both functions also support a `pre_run` argument, which runs the callable once before performing the benchmark. Useful for example when calling JIT compiled functions.

```python
from basicbenchmark import benchmark, benchmark_stats

def my_function(x, y=2):
    return x**y
```

The most basic way to time a function is to use the `benchmark` function, which uses auto ranging to decide the number
of runs required (if argument `n_runs` is not passed), and allows for passing arguments and keyword arguments to the callable.
The example below times the function `my_function` with `x=2` and `y=2`, and returns the average time to `avg_time`:
```python
avg_time = benchmark(my_function, args=(2,))
```
Result is printed to the console

``` my_function: 5,000,000 runs, mean time per run: 72.37 ns. ```

To also get some basic statistics, use the `benchmark_stats` function. This function does not support automatically determining the number of runs, so you need to specify the number of runs yourself.
The example below uses the `benchmark_stats` with keyword arguments to pass to the callable:

```python
timing_stats = benchmark_stats(my_function, kwargs={'x': 100, 'y': 3}, n_runs=100_000)
```

It returns the following dictionary:
```python
timing_stats
{'mean': 1.5315201089833864e-07, 'stdev': 5.44664144321298e-07, 'min': 9.998620953410864e-08, 'max': 0.00013040000339969993}
```

And prints to console:
```
my_function: 100,000 runs, mean time per run: 153.15±544.66 ns.
Fastest run: 99.99 ns. Slowest run: 130400.00 ns.
```
