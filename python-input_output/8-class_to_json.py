#!/usr/bin/python3
"""Return a dict description of an object for JSON serialization."""


def class_to_json(obj):
    """Return the dictionary representation of obj."""
    return obj.__dict__
