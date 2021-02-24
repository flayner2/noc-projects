import p5
import walker


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

# agent = walker.Walker(x, y, stroke=Colors.black)
# agent = walker.BottomRightSkewedWalker(x, y, stroke=Colors.black)
# agent = walker.MouseFollowerWalker(x, y, stroke=Colors.black)
# agent = walker.GaussianWalker(x, y, stroke=Colors.black, mu=0, sd=1)
# agent = walker.MonteCarloWalker(x, y, stroke=Colors.black, min=-1, max=1)
# agent = walker.ExponentialMonteCarloWalker(
#     x, y, stroke=Colors.black, min=-1, max=1, exp=2
# )
# agent = walker.NoiseWalker(x, y, stroke=Colors.black, tx=0, ty=1000, inc=0.001)
agent = walker.NoiseWalker(
    x, y, stroke=Colors.black, tx=0, ty=1000, inc=0.001, stepsize=True
)


# Setup function, runs once before the draw loop
def setup() -> None:
    p5.size(W_WIDTH, W_HEIGHT)
    p5.background(0)


# Draw loop
def draw() -> None:
    if agent.x >= W_WIDTH:
        agent.x = 0
    elif agent.x <= 0:
        agent.x = W_WIDTH

    if agent.y >= W_HEIGHT:
        agent.y = 0
    elif agent.y <= 0:
        agent.y = W_HEIGHT

    agent.show()
    agent.step()


if __name__ == "__main__":
    p5.run()
