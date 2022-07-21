from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.properties import Property

class Game(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.size = (550, 550)
        Window.minimum_width, Window.minimum_height = Window.size
                
        self.snake = Property(None)
        self.clock = Clock.schedule_interval(self.update, 1/2)

    def update(self, dt):     
        self.snake.load_snake()


        