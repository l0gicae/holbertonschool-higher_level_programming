#!/usr/bin/python3
"""Append a string to a UTF-8 text file and return the character count."""


def append_write(filename="", text=""):
    """Append text to a UTF-8 file and return number of characters added."""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
