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
    def __init__(self, head_pos=Vector(0,25), **kwargs):
        super().__init__(**kwargs)
        
        self.position = self.pos
        self.eat = False
        self.hail = None
        self.head_pos = head_pos
        self.mov = MOV.RIGTH
    
    def update(self, dt=None):
        self.pos = self.position
        if self.hail is not None: self.hail.update()

    def reload_snake(self, dt=None):
        self.head_pos += self.mov()

        if self.head_pos.x >= 50 or self.head_pos.y >= 50 or self.head_pos.x < 0 or self.head_pos.y < 0:
            print("GAME OVER")
            self.color_background = (.1,.9,.1,.1)
            self.parent.clock.cancel()
        else:
            self.position = Vector(self.parent.pos) + self.head_pos * 10

        if self.hail is None:
            if self.eat:
                self.hail = Snake(self.head_pos - self.mov())
                self.parent.add_widget(self.hail)
                self.eat = False
        else:
            self.hail.reload_snake()
            self.hail.mov = self.mov

            if self.eat:
                self.hail.eat = True
                self.eat = False
            



        

