from kivy.app import App
from kivy.lang import Builder
from entities import *

class MainApp(App):
    def build(self):
        return Builder.load_file("MainStyle.kv")
    

if __name__=="__main__":
    MainApp().run()