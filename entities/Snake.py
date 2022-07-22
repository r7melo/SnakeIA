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
    def __init__(self, current_position=Vector(25,25), root:Widget=None, **kwargs):
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
    
    def wall_collision(self, current_position:Vector):
        x, y = current_position.x, current_position.y
        if x >= 50 or y >= 50 or x < 0 or y < 0:
            print("GAME OVER")
            self.root.clock_reload_snake.cancel()

    def reload_snake(self, dt=None, mov:Vector=None):
        self.mov_head()
        self.eat_fruit(self.eat)
        
        
            
    def mov_head(self):
        current_position = Vector(self.current_position)
        new_current_position = self.current_position + self.mov()

        self.wall_collision(new_current_position)

        self.current_position = new_current_position

        if not self.hail is None: 
            self.hail.mov_hail(current_position)

    def mov_hail(self, current_position):
        if not self.hail is None: 
            self.hail.mov_hail(self.current_position)
        self.current_position = current_position

    def eat_fruit(self, eat:bool):
        if not self.hail is None:
            self.hail.eat_fruit(eat)

        else:
            if eat:
                self.hail = Snake(Vector(self.current_position), root=self.root)
                self.root.add_widget(self.hail)
        
        self.eat = False


class SnakeHead(Snake):
    pass 
        

        
        







        

