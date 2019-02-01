import pyxel
import math
import tile
import player
import random
class App:
    def __init__(self):
        pyxel.init(210,210)
        pyxel.mouse(True)
        self.pl=player.Player()
        pyxel.run(self.update,self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        pyxel.cls(0)
        self.pl.draw()

App()

#End
