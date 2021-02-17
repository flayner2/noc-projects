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

    def draw(self, surface: pygame.Surface) -> None:
        # TODO: make the splatters position be relative to the center
        # of the screen
        """Draws the Splatter to the screen, with a random color defined by a Gaussian
        distribution.

        Args:
            surface (pygame.Surface): the Surface in which the Splatter is going to be
            drawn.
        """
        # First, pick a random color
        red = abs(round(gauss(0, 1) * 100 % 255))
        green = abs(round(gauss(0, 1) * 100 % 255))
        blue = abs(round(gauss(0, 1) * 100 % 255))
        color = pygame.Color(red, green, blue)

        # Get the surface's dimensions
        s_width = surface.get_width()
        s_height = surface.get_height()

        # Create boundaries so that the splatters stay closer to the center
        # of the screen
        x_bound = 0.2 * s_width
        y_bound = 0.2 * s_height

        # Then, pick a random position
        x = round(gauss(0, 1) * 100 % s_width)
        y = round(gauss(0, 1) * 100 % s_height)

        # And add constraints to the position based on the boundaries
        if x <= 0:
            x += x_bound
        else:
            x -= x_bound

        if y <= 0:
            y += y_bound
        else:
            y -= y_bound

        pygame.draw.circle(surface, color, (x, y), self.height, self.width)
