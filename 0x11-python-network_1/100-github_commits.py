#!/usr/bin/python3
"""
Fetches the 10 most recent commits from
a given GitHub repository by a specified owner.
Prints each commit in the format: <sha>: <author name>
"""
import requests
import sys

if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]

    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"
    params = {'per_page': 10}

    response = requests.get(url, params=params)
    commits = response.json()

    for commit in commits:
        sha = commit.get('sha')
        author_name = commit.get('commit').get('author').get('name')
        print(f"{sha}: {author_name}")
