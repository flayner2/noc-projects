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
    width, height = (5, 5)
    # Wakler color
    curr_color = COLORS["BLACK"]
    # Count the number of Walker steps
    steps = 0

    # Initialize a Walker
    # agent = walker.Walker(xpos, ypos, width, height)
    # Initalize a BottomRightSkewedWalker
    # skewed_agent = walker.BottomRightSkewedWalker(xpos, ypos, width, height)
    # Initialize a MouseFollowerWalker
    stalker_agent = walker.MouseFollowerWalker(xpos, ypos, width, height)

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

        # Change the color depending on the number of steps
        if steps % 1000 == 0:
            curr_color = (randint(0, 255), randint(0, 255), randint(0, 255))

        stalker_agent.draw(screen, curr_color)

        # Make the Walker... walk
        stalker_agent.step()

        # Draw everything to the screen
        pygame.display.flip()

        # Increase the number of steps
        steps += 1


if __name__ == "__main__":
    main()
