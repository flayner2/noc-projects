import pygame
import walker
import sys


# Constants
# The resolution variable, used to calculate each object's size
RES = 10
# The window size
W_WIDTH, W_HEIGHT = (640, 480)
# The window color == white
W_COLOR = pygame.Color(255, 255, 255)


def main() -> None:
    # Initializing pygame's runtime
    pygame.init()

    # Initializing the screen
    screen = pygame.display.set_mode((W_WIDTH, W_HEIGHT))

    # Draw loop
    while True:
        for event in pygame.event.get():
            # Catch a QUIT event to terminate the loop and the app
            if event.type == pygame.QUIT:
                sys.exit()


if __name__ == "__main__":
    main()
