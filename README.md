# pythonCLI

## Overview

`pythonCLI` is a Python-based command-line tool for analyzing GitHub commit data. The repository includes modules for interacting with the GitHub API and processing commit activity.

## Usage

Analyze commits from a local file: `python main.py`

Analyze a repository: `python main.py --repo owner/repo`

Show more contributors: `python main.py --repo owner/repo --top 5`

Limit number of commits fetched: `python main.py --repo owner/repo --limit 100`

Filter by author: `python main.py --repo owner/repo --author username`

## Arguments

- `--repo` — repository in `owner/repo` format
- `--file` — commit JSON file (default: `commits.json`)
- `--top` — number of top contributors (default: 3)
- `--limit` — number of commits to fetch (default: 50)
- `--author` — filter commit messages by author

## Project Structure

- `main.py` — CLI entry point
- `github_api.py` — GitHub API interaction
- `analyzer.py` — commit analysis logic
- `models.py` — data models
- `storage.py` — data loading utilities
- `utils.py` — helper functions
- `commits.json` — example commit data
- `tests/` — test suite

## Requirements

- Python 3.x
