#!/usr/bin/python3
"""
defines a Square class with size validation
"""


class Square:
    """
    represents a square with a given size
    """

    def __init__(self, size=0):
        """
        initializes the square with a specific size
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
