import vector
import pyxel
class tile:
    def __init__(self,x,y):
        self.value=4
        self.position=vector.vector(x,y)
        self.px_position=vector.vector(50*x-20,50*y-20)
        self.velocity=vector.vector(0,0) 
    def show(self):
        self.update()
        pyxel.rect(self.px_position.x-20,
                self.px_position.y-20,
                self.px_position.x+20,
                self.px_position.y+20,
                1)
        pyxel.text(self.px_position.x,
                self.px_position.y,
                str(self.value),
                0)
    def update(self):
        #self.px_position.x=(50*self.position.x-20)
        #self.px_position.y=(50*self.position.y-20)
        if self.px_position.x<50*self.position.x-20:
            self.px_position.x+=10
        if self.px_position.x>50*self.position.x-20:
            self.px_position.x-=10
        if self.px_position.y>50*self.position.y-20:
            self.px_position.y-=10
        if self.px_position.y<50*self.position.y-20:
            self.px_position.y+=10



