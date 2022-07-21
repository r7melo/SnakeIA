from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.properties import Property

from entities.Snake import Snake

class Game(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.size = (550, 550)
        Window.minimum_width, Window.minimum_height = Window.size
                
        self.snake = Snake()
        self.add_widget(self.snake)

        self.clock = Clock.schedule_interval(self.snake.reload_snake, 1/2)

        Clock.schedule_interval(self.snake.update, 1/60)
        Clock.schedule_interval(self.eattemp, 2)

    def eattemp(self, dt):
        self.snake.eat = True


        