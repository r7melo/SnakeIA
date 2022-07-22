from enum import Enum
from secrets import choice
from kivy.uix.widget import Widget
from kivy.vector import Vector

class MOV(Enum):
    STOP  = lambda:Vector( 0, 0)
    RIGTH = lambda:Vector( 1, 0)
    LEFT  = lambda:Vector(-1, 0)
    UP    = lambda:Vector( 0, 1)
    DOWM  = lambda:Vector( 0,-1)



class Snake(Widget):
    def __init__(self, current_position=Vector(25,25), **kwargs):
        super().__init__(**kwargs)
        self.clock = None
        self.current_position:Vector = current_position
        self.eat:bool = False
        self.hail:Snake = None
        self.mov:MOV = choice([MOV.DOWM, MOV.LEFT, MOV.RIGTH, MOV.UP])

    def get_position_absolute(self, pos) -> Vector:
        return Vector(pos) + self.current_position * 10
    
    def update(self):
        self.pos = self.get_position_absolute(self.parent.pos)
        if not self.hail is None: self.hail.update()
    
    def is_wall_collision(self, current_position:Vector) -> bool:
        x, y = current_position.x, current_position.y
        if x >= 50 or y >= 50 or x < 0 or y < 0:
            return True
        return False

    def reload_snake(self, dt=None, mov:Vector=None) -> None:
        self.mov_head()
        self.eat_fruit(self.eat)
        
    def mov_head(self) -> None:
        current_position = Vector(self.current_position)
        new_currente_position = self.current_position + self.mov()
        if not self.hail is None: 
            self.hail.mov_hail(current_position)

        if not self.is_wall_collision(new_currente_position):
            self.current_position = new_currente_position
        else:
            self.clock.cancel()

    def mov_hail(self, current_position) -> None:
        if not self.hail is None: 
            self.hail.mov_hail(self.current_position)
        self.current_position = current_position

    def eat_fruit(self, eat:bool) -> None:
        if not self.hail is None:
            self.hail.eat_fruit(eat)

        else:
            if eat:
                self.hail = Snake(Vector(self.current_position))
                self.parent.add_widget(self.hail)
        
        self.eat = False


class SnakeHead(Snake):
    def __init__(self, current_position=Vector(25, 25), **kwargs):
        super().__init__(current_position, **kwargs)
        

        
        







        

