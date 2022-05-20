import kivy
kivy.require('2.1.0')

from kivy.app import App
from kivy.lang.builder import Builder
from kivy.app import StringProperty

kv = Builder.load_file('tik.kv')


class MainApp(App):
    turn = StringProperty()

    def build(self):
        self.turn = 'X'
        return kv

    def toggleTurn(self):
        match self.turn:
            case 'X':
                self.turn = 'O'
                return "X"
            case 'O':
                self.turn = 'X'
                return 'O'
            case _:
                return ''

if __name__ == '__main__':
    MainApp().run()