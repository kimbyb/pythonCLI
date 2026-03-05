from analyzer import most_active_authors
from models import Commit


def test_most_active_authors():

    commits = [
        Commit("Alice", "msg1"),
        Commit("Bob", "msg2"),
        Commit("Alice", "msg3"),
    ]

    result = most_active_authors(commits, 1)

    assert result == [("Alice", 2)]