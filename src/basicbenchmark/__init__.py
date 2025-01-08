import importlib.metadata

from basicbenchmark.benchmark import benchmark as benchmark
from basicbenchmark.benchmark import benchmark_stats as benchmark_stats
from basicbenchmark.decorators import benchmark_stats_me as benchmark_stats_me

__version__ = importlib.metadata.version("basicbenchmark")
