#!/usr/bin/python3
"""
a Python script that takes 2 arguments in order to solve this challenge.
"""

import requests
import sys


if __name__ == "__main__":
    owner, repo = sys.argv[1:]
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"

    response = requests.get(url)
    response.raise_for_status()

    data = response.json()

    for commit in data[:10]:
        sha = commit["sha"]
        author_name = commit["commit"]["author"]["name"]
        print(f"{sha}: {author_name}")
