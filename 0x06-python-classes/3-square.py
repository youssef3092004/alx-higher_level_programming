#!/usr/bin/python3
"""Square Module"""
class Square:
    def __init__(self, size=0):
        """Construct
        size: length of a side of the square
        TypeError: If size is not an integer
        ValueError: If size in less than 0"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    def area(self):
        return self.__size ** 2
