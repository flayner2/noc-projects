import ursina
import walker

app = ursina.Ursina()

app.win.setClearColorActive(False)

agent = walker.Walker(0, 0)

app.run()
