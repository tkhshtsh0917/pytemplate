"""
memory_analyzer
"""

import tracemalloc


def check_allocation():
    """
    check_allocation
    """

    tracemalloc.start()

    print("Hello, world!")

    snapshot = tracemalloc.take_snapshot()
    top_stats = snapshot.statistics("lineno")

    print("[ Top 10 ]")
    _ = [print(stat) for stat in top_stats[:10]]


def check_memoryleak():
    """
    check_memoryleak
    """

    tracemalloc.start()

    print("Hello, world!")
    snapshot1 = tracemalloc.take_snapshot()
    print("Hello, world!")
    snapshot2 = tracemalloc.take_snapshot()

    top_stats = snapshot2.compare_to(snapshot1, "lineno")

    print("[ Top 10 differences ]")
    _ = [print(stat) for stat in top_stats[:10]]
