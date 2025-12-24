#!/usr/bin/python3
"""Return the JSON representation (string) of an object."""


import json


def to_json_string(my_obj):
    """Convert an object to a JSON string."""
    return json.dumps(my_obj)
