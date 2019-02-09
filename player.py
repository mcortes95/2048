import pyxel
import vector
import tile
import random


class Player:
    def __init__(self):
        self.tiles=[]
        self.empty=[]
        self.tile_counter=0
        self.fill_empty()
        #self.game_testing()
        self.new_game()
        self.busy=False
        self.flag=False
        self.score=0
        self.high_scores=open("scores.txt","r")
        self.new_score=open("scores.txt","a")
        self.continue_game=True
        self.check_hs()
        self.score_flag=False
        self.tiles_to_remove=[]
        self.merging_tiles=[]
        self.update_tile_color=[]
        pyxel.load("my_resource.pyxel")
        
    def game_testing(self): 
        for x in range(3):
            self.add_tile(x+1,1)
            print(len(self.empty))
        for tile in range(3):
            if tile<2:
                self.tiles[tile].value=2
                self.tiles[tile].color=15
            else:
                self.tiles[tile].value=4
                self.tiles[tile].color=14

    def new_game(self):
        for x in range(2):
            self.temp=self.empty[random.randint(0,len(self.empty)-1)]
            self.add_tile(self.temp.x,self.temp.y)
            print(len(self.empty))
            self.empty.remove(self.temp)

    def get_score_flag(self):
        return self.score_flag

    def check_hs(self):
        self.high_score=0
        for score in  self.high_scores:
            print(type(score))
            self.high_score=max(int(score),self.high_score)

    def check_gameover(self):
        print("TODO\nDefine an end state.")


    def check_game(self):
        if len(self.tiles) is 16:
            return False
        else:
            return True

    def new_tile(self):
        print(len(self.tiles))
        if self.check_game():
            added_tile=False
            while added_tile==False:
                x=random.randint(1,4)
                y=random.randint(1,4)
                if any(tile.position.x==x and tile.position.y==y for tile in self.tiles) is False:
                    added_tile=True
            #print(added_tile)
            self.add_tile(x,y)

    def check_tile(self,x,y):
        if x>4 or y>4 or x<1 or y<1:
            return -1
        for tile in self.tiles:
            if tile.position.x == x and tile.position.y == y:
                return tile
        return 0
    
    def remove_tiles(self):
        for tile in self.tiles_to_remove:
            self.tiles.remove(tile)
        self.tiles_to_remove=[]

    def update_color(self,tiles):
        tiles.color-=1

    def merge_tiles(self,update_tile,delete_tile):
        update_tile.value*=2
        delete_tile.value*=2
        self.score+=update_tile.value
        self.tiles_to_remove.append(delete_tile)

    def move(self,x,y):
        #pyxel.load
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
        #self.merging_tiles=[]
        self.update_tile_color=[]
        for v in range(start,end,step):
            self.merging_tiles=[]
            for tile in self.tiles:
                #will manipulate tiles row by row when sliding up or down 
                if tile.position.y == v and x == 0:
                    mv=vector.vector(tile.position.x+x,tile.position.y+y)
                    tile_checked=self.check_tile(mv.x,mv.y)
                    #print(tile_checked.value)
                    if type(tile_checked) is not int:
                        if tile_checked.value==tile.value and tile_checked.slide_flag==False and tile.slide_flag==False:
                            print("merging")
                            print(tile_checked.value,tile.value)
                            tile.position=mv
                            self.merging_tiles.append([tile_checked,tile])
                            tile_checked.slide_flag=True
                            tile.slide_flag=True
                    while tile_checked == 0:
                        tile.position=vector.vector(mv.x,mv.y)    
                        mv=vector.vector(tile.position.x+x,tile.position.y+y)
                        tile_checked=self.check_tile(mv.x,mv.y)
                        if type(tile_checked) is not int:
                            if tile_checked.value==tile.value and tile_checked.slide_flag==False and tile.slide_flag==False:
                                print("merging")
                                print(tile_checked.value,tile.value)
                                tile.position=mv
                                self.merging_tiles.append([tile_checked,tile])
                                tile_checked.slide_flag=True
                                tile.slide_flag=True
                                #self.merge_tiles(tile_checked,tile)
                #will manipulate tiles column by column when sliding left or right 
                elif tile.position.x == v and y == 0:
                    mv=vector.vector(tile.position.x+x,tile.position.y+y)
                    #print(mv)
                    tile_checked=self.check_tile(mv.x,mv.y)
                    #print(tile_checked.value)
                    if type(tile_checked) is not int:
                        if tile_checked.value==tile.value and tile_checked.slide_flag==False and tile.slide_flag==False:
                            print("merging")
                            print(tile_checked.value,tile.value)
                            tile.position=mv
                            self.merging_tiles.append([tile_checked,tile])
                            tile_checked.slide_flag=True
                            tile.slide_flag=True
                    while tile_checked == 0:
                        tile.position=vector.vector(mv.x,mv.y)    
                        mv=vector.vector(tile.position.x+x,tile.position.y+y)
                        tile_checked=self.check_tile(mv.x,mv.y)
                        if type(tile_checked) is not int:
                            if tile_checked.value==tile.value and tile_checked.slide_flag==False and tile.slide_flag==False:
                                print("merging")
                                print(tile_checked.value,tile.value)
                                tile.position=mv
                                self.merging_tiles.append([tile_checked,tile])
                                tile_checked.slide_flag=True
                                tile.slide_flag=True
            for pairs in self.merging_tiles:
                print(pairs[0].id,pairs[1].id)
                self.merge_tiles(pairs[0],pairs[1])
                self.update_tile_color.append(pairs[0])

    def update(self):
        if len(self.tiles) is 16:
            self.check_gameover()
        #checks if any tile is currently moving to decide whether
        #or not to allow user to move tiles
        if any(tile.busy()==True for tile  in self.tiles):
            self.busy=True
        else:
            self.busy=False
        if self.busy==False:
            if self.flag:
                for x in self.update_tile_color:
                    self.update_color(x)
                self.remove_tiles()
                self.new_tile()
                self.flag=False
                for  tile in self.tiles:
                    tile.slide_flag=False
        #Checks to make sure no other actions are occuring before accepting user input
        if self.busy==False:
            if pyxel.btnp(pyxel.KEY_W):
                pyxel.play(0,1)
                self.move(0,-1)
                self.flag=True
            elif pyxel.btnp(pyxel.KEY_A):
                pyxel.play(0,1)
                self.move(-1,0)
                self.flag=True
            elif pyxel.btnp(pyxel.KEY_S):
                pyxel.play(0,1)
                self.move(0,1)
                self.flag=True
            elif pyxel.btnp(pyxel.KEY_D):
                pyxel.play(0,1)
                self.move(1,0)
                self.flag=True
        if self.score>=self.high_score:
            self.high_score=self.score
            self.score_flag=True

    def add_tile(self,x,y):
        self.tiles.append(tile.tile(x,y,self.tile_counter))
        self.tile_counter+=1

    def draw(self):
        for tile in self.tiles:
            tile.show()
        pyxel.rect(0,215,210,255,3)
        pyxel.rect(0,210,210,215,2)
        pyxel.text(80,225,"SCORE: "+str(self.score),15)        
        pyxel.text(80,235,"HIGH SCORE: "+str(self.high_score),15)

    def fill_empty(self):
        for x in range(1,5):
            for y in range(1,5):
                #print(x,y)
                self.empty.append(vector.vector(x,y))




