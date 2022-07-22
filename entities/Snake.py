from enum import Enum
from kivy.uix.widget import Widget
from kivy.vector import Vector

class MOV(Enum):
    STOP  = lambda:Vector( 0, 0)
    RIGTH = lambda:Vector( 1, 0)
    LEFT  = lambda:Vector(-1, 0)
    UP    = lambda:Vector( 0, 1)
    DOWM  = lambda:Vector( 0,-1)


class Snake(Widget):
    def __init__(self, current_position=Vector(25,25), root=None, **kwargs):
        super().__init__(**kwargs)
        self.root = root
        self.current_position:Vector = current_position
        self.pos = self.get_position_absolute()
        self.eat:bool = False
        self.hail:Snake = None
        self.mov:MOV = MOV.RIGTH

    def get_position_absolute(self):
        return Vector(self.root.pos) + self.current_position * 10
    
    def update(self, dt=None):
        self.pos = self.get_position_absolute()
        if not self.hail is None: self.hail.update()

    def reload_snake(self, dt=None, mov:Vector=None):
        self.mov_head()
            
    def mov_head(self):
        current_position = Vector(self.current_position)
        self.current_position += self.mov()
        if not self.hail is None: 
            self.hail.mov_hail(current_position)

    def mov_hail(self, current_position):
        if not self.hail is None: 
            self.hail.mov_hail(self.current_position)
        self.current_position = current_position

        
        

        
        







        

