import pygame
from random import gauss


class Splatter(pygame.Rect):
    """Basically every figure in pygame is a Rect at the end of the day, but a Splatter
    is just a colored circle.
    """

    def __init__(self, x: int = 0, y: int = 0, w: int = 0, h: int = 1) -> None:
        """Instantiates a Splatter object at position `(x, y)` and with width and
        height = `(w, h)`.

        Args:
            x (int): the position of the Splatter object in the x axis.
            y (int): the position of the Splatter object in the y axis.
            w (int): the width of the Splatter object. Defines the circle radius.
            Defaults to 1.
            h (int): the height of the Splatter object. Defines if the circle should
            be filled or the thickness of the outline. Defaults to 0.
        """
        super().__init__(x, y, w, h)

    def draw(self, surface: pygame.Surface, sd: float = 0.2) -> None:
        """Draws the Splatter to the screen, with a random color defined by a Gaussian
        distribution. The Splatters are scattered around the center of the screen, with
        their positions also following a Gaussian distribution.

        Args:
            surface (pygame.Surface): the Surface in which the Splatter is going to be
            drawn.
            sd (float): defines the percentage of the fake "mean" of the distribution
            that is gonna be used to calculate a fake "standard deviation". Defaults to
            0.2.
        """
        # First, pick a random color
        red = abs(round(gauss(0, 1) * 100 % 255))
        green = abs(round(gauss(0, 1) * 100 % 255))
        blue = abs(round(gauss(0, 1) * 100 % 255))
        color = pygame.Color(red, green, blue)

        # Get the center positions of the screen
        half_width = round(surface.get_width() / 2)
        half_height = round(surface.get_height() / 2)

        # Calculate the sd as a percentage of the "mean"
        sd_x = sd * half_width
        sd_y = sd * half_height

        # Then, pick a random position
        x = round(gauss(half_width, sd_x))
        y = round(gauss(half_height, sd_y))

        pygame.draw.circle(surface, color, (x, y), self.height, self.width)
