import pytest


def count_even(arr: list[int]) -> int:
    """Count the number of even numbers in an array."""
    return sum(1 for x in arr if x % 2 == 0)


# Your tests can also be benchmarks
@pytest.mark.benchmark
def test_count_even():
    assert count_even(range(1000)) == 500
