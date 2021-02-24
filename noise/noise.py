import p5

W_WIDTH, W_HEIGHT = (800, 600)


def setup() -> None:
    p5.size(W_WIDTH, W_HEIGHT)


def draw() -> None:
    xoff = 0.0

    with p5.load_pixels():
        for x in range(W_WIDTH):
            yoff = 0.0

            for y in range(W_HEIGHT):
                r = p5.remap(p5.noise(xoff, yoff), (0, 1), (0, 255))
                g = p5.remap(p5.noise(xoff * 10, yoff * 10), (0, 1), (0, 255))
                b = p5.remap(p5.noise(xoff * 5, yoff * 5), (0, 1), (0, 255))
                # pixels._set_pixel((x, y), p5.color.Color(r=r, g=g, b=b))
                pixels._set_pixel((x, y), p5.color.Color(r=r, g=0, b=0))

                # brightness = p5.remap(p5.noise(xoff, yoff), (0, 1), (0, 255))
                # pixels._set_pixel((x, y), p5.color.Color(brightness))

                yoff += 0.01

            xoff += 0.01

        pixels.load_pixels()


if __name__ == "__main__":
    p5.run()
