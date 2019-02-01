import pyxel
import math

class App:
    def __init__(self):
        pyxel.init(250,250)
        pyxel.mouse(True)

        pyxel.run(self.update,self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        pyxel.cls(0)

App()

#End
