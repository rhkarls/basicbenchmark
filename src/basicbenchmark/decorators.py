"""
Decorator function which warps benchmark_stats.
"""

from functools import wraps
from typing import Optional

from basicbenchmark.benchmark import benchmark_stats


def basicbenchmark(n_runs: Optional[int] = None, pre_run: bool = False):
    """
    Decorator function for timing the execution of a callable.

    Parameters
    ----------
    n_runs : int, optional
        The number of times to run the function. The default is None, which will run the function only 1 time.
    pre_run : bool, optional
        If True will run function once before recording times. The default is False.

    Returns
    -------
    function
        The decorator function.
    """

    def decorator(func):  # numpydoc ignore=GL08
        @wraps(func)
        def wrapper(*args, **kwargs):  # numpydoc ignore=GL08
            result = benchmark_stats(
                func, args=args, kwargs=kwargs, n_runs=n_runs, pre_run=pre_run
            )
            return result["return_value"]

        return wrapper

    if callable(n_runs):  # when called without parentheses, n_runs will be the function
        f = n_runs
        n_runs = None  # reset n_runs to default in this case
        return decorator(f)

    # when called with parentheses return the decorator itself
    return decorator
