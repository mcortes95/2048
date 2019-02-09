import pyxel
import math
import tile
import player
import random
class App:
    def __init__(self):
        pyxel.init(210,255,caption="2048")
        pyxel.mouse(True)
        self.pl=player.Player()
        pyxel.run(self.update,self.draw)
    
    def new_game(self):
        self.pl=player.Player()
    
    def new_high_score(self):
        self.pl.new_score.write(str(self.pl.score))

    def update(self):
        self.pl.update()
        if pyxel.btnp(pyxel.KEY_R):
            if self.pl.score_flag:
                self.new_high_score()
            self.new_game()

        if pyxel.btnp(pyxel.KEY_Q):
            if self.pl.score_flag:
                self.new_high_score()
            pyxel.quit()

    def draw(self):
        pyxel.cls(0)
        self.pl.draw()

App()

#End
