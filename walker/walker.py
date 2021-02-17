import pygame
from random import randint, uniform


class Walker(pygame.Rect):
    """The Walker class is a simple random walker agent represented by a
    two-dimensional square.
    """

    def __init__(
        self,
        x: int,
        y: int,
        w: int,
        h: int,
    ) -> None:
        """Instantiates a Walker object at position `(x, y)` and with width and
        height = `(w, h)`.

        Args:
            x (int): the position of the Walker object in the x axis
            y (int): the position of the Walker object in the x axis
            w (int): the width of the Walker object
            h (int): the height of the Walker object
        """
        super().__init__(x, y, w, h)

    def draw(
        self, surface: pygame.Surface, color: pygame.Color = pygame.Color(0, 0, 0)
    ) -> None:
        """Draws the Walker to the screen, defaulting to a black colored Walker

        Args:
            surface (pygame.Surface): the Surface in which the Walker is going to be
            drawn
            color (pygame.Color, optional): the color for the Walker object. Defaults
            to pygame.Color(0, 0, 0), which translates to solid black.
        """
        pygame.draw.rect(surface, color, self)

    def step(self) -> None:
        """Updates the Walker's position"""
        # The value for each axis of the step the Walker is going to take each frame
        x_step = randint(-1, 1)
        y_step = randint(-1, 1)

        self.left += x_step
        self.top += y_step


class BottomRightSkewedWalker(Walker):
    """A Walker class with a tendency to move down and to the right"""

    def __init__(self, x: int, y: int, w: int, h: int) -> None:
        """Instantiates a BottomRightSkewedWalker object at position `(x, y)` and with width and
        height = `(w, h)`.

        Args:
            x (int): the position of the Walker object in the x axis
            y (int): the position of the Walker object in the x axis
            w (int): the width of the Walker object
            h (int): the height of the Walker object
        """
        super().__init__(x, y, w, h)

    def step(self, probability: float = 0.6) -> None:
        """Updates the Walker's position, with a bottom-right skew

        Args:
            probability (float, optional): The probability that the walker will go to
            the bottom-right of the screen. Defaults to 0.6.
        """
        # The value for each axis of the step the Walker is going to take each frame
        x_step = uniform(0, 1)
        y_step = uniform(0, 1)

        if x_step <= probability:
            self.left += 1
        else:
            self.left -= 1

        if y_step <= probability:
            self.top += 1
        else:
            self.top -= 1
