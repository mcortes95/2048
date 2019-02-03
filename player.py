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

    #def adjacent_tile(self,cur_tile,direction):
        #if direction is 0:
    #def look_horizontal(self):
        #hor.position.x== 
    def check_tile(self,x,y):
        if x>4 or y>4 or x<1 or y<1:
            return -1
        for tile in self.tiles:
            if tile.position.x == x and tile.position.y == y:
                return tile.value
        return 0

    def move(self,x,y):
        for tile in self.tiles:
            mv=vector.vector(tile.position.x+x,tile.position.y+y)
            print(mv)
            tile_value=self.check_tile(mv.x,mv.y)
            print(tile_value)
            while tile_value == 0:
                tile.position=vector.vector(mv.x,mv.y)    
                
                mv=vector.vector(tile.position.x+x,tile.position.y+y)
                tile_value=self.check_tile(mv.x,mv.y)
                
           

    
    def update(self):
        if pyxel.btnp(pyxel.KEY_W):
            print("U")
            self.move(0,-1)
        elif pyxel.btnp(pyxel.KEY_A):
            print("L")
            self.move(-1,0)
        elif pyxel.btnp(pyxel.KEY_S):
            print("D")
            self.move(0,1)
        elif pyxel.btnp(pyxel.KEY_D):
            print("R")
            self.move(1,0)
        
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




