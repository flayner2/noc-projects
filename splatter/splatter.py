import p5


class Splatter:
    """Basically every figure in pygame is a Rect at the end of the day, but a Splatter
    is just a colored circle.
    """

    def __init__(
        self,
        x: float = 0,
        y: float = 0,
        radius: float = 1,
        fill: tuple = (0, 0, 0, 255),
    ) -> None:
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
        self.x = x
        self.y = y
        self.radius = radius

        # Fill colors
        self.r, self.g, self.b, self.a = fill

    def show(self, sd: float = 1, mean_x: float = 0, mean_y: float = 0) -> None:
        """Draws the Splatter to the screen, with a random color defined by a Gaussian
        distribution. The Splatters are scattered around the center of the screen, with
        their positions also following a Gaussian distribution.

        Args:
            surface (pygame.Surface): the Surface in which the Splatter is going to be
            drawn.
            color (pygame.Color, optional): the color for the Splatter object. Defaults
            to pygame.Color(0, 0, 0), which translates to solid black.
            sd (float): defines the percentage of the fake "mean" of the distribution
            that is gonna be used to calculate a fake "standard deviation" for the
            position of the splatters. Defaults to 0.2.
            color_sd (float): defines the "standard deviation" for the color of the
            splatters. Defaults to 1.0.
        """

        # Pick a random position
        self.x = p5.random_gaussian(mean_x, sd)
        self.y = p5.random_gaussian(mean_y, sd)

        p5.fill(r=self.r, g=self.g, b=self.b, a=self.a)
        p5.no_stroke()
        p5.circle((self.x, self.y), self.radius)
