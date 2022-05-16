import kivy
kivy.require('2.1.0')

from kivy.app import App
from kivy.lang.builder import Builder

kv = Builder.load_file('tik.kv')


class MainApp(App):
    
    def build(self):
        return kv


if __name__ == '__main__':
    MainApp().run()