import p5
import splatter


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


def generate_gaussian_pallette(
    base_mean: float = 127.5,
    base_sd: float = 1.0,
    secondary_mean: float = 63.75,
    secondary_sd: float = 1.0,
) -> tuple[int]:
    # The color to generate
    colors = [0, 0, 0, 255]

    # Pick the base color of our pallette
    selected = abs(round(p5.random_uniform(low=0, high=3)))

    # Create a random color based on our pallette
    colors[selected] = abs(round(p5.random_gaussian(base_mean, base_sd)))

    for index in range(len(colors)):
        if index != selected and index != 3:
            colors[index] = round(p5.random_gaussian(secondary_mean, secondary_sd))

    return tuple(colors)


# Color generation parameters
base_mean = 127.5
base_sd = 10.0
secondary_mean = 100.0
secondary_sd = 50.0

# Initialize a collection of Splatters
splats = []
n = 1000

for i in range(n):
    # Pick a radius for each splat
    radius = p5.random_uniform(5, 15)

    # Generate a new gaussian color for each splatter
    color = generate_gaussian_pallette(
        base_mean=base_mean,
        base_sd=base_sd,
        secondary_mean=secondary_mean,
        secondary_sd=secondary_sd,
    )

    splats.append(splatter.Splatter(radius=radius, fill=color))


def setup() -> None:
    p5.size(W_WIDTH, W_HEIGHT)
    p5.background(255)


def draw() -> None:
    # Splatter position distribution parameters
    half_w, half_h = W_WIDTH / 2, W_HEIGHT / 2
    pos_sd = 70

    for splat in splats:
        # Then draw it
        splat.show(mean_x=half_w, mean_y=half_h, sd=pos_sd)

    p5.no_loop()


if __name__ == "__main__":
    p5.run()
