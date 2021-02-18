import pygame
import splatter
import sys
from random import gauss, choice


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


def generate_gaussian_pallette(
    n_colors: int = 1,
    base_mean: float = 127.5,
    base_sd: float = 1.0,
    secondary_mean: float = 1.0,
    secondary_sd: float = 0.1,
):
    # The list to hold all colors in our pallette
    colors = []

    # The color channels
    channels = {"red": 0, "green": 0, "blue": 0}

    # Pick the color to be the base of our pallette
    selected = choice(list(channels))

    # Try to generate a valid color
    while len(colors) < n_colors:
        for _ in range(n_colors):
            for key in channels.keys():
                if key == selected:
                    # The selected base channel can have any value from 0 to 255
                    # and even have a larger variation of possible values
                    channels[key] = abs(round(gauss(base_mean, base_sd)))
                else:
                    # While te secondary colors are going to be less variable
                    # and are going to have smaller values overall
                    channels[key] = abs(round(gauss(secondary_mean, secondary_sd)))
            try:
                # Create a random color
                color = pygame.Color(
                    channels["red"], channels["green"], channels["blue"]
                )
                colors.append(color)
            # If the color is not valid (e.g. over 255 in any channel), try again
            except ValueError:
                continue

    return colors


def main() -> None:
    # Initializing pygame's runtime
    pygame.init()

    # Initializing the screen
    screen = pygame.display.set_mode((W_WIDTH, W_HEIGHT))

    # The Splatter doesn't need a position or a color since those
    # are calculated by its draw() method randomly. We just need a
    # radius and a width
    radius, width = (5, 0)

    # Parameters to calculate the spread of the Splatters and the
    # range of Splatter colors
    pos_sd = 0.2

    # Initialize a collection of Splatters
    n = 100000
    splats = [splatter.Splatter(w=width, h=radius) for _ in range(n)]

    # Coloring the screen
    screen.fill(W_COLOR)

    # Generate a Gaussian distributed color pallette
    base_mean = 127.5
    base_sd = 1.0
    secondary_mean = 10.0
    secondary_sd = 205.0
    colors = generate_gaussian_pallette(
        n_colors=n,
        base_mean=base_mean,
        base_sd=base_sd,
        secondary_mean=secondary_mean,
        secondary_sd=secondary_sd,
    )

    # Draw each Splatter to the screen
    for splat, color in zip(splats, colors):
        splat.draw(screen, color=color, sd=pos_sd)

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
                    # Generating the new pallette
                    colors = generate_gaussian_pallette(
                        n_colors=n,
                        base_mean=base_mean,
                        base_sd=base_sd,
                        secondary_mean=secondary_mean,
                        secondary_sd=secondary_sd,
                    )
                    # Draw a new set of Splatters
                    for splat, color in zip(splats, colors):
                        splat.draw(screen, color=color, sd=pos_sd)

        # Draw everything to the screen
        pygame.display.flip()


if __name__ == "__main__":
    main()
