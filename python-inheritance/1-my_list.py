#!/usr/bin/python3
"""Defines MyList, a list subclass with a sorted print helper."""


class MyList(list):
    """A list subclass that can print itself sorted."""

    def print_sorted(self):
        """Print the list in ascending order without modifying it."""
        print(sorted(self))
