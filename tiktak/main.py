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

    def checkBoard(self):
        # Get board values
        tl = self.root.ids.tl.text
        tm = self.root.ids.tm.text
        tr = self.root.ids.tr.text
        ml = self.root.ids.ml.text
        mm = self.root.ids.mm.text
        mr = self.root.ids.mr.text
        bl = self.root.ids.bl.text
        bm = self.root.ids.bm.text
        br = self.root.ids.br.text

        # Check for win condition
            # All top row match
        if tl != '' and tl == tm and tl == tr:
            return self.gameWon(tl)
            # All middle row match
        if ml != '' and ml == mm and ml == mr:
            return self.gameWon(ml)
            # All bottom row match
        if bl != '' and bl == bm and bl == br:
            return self.gameWon(bl)
            # All left column match
        if tl != '' and tl == ml and tl == bl:
            return self.gameWon(tl)
            # All middle column match
        if tm != '' and tm == mm and tm == bm:
            return self.gameWon(tm)
            # All right column match
        if tr != '' and tr == mr and tr == br:
            return self.gameWon(tr)
            # All backslash diagonal match
        if tl != '' and tl == mm and tl == br:
            return self.gameWon(tl)
            # All forward slash diagonal match
        if tr != '' and tr == mm and tr == bl:
            return self.gameWon(tr)
        
        # Check if any spaces available
        if tl=='' or tm=='' or tr=='' or ml=='' or mm=='' or mr=='' or bl=='' or bm=='' or br=='':
            return self.nextTurn()
        # Game is tied
        return self.gameTie()

    def gameWon(self, winner): #TODO: Remove winner and take from turn instead
        self.root.ids.instruct.text = 'Player ' + winner + ' has won.'

        # Disable all buttons
        self.root.ids.tl.disabled = True
        self.root.ids.tm.disabled = True
        self.root.ids.tr.disabled = True
        self.root.ids.ml.disabled = True
        self.root.ids.mm.disabled = True
        self.root.ids.mr.disabled = True
        self.root.ids.bl.disabled = True
        self.root.ids.bm.disabled = True
        self.root.ids.br.disabled = True

        self.enablePlayAgain()
        

    def gameTie(self):
        self.root.ids.instruct.text = 'The game has ended in a tie.'
        self.enablePlayAgain()

    def nextTurn(self):
        self.turn = 'X' if self.turn == 'O' else 'O'
        self.root.ids.instruct.text = 'Player ' + self.turn + ', select a box.'

    def enablePlayAgain(self):
        # Enable play again button and show
        self.root.ids.playAgain.text = 'Play Again'
        self.root.ids.playAgain.size_hint = 0.5, 0.3
        self.root.ids.playAgain.disabled = False

    def reset(self):
        # Disable play again button and hide
        self.root.ids.playAgain.text = ''
        self.root.ids.playAgain.size_hint = (0.01, 0.01)
        self.root.ids.playAgain.disabled = True

        # Empty and enable all boxes
        self.root.ids.tl.text = ''
        self.root.ids.tl.disabled = False
        self.root.ids.tm.text = ''
        self.root.ids.tm.disabled = False
        self.root.ids.tr.text = ''
        self.root.ids.tr.disabled = False
        self.root.ids.ml.text = ''
        self.root.ids.ml.disabled = False
        self.root.ids.mm.text = ''
        self.root.ids.mm.disabled = False
        self.root.ids.mr.text = ''
        self.root.ids.mr.disabled = False
        self.root.ids.bl.text = ''
        self.root.ids.bl.disabled = False
        self.root.ids.bm.text = ''
        self.root.ids.bm.disabled = False
        self.root.ids.br.text = ''
        self.root.ids.br.disabled = False

        # Start game with player that did not play last in previous game
        self.nextTurn()
        



if __name__ == '__main__':
    MainApp().run()