import pygame
import splatter
import sys


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

    # The Splatter doesn't need a position or a color since those
    # are calculated by its draw() method randomly. We just need a
    # radius and a width
    radius, width = (5, 0)

    # Initialize a collection of Splatters
    n = 100

    splats = [splatter.Splatter(w=width, h=radius) for _ in range(n)]

    # Coloring the screen
    screen.fill(W_COLOR)

    # Draw each Splatter to the screen
    for splat in splats:
        splat.draw(screen)

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
                # If the user press ENTER
                elif event.key == pygame.K_RETURN:
                    # Clearing the screen
                    screen.fill(W_COLOR)
                    # Draw a new set of Splatters
                    for splat in splats:
                        splat.draw(screen)

        # Draw everything to the screen
        pygame.display.flip()


if __name__ == "__main__":
    main()
