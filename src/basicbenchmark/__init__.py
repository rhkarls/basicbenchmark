import importlib.metadata

from basicbenchmark.benchmark import benchmark as benchmark
from basicbenchmark.benchmark import benchmark_stats as benchmark_stats
from basicbenchmark.decorators import basicbenchmark as basicbenchmark

__version__ = importlib.metadata.version("basicbenchmark")
