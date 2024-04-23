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
    @property
    def size(self):
        """Construct
        size: length of a side of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    def area(self):
        """Area of this square
        Returns: the size squared"""
        return self.__size ** 2

    def my_print(self):
        """prints this square"""
        if self.size is not 0:
            for i in range(self.size):
                for j in range(self.size):
                    print("#", end="")
                print()
        else:
            print()
