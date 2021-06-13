class Rectangle:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height

    def __str__(self) -> str:
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self, width: int) -> None:
        """ Changes the width of the rectangle. """

        self.width = width

    def set_height(self, height: int) -> None:
        """ Changes the height of the rectangle. """

        self.height = height

    def get_area(self) -> int:
        """ Returns the area of the rectangle. """

        return self.width * self.height

    def get_perimeter(self) -> int:
        """ Returns the perimeter of the rectangle. """

        return (2 * self.width) + (2 * self.height)

    def get_diagonal(self) -> float:
        """ Returns the diagonal line that passes through the rectangle. """

        return ((self.width ** 2) + (self.height ** 2)) ** 0.5
    
    def get_picture(self) -> str:
        """ Prints the rectangle for visualization. """

        if self.width > 50 or self.height > 50:
            return "Too big for picture."

        picture = ""
        for _ in range(self.height):
            picture += f"{'*' * self.width}\n"

        return picture

    def get_amount_inside(self, shape: object) -> int:
        """
        Returns how many times the passed shape (rectangle or square) could
        fit inside the current rectangle (with no rotations).
        """

        return (self.width // shape.width) * (self.height // shape.height)


class Square(Rectangle):
    def __init__(self, side: int) -> None:
        self.width = side
        self.height = side

    def __str__(self) -> str:
        return f"Square(side={self.width})"

    def set_side(self, side: int) -> None:
        """ Changes the side of the square (width and height). """

        self.width = side
        self.height = side
