import pytest
from flo import mocker
from task_scheduler.topic_search.websites_to_search import britannica_search ,wikipedia_search

pytestmark = [pytest.mark.version_2]


def test_britannica_search():
    diffs = mocker(britannica_search, path="tests/search_test/test_britannica_search.txt")
    assert not diffs, diffs

def test_wikipedia_search():
    diffs = mocker(wikipedia_search, path="tests/search_test/test_wikipedia_search.txt")
    assert not diffs, diffs



    