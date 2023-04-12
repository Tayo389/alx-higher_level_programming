a Rectangle subclas Square."""
Rectangle = __import__('9-rectangle').Rectanglele


class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
        """
        self.integer_validatior("size", size)
        super().__init__(size, size)
        self.__size = size
