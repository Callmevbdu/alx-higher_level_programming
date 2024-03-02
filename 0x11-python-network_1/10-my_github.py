#!/usr/bin/python3
"""
a Python script that takes your GitHub credentials (username and password) and
uses the GitHub API to display your id.
"""

import requests


def get_my_github_id(username, access_token):
    url = f"https://api.github.com/users/{username}"
    headers = {"Authorization": f"token {access_token}"}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data.get("id")
    else:
        print(f"Error: {response.status_code}")
        return None


access_token = "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"


if __name__ == "__main__":
    username = sys.argv[1]
    my_id = get_my_github_id(username, access_token)

    if my_id:
        print(my_id)
    else:
        print("Failed to retrieve ID")
