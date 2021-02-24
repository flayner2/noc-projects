import p5
from funcs import monte_carlo, monte_exp


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
        x_step = p5.random_uniform(low=-1, high=1)
        y_step = p5.random_uniform(low=-1, high=1)

        self.x += x_step
        self.y += y_step


class BottomRightSkewedWalker(Walker):
    """A Walker class with a tendency to move down and to the right"""

    def __init__(
        self,
        x: float,
        y: float,
        z: float = 0,
        stroke: tuple[int] = (0, 0, 0, 255),
        stroke_weight: int = 1,
        probability: float = 0.6,
    ) -> None:
        """Instantiates a BottomRightSkewedWalker object at position `(x, y)` and with
        width and height = `(w, h)`.

        Args:
            x (int): the position of the Walker object in the x axis
            y (int): the position of the Walker object in the y axis
            w (int): the width of the Walker object
            h (int): the height of the Walker object
        """
        super().__init__(x, y, z, stroke, stroke_weight)
        self.probability = probability

    def step(self) -> None:
        """Updates the Walker's position, with a bottom-right skew"""
        # The value for each axis of the step the Walker is going to take each frame
        x_step = p5.random_uniform(low=0, high=1)
        y_step = p5.random_uniform(low=0, high=1)

        chance = p5.random_uniform(low=0, high=1)

        if chance <= self.probability:
            self.x += x_step
        else:
            self.x -= x_step

        if chance <= self.probability:
            self.y += y_step
        else:
            self.y -= y_step


class MouseFollowerWalker(Walker):
    """A Walker class with a tendency to move towards the cursor position"""

    def __init__(
        self,
        x: float,
        y: float,
        z: float = 0,
        stroke: tuple[int] = (0, 0, 0, 255),
        stroke_weight: int = 1,
        probability: float = 0.5,
    ) -> None:
        """Instantiates a MouseFollowerWalker object at position `(x, y)` and with
        width and height = `(w, h)`.

        Args:
            x (int): the position of the Walker object in the x axis
            y (int): the position of the Walker object in the y axis
            w (int): the width of the Walker object
            h (int): the height of the Walker object
        """
        super().__init__(x, y, z, stroke, stroke_weight)
        self.probability = probability

    def step(self, probability: float = 0.5) -> None:
        """Updates the Walker's position, with a tendency of moving towards the cursor
        position

        Args:
            probability (float, optional): The probability that the walker will try to
            move towards the cursor. Defaults to 0.5.
        """
        # The chance of the Walker moving towards the cursor
        chance = p5.random_uniform(low=0, high=1)

        # The value for each axis of the step the Walker is going to take each frame
        # if chance > probability
        x_step = p5.random_uniform(low=0, high=1)
        y_step = p5.random_uniform(low=0, high=1)

        # If the Walker feels like following the mouse...
        if chance <= probability:
            # If the cursor is further right, move right
            if mouse_x - self.x > 0:
                self.x += x_step
            # Else, move left
            else:
                self.x -= x_step

            # If the cursor is further down, move down
            if mouse_y - self.y > 0:
                self.y += y_step
            # Else, move up
            else:
                self.y -= y_step
        # Otherwise, just move randomly
        else:
            self.x += x_step
            self.y += y_step


class GaussianWalker(Walker):
    """A Walker class that moves with a step size defined by a Gaussian distribution"""

    def __init__(
        self,
        x: float,
        y: float,
        z: float = 0,
        stroke: tuple[int] = (0, 0, 0, 255),
        stroke_weight: int = 1,
        mu: float = 0.0,
        sd: float = 1.0,
    ) -> None:
        """Instantiates a GaussianWalker object at position `(x, y)` and with width and
        height = `(w, h)`.

        Args:
            x (int): the position of the Walker object in the x axis
            y (int): the position of the Walker object in the y axis
            w (int): the width of the Walker object
            h (int): the height of the Walker object
        """
        super().__init__(x, y, z, stroke, stroke_weight)
        self.mu = mu
        self.sd = sd

    def step(self) -> None:
        """Updates the Walker's position based on a step size defined by a
        Gaussian distribution of random values"""
        # The value for each axis of the step the Walker is going to take each frame
        x_step = p5.random_gaussian(self.mu, self.sd)
        y_step = p5.random_gaussian(self.mu, self.sd)

        self.x += x_step
        self.y += y_step


class MonteCarloWalker(Walker):
    """A Walker with varying step sizes calculated by the Monte Carlo method"""

    def __init__(
        self,
        x: float,
        y: float,
        z: float = 0,
        stroke: tuple[int] = (0, 0, 0, 255),
        stroke_weight: int = 1,
        min: float = -1,
        max: float = 1,
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
        """
        super().__init__(x, y, z, stroke, stroke_weight)
        self.max = max
        self.min = min

    def step(self) -> None:
        """Updates the Walker's position based on a step size defined by a
        Monte Carlo random sampling"""
        x_step = monte_carlo(min=self.min, max=self.max)
        y_step = monte_carlo(min=self.min, max=self.max)

        self.x += x_step
        self.y += y_step


class ExponentialMonteCarloWalker(Walker):
    """A Walker with varying step sizes calculated by the Monte Carlo method, with
    the probability of a number being picked as an exponential function"""

    def __init__(
        self,
        x: float,
        y: float,
        z: float = 0,
        stroke: tuple[int] = (0, 0, 0, 255),
        stroke_weight: int = 1,
        min: float = -1,
        max: float = 1,
        exp: float = 2,
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
        super().__init__(x, y, z, stroke, stroke_weight)
        self.max = max
        self.min = min
        self.exp = exp

    def step(self) -> None:
        """Updates the Walker's position based on a step size defined by a
        Monte Carlo random sampling"""
        x_step = monte_exp(min=self.min, max=self.max, exp=self.exp)
        y_step = monte_exp(min=self.min, max=self.max, exp=self.exp)

        self.x += x_step
        self.y += y_step


class NoiseWalker(Walker):
    """A Walker with varying step sizes calculated by a PerlinNoise function"""

    def __init__(
        self,
        x: float,
        y: float,
        z: float = 0,
        stroke: tuple[int] = (0, 0, 0, 255),
        stroke_weight: int = 1,
        tx: float = 0.0,
        ty: float = 0.0,
        inc: float = 0.001,
        stepsize: bool = False,
    ) -> None:
        """Instantiates a NoiseWalker object at position `(x, y)` and with width
        and height = `(w, h)`.

        Args:
            x (int): the position of the Walker object in the x axis
            y (int): the position of the Walker object in the y axis
            w (int): the width of the Walker object
            h (int): the height of the Walker object
            tx (float): the initial "time" for the x axis
            ty (float): the initial "time" for the y axis
            inc (float): the increment for each iteration
        """
        super().__init__(x, y, z, stroke, stroke_weight)
        self.tx = tx
        self.ty = ty
        self.inc = inc
        self.stepsize = stepsize

    def step(self) -> None:
        """Updates the Walker's position based on a step size defined by a
        Monte Carlo random sampling"""
        if self.stepsize:
            x_step = p5.remap(p5.noise(self.tx), (0, 1), (-1, 1))
            y_step = p5.remap(p5.noise(self.ty), (0, 1), (-1, 1))

            self.x += x_step
            self.y += y_step
        else:
            self.x = p5.remap(p5.noise(self.tx), (0, 1), (0, width))
            self.y = p5.remap(p5.noise(self.ty), (0, 1), (0, height))

        self.tx += self.inc
        self.ty += self.inc
