#!/usr/bin/python3
"""1-rectangle, créé pour le projet Holberton Python 0x08 tâche 1.
"""


class Rectangle:
    """À ce stade, la classe crée uniquement des attributs d'instance privés
    en prenant deux arguments.

    Args:
        width (int): dimension horizontale du rectangle, par défaut à 0
        height (int): dimension verticale du rectangle, par défaut à 0

    """
    def __init__(self, width=0, height=0):
        # l'assignation d'attributs ici engage les setters définis ci-dessous
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter pour la dimension horizontale du rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Args:
            value (int): dimension horizontale du rectangle

        Attributes:
            __width (int): dimension horizontale du rectangle

        Raises:
            TypeError: Si `value` n'est pas un entier.
            ValueError: Si `value` est inférieur à 0.

        """
        if type(value) is not int:
            raise TypeError('width doit être un entier')
        elif value < 0:
            raise ValueError('width doit être >= 0')
        self.__width = value

    @property
    def height(self):
        """Getter pour la dimension verticale du rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Args:
            value (int): dimension verticale du rectangle

        Attributes:
            __height (int): dimension verticale du rectangle

        Raises:
            TypeError: Si `value` n'est pas un entier.
            ValueError: Si `value` est inférieur à 0.

        """
        if type(value) is not int:
            raise TypeError('height doit être un entier')
        if value < 0:
            raise ValueError('height doit être >= 0')
        self.__height = value

