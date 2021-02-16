import ursina


class Walker(ursina.Entity):
    def __init__(self, x: float, y: float, color: ursina.Color = ursina.color.white):
        super().__init__()
        self.model = "quad"
        self.x = x
        self.y = y
        self.color = color
