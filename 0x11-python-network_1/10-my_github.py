#!/usr/bin/python3
"""
This script takes GitHub credentials (username and personal access token) and
uses the GitHub API to display the user's id.
"""

import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]

    url = f"https://api.github.com/user"
    headers = {'Authorization': f'token {token}'}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        user_data = response.json()
        print(user_data['id'])
    else:
        print("None")
