from enum import Enum
from kivy.uix.widget import Widget
from kivy.vector import Vector
from kivy.graphics import Rectangle

class MOV(Enum):
    STOP  = lambda:Vector( 0, 0)
    RIGTH = lambda:Vector( 1, 0)
    LEFT  = lambda:Vector(-1, 0)
    UP    = lambda:Vector( 0, 1)
    DOWM  = lambda:Vector( 0,-1)


class BodySnake(Widget):
    def __init__(self, current_body=Vector(25,25), **kwargs):
        super().__init__(**kwargs)

        self.hail = None
        self.current_body = current_body

    def increase_body(self):
        self.hail = BodySnake(self.current_body)
        self.add_widget(self.hail)

class Snake(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.hail = None
        self.head_pos = Vector(25,25)
        self.mov = MOV.RIGTH

        self.

    def load_snake(self):
        self.head_pos += self.mov()

        if self.head_pos.x >= 50 or self.head_pos.y >= 50 or self.head_pos.x < 0 or self.head_pos.y < 0:
            print("GAME OVER")
            self.color_background = (.1,.9,.1,.1)
            self.parent.clock.cancel()
        else:
            self.pos = Vector(self.parent.pos) + self.head_pos * 10
            



        

