import pyxel
import vector
import tile
import random

class Player:
    def __init__(self):
        self.tiles=[]
        self.empty=[]
        self.fill_empty()
        self.temp=self.empty[random.randint(0,len(self.empty)-1)]
        self.add_tile(self.temp.x,self.temp.y)
        print(len(self.empty))
        self.empty.remove(self.temp)
        self.temp=self.empty[random.randint(0,len(self.empty)-1)]
        self.add_tile(self.temp.x,self.temp.y)
        self.empty.remove(self.temp)
        print(len(self.empty))


    def add_tile(self,x,y):
        self.tiles.append(tile.tile(x,y))

    def draw(self):
        for tile in self.tiles:
            tile.show()

    def fill_empty(self):
        for x in range(1,5):
            for y in range(1,5):
                #print(x,y)
                self.empty.append(vector.vector(x,y))




