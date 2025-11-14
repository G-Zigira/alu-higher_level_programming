#!/usr/bin/python3
"""defining the square class """

class Square:
    """    represents a square with a given size """
    
    def __init__(self, size):
        """initializes the square object with a specific size from either assignment from the source code or the users"""
        self.__size = size
