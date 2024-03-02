#!/usr/bin/python3
"""
a Python script that takes in a letter and sends a POST request to
"http://0.0.0.0:5000/search_user" with the letter as a parameter.
"""

import requests
import sys


if __name__ == "__main__":
    query = argv[1] if len(argv) > 1 else ""

    url = "http://0.0.0.0:5000/search_user"

    response = requests.post(url, data={"q": query})

    try:
        data = response.json()

        if not data or not any(key in data for key in ("id", "name")):
            print("No result")
        else:
            user_id = data.get("id")
            user_name = data.get("name")
            print(f"[{user_id}] {user_name}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    except ValueError:
        print("Not a valid JSON")
