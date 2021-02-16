import pygame
import walker
import sys
import time


# Constants
# The window size
W_WIDTH, W_HEIGHT = (640, 480)
# The window color == white
W_COLOR = pygame.Color(255, 255, 255)


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

    # Initialize a Walker
    agent = walker.Walker(xpos, ypos, width, height)

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

        # Draw the Walker to the screen
        agent.draw(screen)

        # Make the Walker... walk
        agent.step()

        # Slow the draw loop down
        time.sleep(0.1)

        # Draw everything to the screen
        pygame.display.flip()


if __name__ == "__main__":
    main()
