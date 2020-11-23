"""
__main__
"""

import time
import tracemalloc


class MemoryAllocationAnalyzer:
    """
    MemoryAllocationAnalyzer
    """

    def __init__(self):
        self.snap = None
        self.size = None

    def __enter__(self):
        tracemalloc.start()

        self.snap = tracemalloc.take_snapshot()
        self.size = sum(stat.size for stat in self.snap.statistics("filename"))

        print("--- START ---")
        for stat in self.snap.statistics("lineno"):
            print(stat)

        return self

    def __exit__(self, ex_type, ex_value, trace):
        snap = tracemalloc.take_snapshot()
        size = sum(stat.size for stat in snap.statistics("filename"))

        for stat in snap.compare_to(self.snap, "lineno"):
            print(stat)

        diff = abs(self.size - size)
        print("--- END ---")

        print("*** RESULT ***")
        print("Memory allocated: {:,} Bytes".format(diff))
        print("**************")

        return False


class BenchmarkAnalyzer:
    """
    BenchmarkAnalyzer
    """

    def __init__(self):
        self.start = None

    def __enter__(self):
        print("--- START ---")
        self.start = time.time()
        return self

    def __exit__(self, ex_type, ex_value, trace):
        end = time.time()
        print(f"time = {end - self.start}")
        print("--- END ---")
        return False
