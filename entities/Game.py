from secrets import choice
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.vector import Vector

from entities.Snake import Snake, MOV, SnakeHead

class Game(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.size = (550, 550)
        Window.minimum_width, Window.minimum_height = Window.size
                
        head = SnakeHead(Vector(21,20), root=self)
        body0 = Snake(Vector(20,20), root=self)
        body1 = Snake(Vector(19,20), root=self)
        body2 = Snake(Vector(18,20), root=self)
        hail = Snake(Vector(17,20), root=self)

        body2.hail = hail
        body1.hail = body2
        body0.hail = body1
        head.hail = body0

        self.snake = head
         
        self.add_widget(self.snake)
        self.add_widget(body0)
        self.add_widget(body1)
        self.add_widget(body2)
        self.add_widget(hail)



        self.clock_snake_update = Clock.schedule_interval(self.snake.update, 1/60)
        self.clock_reload_snake = Clock.schedule_interval(self.snake.reload_snake, 1/10)


        Clock.schedule_interval(self.random_mov, 7)
        Clock.schedule_interval(self.eattemp, 2)

        

    def eattemp(self, dt):
        self.snake.eat = True

    def random_mov(self, dt):
        self.snake.mov = choice([MOV.DOWM, MOV.LEFT, MOV.RIGTH, MOV.UP])


        