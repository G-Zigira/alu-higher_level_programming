#!/usr/bin/python3
"""
this module contains the definition of the Square class
"""


class Square:
    """
    a class that defines a square by its size
    """

    def __init__(self, size=0):
        """
        initialize the square with a private instance attribute size

       
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculate and return the area of the square
        """
        return self.__size ** 2
