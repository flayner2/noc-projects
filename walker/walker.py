import pygame
import p5
from random import uniform, gauss
from funcs import monte_carlo, monte_exp
from noise import pnoise1
import numpy as np


class Walker:
    """The Walker class is a simple random walker agent represented by a
    two-dimensional square.
    """

    def __init__(
        self,
        x: float,
        y: float,
        z: float = 0,
        stroke: tuple[int] = (0, 0, 0, 255),
        stroke_weight: int = 1,
    ) -> None:
        """Instantiates a Walker object at position `(x, y)` and with width and
        height = `(w, h)`.

        Args:
            x (int): the position of the Walker object in the x axis
            y (int): the position of the Walker object in the y axis
            w (int): the width of the Walker object
            h (int): the height of the Walker object
        """

        # Position of the Walker
        self.x = x
        self.y = y
        self.z = z
        # Stroke color and weight (thickness)
        self.sr, self.sg, self.sb, self.sa = stroke
        self.stroke_weight = stroke_weight

    def show(self) -> None:
        """Draws the Walker to the screen, defaulting to a black colored Walker

        Args:
            surface (pygame.Surface): the Surface in which the Walker is going to be
            drawn
            color (pygame.Color, optional): the color for the Walker object. Defaults
            to pygame.Color(0, 0, 0), which translates to solid black.
        """
        p5.stroke_weight(self.stroke_weight)
        p5.stroke(self.sr, self.sg, self.sb, self.sa)
        p5.point(self.x, self.y, self.z)

    def step(self) -> None:
        """Updates the Walker's position"""
        # The value for each axis of the step the Walker is going to take each frame
        x_step = uniform(-1, 1)
        y_step = uniform(-1, 1)

        self.x += x_step
        self.y += y_step


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
        x_step = round(uniform(-1, 1))
        y_step = round(uniform(-1, 1))

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
    """A Walker class that moves with a step size defined by a Gaussian distribution"""

    def __init__(
        self, x: int, y: int, w: int, h: int, mu: float = 0.0, sd: float = 1.0
    ) -> None:
        """Instantiates a GaussianWalker object at position `(x, y)` and with width and
        height = `(w, h)`.

        Args:
            x (int): the position of the Walker object in the x axis
            y (int): the position of the Walker object in the y axis
            w (int): the width of the Walker object
            h (int): the height of the Walker object
        """
        super().__init__(x, y, w, h)
        self.mu = mu
        self.sd = sd

    def step(self) -> None:
        """Updates the Walker's position based on a step size defined by a
        Gaussian distribution of random values"""
        # The value for each axis of the step the Walker is going to take each frame
        x_step = round(gauss(self.mu, self.sd))
        y_step = round(gauss(self.mu, self.sd))

        self.left += x_step
        self.top += y_step


class MonteCarloWalker(Walker):
    """A Walker with varying step sizes calculated by the Monte Carlo method"""

    def __init__(self, x: int, y: int, w: int, h: int, min: float, max: float) -> None:
        """Instantiates a MonteCarloWalker object at position `(x, y)` and with width
        and height = `(w, h)`.

        Args:
            x (int): the position of the Walker object in the x axis
            y (int): the position of the Walker object in the y axis
            w (int): the width of the Walker object
            h (int): the height of the Walker object
            max (float): the maximum number generated by the Monte Carlo method
            min (float): the minimum number generated by the Monte Carlo method
        """
        super().__init__(x, y, w, h)
        self.max = max
        self.min = min

    def step(self) -> None:
        """Updates the Walker's position based on a step size defined by a
        Monte Carlo random sampling"""
        x_step = round(monte_carlo(min=self.min, max=self.max))
        y_step = round(monte_carlo(min=self.min, max=self.max))

        self.left += x_step
        self.top += y_step


class ExponentialMonteCarloWalker(Walker):
    """A Walker with varying step sizes calculated by the Monte Carlo method, with
    the probability of a number being picked as an exponential function"""

    def __init__(
        self, x: int, y: int, w: int, h: int, min: float, max: float, exp: float
    ) -> None:
        """Instantiates a MonteCarloWalker object at position `(x, y)` and with width
        and height = `(w, h)`.

        Args:
            x (int): the position of the Walker object in the x axis
            y (int): the position of the Walker object in the y axis
            w (int): the width of the Walker object
            h (int): the height of the Walker object
            max (float): the maximum number generated by the Monte Carlo method
            min (float): the minimum number generated by the Monte Carlo method
            exp (float): the exponent that defines the exponential function
        """
        super().__init__(x, y, w, h)
        self.max = max
        self.min = min
        self.exp = exp

    def step(self) -> None:
        """Updates the Walker's position based on a step size defined by a
        Monte Carlo random sampling"""
        x_step = round(monte_exp(min=self.min, max=self.max, exp=self.exp))
        y_step = round(monte_exp(min=self.min, max=self.max, exp=self.exp))

        self.left += x_step
        self.top += y_step


class NoiseWalker(Walker):
    """A Walker with varying step sizes calculated by a PerlinNoise function"""

    def __init__(
        self,
        x: int,
        y: int,
        w: int,
        h: int,
        surface_width: int,
        surface_height: int,
        tx: float = 0.0,
        ty: float = 0.0,
        inc: float = 0.001,
    ) -> None:
        """Instantiates a NoiseWalker object at position `(x, y)` and with width
        and height = `(w, h)`.

        Args:
            x (int): the position of the Walker object in the x axis
            y (int): the position of the Walker object in the y axis
            w (int): the width of the Walker object
            h (int): the height of the Walker object
            surface_width (int): the width of the surface to draw
            surface_height (int): the height of the surface to draw
            tx (float): the initial "time" for the x axis
            ty (float): the initial "time" for the y axis
            inc (float): the increment for each iteration
        """
        super().__init__(x, y, w, h)
        self.tx = tx
        self.ty = ty
        self.inc = inc
        self.s_width = surface_width
        self.s_heigth = surface_height

    def step(self) -> None:
        """Updates the Walker's position based on a step size defined by a
        Monte Carlo random sampling"""
        self.left = round(np.interp(pnoise1(self.tx), [-1, 1], [0, self.s_width]))
        self.top = round(np.interp(pnoise1(self.ty), [-1, 1], [0, self.s_heigth]))
        print(self.left, self.top)

        self.tx += self.inc
        self.ty += self.inc
