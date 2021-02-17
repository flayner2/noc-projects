import pygame
from random import uniform, gauss


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
            y (int): the position of the Walker object in the y axis
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
        x_step = int(round(uniform(-1, 1)))
        y_step = int(round(uniform(-1, 1)))

        self.left += int(x_step)
        self.top += int(y_step)


class BottomRightSkewedWalker(Walker):
    """A Walker class with a tendency to move down and to the right"""

    def __init__(self, x: int, y: int, w: int, h: int) -> None:
        """Instantiates a BottomRightSkewedWalker object at position `(x, y)` and with
        width and height = `(w, h)`.

        Args:
            x (int): the position of the Walker object in the x axis
            y (int): the position of the Walker object in the y axis
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


class MouseFollowerWalker(Walker):
    """A Walker class with a tendency to move towards the cursor position"""

    def __init__(self, x: int, y: int, w: int, h: int) -> None:
        """Instantiates a MouseFollowerWalker object at position `(x, y)` and with
        width and height = `(w, h)`.

        Args:
            x (int): the position of the Walker object in the x axis
            y (int): the position of the Walker object in the y axis
            w (int): the width of the Walker object
            h (int): the height of the Walker object
        """
        super().__init__(x, y, w, h)

    def step(self, probability: float = 0.5) -> None:
        """Updates the Walker's position, with a tendency of moving towards the cursor
        position

        Args:
            probability (float, optional): The probability that the walker will try to
            move towards the cursor. Defaults to 0.5.
        """
        # The chance of the Walker moving towards the cursor
        chance = uniform(0, 1)

        # The value for each axis of the step the Walker is going to take each frame
        # if chance > probability
        x_step = int(round(uniform(-1, 1)))
        y_step = int(round(uniform(-1, 1)))

        # If the Walker feels like following the mouse...
        if chance <= probability:
            # Get the current position of the cursor
            mouse_pos = pygame.mouse.get_pos()

            # If the cursor is further right, move right
            if mouse_pos[0] - self.left > 0:
                self.left += 1
            # Else, move left
            else:
                self.left -= 1

            # If the cursor is further down, move down
            if mouse_pos[1] - self.top > 0:
                self.top += 1
            # Else, move up
            else:
                self.top -= 1
        # Otherwise, just move randomly
        else:
            self.left += x_step
            self.top += y_step


class GaussianWalker(Walker):
    """A Walker class that moves with a Gaussian random distribution"""

    def __init__(self, x: int, y: int, w: int, h: int) -> None:
        """Instantiates a GaussianWalker object at position `(x, y)` and with width and
        height = `(w, h)`.

        Args:
            x (int): the position of the Walker object in the x axis
            y (int): the position of the Walker object in the y axis
            w (int): the width of the Walker object
            h (int): the height of the Walker object
        """
        super().__init__(x, y, w, h)

    def step(self, mu: float = 1, sd: float = 1) -> None:
        """Updates the Walker's position based on a Gaussian distribution of random
        values"""
        # The value for each axis of the step the Walker is going to take each frame
        x_step = int(round(gauss(mu, sd)))
        y_step = int(round(gauss(mu, sd)))

        self.left += x_step
        self.top += y_step
