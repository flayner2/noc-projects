import ursina
from random import randint


class Walker(ursina.Entity):
    """The Walker class is a simple random walker agent represented by a
    two-dimensional square
    """

    def __init__(
        self,
        x: float,
        y: float,
        color: ursina.Color = ursina.color.white,
        scale: tuple[float] = (0.05, 0.05),
    ):
        """Instantiates a Walker object at position (x, y, 0) with color = `color`,
        which defaults to white

        Args:
            x (float): position on the x-axis
            y (float): position on the y-axis
            color (ursina.Color, optional): the color for the Walker object. Defaults
            to ursina.color.white.
            scale (tuple[float]): x and y scale of the Walker object
        """
        super().__init__()

        # Model is hard-coded to be a 2D square, but can be changed with Walker.model
        self.model = "quad"

        # Walker's intial position on the screen
        self.x = x
        self.y = y

        # The size of the Walker
        self.scale = scale

        # Walker's color, defaults to white
        self.color = color

        self.eternal = True
        self.always_on_top = True

    def step(self):
        """Updates the Walker's position based on a step size

        Args:
            step_size (float, optional): the size of each step. Defaults to 0.01.
        """
        # Time delta to make animations look smooth
        delta = ursina.time.dt
        # The actual step the Walker is going to take each frame
        x_step = randint(-1, 1) * delta
        y_step = randint(-1, 1) * delta

        self.x += x_step
        self.y += y_step

    def update(self):
        """Updates the Walker's position each frame"""
        self.step()
