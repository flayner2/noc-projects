from random import uniform


def monte_carlo(min: float = -1, max: float = 1) -> float:
    """Implements a rough Monte Carlo method to generate a varying distribution of
    random numbers.

    Args:
        min (float, optional): the minimum value for the random number. Defaults to -1.
        max (float, optional): the maximum value for the random number. Defaults to 1.

    Returns:
        float: the random value generate by a "Monte Carlo" distribution.
    """

    while True:
        r1 = uniform(min, max)
        r2 = uniform(min, max)

        if r2 < r1:
            return r1


def monte_exp(min: float = -1, max: float = 1, exp: float = 1) -> float:
    """Implements a rough Monte Carlo method to generate a varying distribution of
    random numbers.

    Args:
        min (float, optional): the minimum value for the random number. Defaults to -1.
        max (float, optional): the maximum value for the random number. Defaults to 1.
        exp (float, optional): the exponent to calculate the probability of a value
        being picked.

    Returns:
        float: the random value generate by a "Monte Carlo" distribution.
    """

    while True:
        r1 = uniform(min, max)
        r2 = uniform(min, max)
        p = r1 ** exp

        if r2 < p:
            return r1
