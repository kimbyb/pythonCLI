from analyzer import commit_messages
from models import Commit

def test_commit_messages():

    commits = [
        Commit("Alice", "A"),
        Commit("Bob", "B"),
    ]

    messages = list(commit_messages(commits, ["Alice", "Bob"]))

    assert messages == ["A", "B"]

def test_commit_messages_filter():

    commits = [
        Commit("Alice", "A"),
        Commit("Bob", "B"),
    ]

    messages = list(commit_messages(commits, ["Alice"]))

    assert messages == ["A"]