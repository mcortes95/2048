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
        self.busy=False
        self.flag=False

        #if any(tile.busy()==True for tile  in self.tiles):
            #self.busy=True

    def new_tile(self):
        for tile in self.tiles:
            print(tile.position.x,tile.position.y)
        print("TODO")
        added_tile=False
        while added_tile==False:
            x=random.randint(1,4)
            y=random.randint(1,4)
            print(x,y)
            if any(tile.position.x==x and tile.position.y==y for tile in self.tiles) is False:
                added_tile=True
            print(added_tile)
        self.add_tile(x,y)
    def check_tile(self,x,y):
        if x>4 or y>4 or x<1 or y<1:
            return -1
        for tile in self.tiles:
            if tile.position.x == x and tile.position.y == y:
                return tile
        return 0

    def merge_tiles(self,update_tile,delete_tile):
        print("TODO")
        update_tile.value*=2
        self.tiles.remove(delete_tile)

    def move(self,x,y):
        if x==0:
            #move up
            if y==-1:
                start=1
                end=5
                step=1
            #move down
            elif y==1:
               start=4
               end=0
               step=-1
        
        elif y==0:
            #move left
            if x==-1:
                start=1
                end=5
                step=1
            elif x==1:
                start=4
                end=0
                step=-1
        #moves tiles in desired direction in the correct order to prevent them from colliding 
        for v in range(start,end,step):
            merging_tiles=[]
            for tile in self.tiles:
                #will manipulate tiles row by row when sliding up or down 
                 
                if tile.position.y == v and x == 0:
                    mv=vector.vector(tile.position.x+x,tile.position.y+y)
                    print(mv)
                    tile_checked=self.check_tile(mv.x,mv.y)
                    #print(tile_checked.value)
                    if type(tile_checked) is not int:
                        if tile_checked.value==tile.value:
                            print("merge")
                            print(tile_checked.position.x,tile_checked.position.y)
                            print(tile.position.x,tile.position.y)
                            merging_tiles.append([tile_checked,tile])
                    while tile_checked == 0:
                        tile.position=vector.vector(mv.x,mv.y)    
                        mv=vector.vector(tile.position.x+x,tile.position.y+y)
                        tile_checked=self.check_tile(mv.x,mv.y)
                        if type(tile_checked) is not int:
                            if tile_checked.value==tile.value:
                                merging_tiles.append([tile_checked,tile])
                                print("merge0")
                #will manipulate tiles column by column when sliding left or right 
                elif tile.position.x == v and y == 0:
                    mv=vector.vector(tile.position.x+x,tile.position.y+y)
                    print(mv)
                    tile_checked=self.check_tile(mv.x,mv.y)
                    #print(tile_checked.value)
                    if type(tile_checked) is not int:
                        if tile_checked.value==tile.value:
                            print("merge")
                            merging_tiles.append([tile_checked,tile])
                    while tile_checked == 0:
                        tile.position=vector.vector(mv.x,mv.y)    
                        mv=vector.vector(tile.position.x+x,tile.position.y+y)
                        tile_checked=self.check_tile(mv.x,mv.y)
                        if type(tile_checked) is not int:
                            if tile_checked.value==tile.value:
                                print("merge0")
                                merging_tiles.append([tile_checked,tile])
            for pairs in  merging_tiles:
                self.merge_tiles(pairs[0],pairs[1])
        #self.new_tile()
    def update(self):
        #checks if any tile is currently moving to decide whether
        #or not to allow user to move tiles
        if any(tile.busy()==True for tile  in self.tiles):
            self.busy=True
        else:
            self.busy=False
        if self.busy==False:
            if self.flag:
                self.new_tile()
                self.flag=False
        if self.busy==False:
            if pyxel.btnp(pyxel.KEY_W):
                print("U")
                self.move(0,-1)
                self.flag=True
            elif pyxel.btnp(pyxel.KEY_A):
                print("L")
                self.move(-1,0)
                self.flag=True
            elif pyxel.btnp(pyxel.KEY_S):
                print("D")
                self.move(0,1)
                self.flag=True
            elif pyxel.btnp(pyxel.KEY_D):
                print("R")
                self.move(1,0)
                self.flag=True
            #self.new_tile()
        
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




