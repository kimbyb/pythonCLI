import argparse

from analyzer import most_active_authors, commit_messages
from models import Commit

def main():

    parser = argparse.ArgumentParser(description='Analyze commits stats')

    parser.add_argument(
        "--top",
        type=int,
        default=3,
        help="Number of top contributors to show"
    )

    args = parser.parse_args()

    commits = [
    Commit("Sasha", "Initial commit"),
    Commit("Bob", "Bug fix"),
    Commit("Daniel", "Says hellp"),
    Commit("Sasha", "Pro max"),
    ]

    top = most_active_authors(commits, args.top)

    top_authors = [author for author, _ in top]

    print("Top contributors:")

    for author, count in top:
        print(author, count)

    print("\nCommit messages:")
    for message in commit_messages(commits, top_authors):
        print(author, message)

if __name__ == "__main__":
    main()