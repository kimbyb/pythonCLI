import argparse

from analyzer import most_active_authors, commit_messages
from storage import load_commits_from_file
from github_api import fetch_commits


def main():

    parser = argparse.ArgumentParser(description="Analyze commit stats")

    parser.add_argument("--top", type=int, default=3, help="Number of top contributors")
    parser.add_argument("--author", type=str, nargs="*", help="Commit authors")
    parser.add_argument("--file", type=str, default="commits.json", help="Commit file")
    parser.add_argument("--repo", type=str, help="Repository name")
    parser.add_argument("--limit", type=int, default=50, help="Number of commits to fetch")

    args = parser.parse_args()

    # Decide source of commits
    if args.repo:
        owner, repo = args.repo.split("/")
        commits = fetch_commits(owner, repo)
    else:
        commits = load_commits_from_file(args.file)

    # Analyze contributors
    top = most_active_authors(commits, args.top)

    print("Top contributors:")

    for author, count in top:
        print(author, count)

    # Determine authors to filter
    if args.author:
        authors = [args.author]
    else:
        authors = [author for author, _ in top]

    commits = fetch_commits(owner, repo, args.limit)

    print("\nCommit messages:")

    for message in commit_messages(commits, authors):
        print(message)


if __name__ == "__main__":
    main()