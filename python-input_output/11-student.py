#!/usr/bin/python3
"""Define a Student class with JSON serialization and reloading."""


class Student:
    """Student class."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return dict representation, optionally filtered by attrs list."""
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace attributes using key/value pairs from a dictionary."""
        for key, value in json.items():
            setattr(self, key, value)
