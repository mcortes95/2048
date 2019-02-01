import vector
import pyxel
class tile:
    def __init__(self,x,y):
        self.value=4
        self.position=vector.vector(x,y)
        self.px_position=vector.vector(50*x-20,50*y-20)
        
    def show(self):
        pyxel.rect(self.px_position.x-20,
                self.px_position.y-20,
                self.px_position.x+20,
                self.px_position.y+20,
                1)
        pyxel.text(self.px_position.x,
                self.px_position.y,
                str(self.value),
                0)

