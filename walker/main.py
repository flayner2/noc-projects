import p5
from p5.core.attribs import no_fill
import walker
import sys
from random import randint


# Common colors
class Colors:
    white = (255, 255, 255, 255)
    black = (0, 0, 0, 255)
    gray = (222, 222, 222, 255)
    red = (255, 0, 0, 255)
    green = (0, 255, 0, 255)
    blue = (0, 0, 255, 255)


# The window size
W_WIDTH, W_HEIGHT = (800, 600)

# Objects will have to be defined globally
x, y = W_WIDTH / 2, W_HEIGHT / 2
agent = walker.Walker(x, y, stroke=Colors.black)


# Setup function, runs once before the draw loop
def setup() -> None:
    p5.size(W_WIDTH, W_HEIGHT)
    p5.background(0)


# Draw loop
def draw() -> None:
    agent.show()
    agent.step()


if __name__ == "__main__":
    p5.run()
