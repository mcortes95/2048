import vector

class tile:
    def __init__(self,x,y):
        self.value=4
        self.position=vector.vector(x,y)
        self.px_position=vector.vector(50*x-20,50*y-20)
        


