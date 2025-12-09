#!/usr/bin/python3
"""
Task 02 - Using requests to fetch, parse and save API data.
Fetches posts from JSONPlaceholder and processes them.
"""

import requests
import csv


def fetch_and_print_posts():
    """Fetches posts and prints the status code + all post titles."""
    url = "https://jsonplaceholder.typicode.com/posts"

    response = requests.get(url)
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        try:
            posts = response.json()
        except ValueError:
            print("Error: Response is not valid JSON")
            return

        for post in posts:
            print(post.get("title"))


def fetch_and_save_posts():
    """Fetches posts and saves id, title, body fields into posts.csv"""
    url = "https://jsonplaceholder.typicode.com/posts"

    response = requests.get(url)

    if response.status_code == 200:
        try:
            posts = response.json()
        except ValueError:
            print("Error: Response is not valid JSON")
            return

        data_to_save = [
            {
                "id": post.get("id"),
                "title": post.get("title"),
                "body": post.get("body")
            }
            for post in posts
        ]

        with open("posts.csv", mode="w", newline="", encoding="utf-8") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(data_to_save)
