from collections import Counter
from models import Commit
from utils import meassure_time


@meassure_time
def most_active_authors(commits : list[Commit], n: int):
    authors = [commit.author for commit in commits]
    counter = Counter(authors)
    return counter.most_common(n)


def commit_messages(commits : list[Commit], authors: list[str]):
    for commit in commits:
        if commit.author in authors:
            yield commit.message