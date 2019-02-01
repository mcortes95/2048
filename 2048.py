import pyxel
import math
import tile

class App:
    def __init__(self):
        pyxel.init(210,210)
        pyxel.mouse(True)
        self.tiles=[tile.tile(1,3),
            tile.tile(2,1),
            tile.tile(3,4),
            tile.tile(4,2)
            ]
        pyxel.run(self.update,self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        pyxel.cls(0)
        for tile in self.tiles:
            pyxel.rect(tile.px_position.x-20,tile.px_position.y-20,tile.px_position.x+20,tile.px_position.y+20,1)
            pyxel.text(tile.px_position.x,tile.px_position.y,str(tile.value),0)

t=tile.tile(1,2)
App()

#End
