#!/usr/bin/python3
"""Write an object to a text file using JSON representation."""


import json


def save_to_json_file(my_obj, filename):
    """Serialize my_obj to JSON and write it to filename."""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
