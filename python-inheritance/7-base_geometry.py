#!/usr/bin/python3
"""Defines a BaseGeometry class with area and integer validation."""


class BaseGeometry:
    """Base geometry class."""

    def area(self):
        """Raise Exception because area is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is a positive integer."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
