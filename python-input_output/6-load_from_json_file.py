#!/usr/bin/python3
"""Create a Python object from a JSON file."""


import json


def load_from_json_file(filename):
    """Read JSON from filename and return the corresponding Python object."""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
