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

        self.snakes:list[Snake] = []

        for i in range(100):
            snake = SnakeHead(Vector(20,25))
            snake.clock = Clock.schedule_interval(snake.reload_snake, 1/10)
            self.add_widget(snake)
            self.snakes.append(snake)
            
            for x in range(10):
                snake.eat = True
                snake.reload_snake()
                
        self.clock_snake_update = Clock.schedule_interval(self.update, 1/60)

    def update(self, dt) -> None:
        for snake in self.snakes:
            snake.update()
            if self.is_snake_collision(snake, snake.hail): 
                snake.clock.cancel()
            
            #random mov
            snake.mov = choice([MOV.DOWM, MOV.LEFT, MOV.RIGTH, MOV.UP]) 
        
    def is_snake_collision(self, head:Snake, hail:Snake) -> bool:
        if not hail is None:
            if head.current_position == hail.current_position:
                return True 
            else:
                self.is_snake_collision(head, hail.hail)   
        else:
            return False


        