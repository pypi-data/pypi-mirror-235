import pytest
from .idx import Idx

intervals = [
    {"begin": 1, "end": 2},
    {"begin": 1, "end": 4},
    {"begin": 1.1, "end": 2},
]

tests = [
    # Query for intervals contained by a query
    {"query": "get_intervals_contained_by", "interval": [1.05, 8], "expected_result": 1},
    {"query": "get_intervals_contained_by", "interval": [1, 2], "expected_result": 2},
    {"query": "get_intervals_contained_by", "interval": [0, 10], "expected_result": 3},
    # Query for intervals that contain a query
    {"query": "get_intervals_containing", "interval": [1.3, 1.6], "expected_result": 3},
    {"query": "get_intervals_containing", "interval": [0, 8], "expected_result": 0},
    {"query": "get_intervals_containing", "interval": [1, 2], "expected_result": 2},
]

@pytest.fixture
def idx():
    idx = Idx()
    for interval in intervals:
        begin = interval.get("begin")
        end = interval.get("end")
        idx.insert(begin, end, interval)
    return idx

@pytest.mark.parametrize("test", tests)
def test_idx(idx, test):
    query_results = getattr(idx, test.get("query"))(*test.get("interval"))
    assert len(query_results) == test.get("expected_result")
