#!/usr/bin/python3
"""Check if an object is an instance of a class or of a subclass."""


def is_kind_of_class(obj, a_class):
    """Return True if obj is an instance of a_class or inherits from it."""
    return isinstance(obj, a_class)
