#!/usr/bin/python3
"""
a Python script that takes in a letter and sends a POST request to
"http://0.0.0.0:5000/search_user" with the letter as a parameter.
"""

import requests
import sys

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    q = sys.argv[1] if len(sys.argv) > 1 else ""

    data = {"q": q}
    response = requests.post(url, data=data)

    try:
        response.raise_for_status()
        data = response.json()

        if data:
            for user in data:
                print(f"[{user['id']}] {user['name']}")
        else:
            print("No result")
    except requests.exceptions.RequestException as e:
        print("Error:", e)
    except ValueError:
        print("Not a valid JSON")
