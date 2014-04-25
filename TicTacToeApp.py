from kivy.app import App
from kivy.uix.gridlayout import GridLayout


class TicTacToeApp(App):
    def build(self):
        return TicTacToeGrid


class TicTacToeGrid(GridLayout):
    pass

if __name__ == "__main__":
    TicTacToeApp().run()