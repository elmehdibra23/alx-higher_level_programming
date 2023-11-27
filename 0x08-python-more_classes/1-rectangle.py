#!/usr/bin/python3
"""
1-rectangle, built for Holberton Python project 0x08 task 1.
"""


class Rectangle:
    """
    Rectangle class with private instance attributes for width and height.
    """

    def __init__(self, width=0, height=0):
        """Initializes a Rectangle instance.

        Args:
            width (int): Horizontal dimension, defaults to 0.
            height (int): Vertical dimension, defaults to 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter for the horizontal dimension of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the horizontal dimension of the rectangle.

        Args:
            value (int): Horizontal dimension.

        Raises:
            TypeError: If `value` is not an int.
            ValueError: If `value` is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError('Width must be an integer')
        if value < 0:
            raise ValueError('Width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """Getter for the vertical dimension of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the vertical dimension of the rectangle.

        Args:
            value (int): Vertical dimension.

        Raises:
            TypeError: If `value` is not an int.
            ValueError: If `value` is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError('Height must be an integer')
        if value < 0:
            raise ValueError('Height must be >= 0')
        self.__height = value

