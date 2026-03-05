import argparse

from analyzer import most_active_authors, commit_messages
from models import Commit


def main():

    parser = argparse.ArgumentParser(description="Analyze commit stats")

    parser.add_argument(
        "--top",
        type=int,
        default=3,
        help="Number of top contributors to show",
    )

    parser.add_argument(
        "--author",
        type=str,
        help="Filter commits by author",
    )

    args = parser.parse_args()

    commits = [
        Commit("Sasha", "Initial commit"),
        Commit("Bob", "Bug fix"),
        Commit("Daniel", "Says help"),
        Commit("Sasha", "Pro max"),
    ]

    top = most_active_authors(commits, args.top)

    print("Top contributors:")

    for author, count in top:
        print(author, count)

    # Determine which authors we want messages for
    if args.author:
        authors = [args.author]
    else:
        authors = [author for author, _ in top]

    print("\nCommit messages:")

    for message in commit_messages(commits, authors):
        print(message)


if __name__ == "__main__":
    main()