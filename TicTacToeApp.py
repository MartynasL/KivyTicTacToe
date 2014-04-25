from kivy.app import App
from kivy.uix.gridlayout import GridLayout


class TicTacToeApp(App):
    def build(self):
        return TicTacToeGrid


class TicTacToeGrid(GridLayout):
    def __init__(self, *args, **kwargs):
        super(TicTacToeGrid, self).__init__(*args, **kwargs)


if __name__ == "__main__":
    TicTacToeApp().run()