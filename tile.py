import vector
import pyxel
import random
 

class tile:
    def __init__(self,x,y,i):
        self.id=i
        self.tile_value()
        self.position=vector.vector(x,y)
        self.px_position=vector.vector(50*x-20,50*y-20)
        self.velocity=vector.vector(0,0)
        self.slide_flag=False


    def tile_value(self):
        temp=random.randint(1,10)
        if temp<6:
            self.value=2
            self.color=15
        else:
            self.value=4
            self.color=14
    def show(self):
        self.update()
        pyxel.rect(self.px_position.x-20,
                self.px_position.y-20,
                self.px_position.x+20,
                self.px_position.y+20,
                self.color)
        pyxel.text(self.px_position.x,
                self.px_position.y,
                str(self.value),
                0)
        pyxel.text(self.px_position.x-18,
                self.px_position.y-18,
                str(self.id),
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

    def busy(self):
        if self.px_position.x==50*self.position.x-20 and self.px_position.y==50*self.position.y-20:
            return False
        else:
            return True



