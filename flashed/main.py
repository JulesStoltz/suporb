import kivy
kivy.require('2.1.0')

from kivy.app import App
from kivy.lang.builder import Builder
from kivy.config import Config
 
Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '300')

kv = Builder.load_file('gui.kv')


class MainApp(App):

    def build(self):
        return kv


if __name__ == '__main__':
    MainApp().run()