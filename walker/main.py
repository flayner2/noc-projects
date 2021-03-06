import pygame
import walker
import sys
from random import randint


# Constants
# The window size
W_WIDTH, W_HEIGHT = (800, 600)
# Colors
COLORS = {
    "WHITE": pygame.Color(255, 255, 255),
    "BLACK": pygame.Color(0, 0, 0),
    "RED": pygame.Color(255, 0, 0),
    "GREEN": pygame.Color(0, 255, 0),
    "BLUE": pygame.Color(0, 0, 255),
    "YELLOW": pygame.Color(255, 255, 0),
    "PURPLE": pygame.Color(127, 0, 255),
    "ORANGE": pygame.Color(204, 102, 0),
}
# Window color
W_COLOR = COLORS["WHITE"]


def main() -> None:
    # Initializing pygame's runtime
    pygame.init()

    # Initializing the screen
    screen = pygame.display.set_mode((W_WIDTH, W_HEIGHT))

    # Coloring the screen
    screen.fill(W_COLOR)

    # Walker position in (x, y)
    xpos, ypos = (W_WIDTH / 2, W_HEIGHT / 2)
    # Walker size in (width, height)
    width, height = (2, 2)
    # Wakler color
    curr_color = COLORS["BLACK"]
    # Count the number of Walker steps
    steps = 0
    # Number of Walkers to generate
    n = 20

    # Initialize a collection of Walkers
    # walkers = [walker.Walker(xpos, ypos, width, height) for _ in range(n)]
    # Initalize a collection of BottomRightSkewedWalkers
    # walkers = [
    #     walker.BottomRightSkewedWalker(xpos, ypos, width, height) for _ in range(n)
    # ]
    # Initialize a collection of MouseFollowerWalkers
    # walkers = [walker.MouseFollowerWalker(xpos, ypos, width, height) for _ in range(n)]
    # Initialize a collection of GaussianWalkers
    walkers = [
        walker.GaussianWalker(xpos, ypos, width, height, mu=0, sd=1) for _ in range(n)
    ]

    # Draw loop
    while True:
        for event in pygame.event.get():
            # Catch a QUIT event to terminate the loop and the app
            if event.type == pygame.QUIT:
                sys.exit()
            # Or exit on pressing the ESC key
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        for agent in walkers:
            # Change the color depending on the number of steps
            if steps % 1000 == 0:
                curr_color = (randint(0, 255), randint(0, 255), randint(0, 255))

            # If the Walker tries to get out of the screen, warp it to the other side
            if agent.left >= W_WIDTH:
                agent.left = 0
            elif agent.left <= 0:
                agent.left = W_WIDTH

            if agent.top >= W_HEIGHT:
                agent.top = 0
            elif agent.top <= 0:
                agent.top = W_HEIGHT

            # Draw the Walker to the screen
            agent.draw(screen, curr_color)

            # Make the Walker... walk
            agent.step()

        # Draw everything to the screen
        pygame.display.flip()

        # Increase the number of steps
        steps += 1


if __name__ == "__main__":
    main()
