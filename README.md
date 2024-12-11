# basicbenchmark

This is a basic benchmarking tool for timing Python callables.

It's so basic, that probably you don't need it. But if you do, here it is.
No dependencies, just a simple wrapper around `timeit.Timer` and `time.perf_counter`.

## Installation

> [!NOTE]
> Package is not yet published to pypi.org

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

Using auto ranging and passing arguments:
```python
avg_time = benchmark(my_function, args=(2,))
my_function: 5,000,000 runs, mean time per run: 72.37 ns.
```

Calling the benchmark_stats with keyword arguments to pass to the callable, and a specific number of runs:
```python
timing_stats = benchmark_stats(my_function, kwargs={'x': 100, 'y': 3}, n_runs=100_000)
my_function: 100,000 runs, mean time per run: 153.15±544.66 ns.
Fastest run: 99.99 ns. Slowest run: 130400.00 ns.

timing_stats
{'mean': 1.5315201089833864e-07, 'stdev': 5.44664144321298e-07, 'min': 9.998620953410864e-08, 'max': 0.00013040000339969993}

```
