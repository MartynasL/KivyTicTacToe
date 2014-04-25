from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.properties import ListProperty


class TicTacToeCell(Button):
    coordinates = ListProperty([0, 0])


class TicTacToeApp(App):
    def build(self):
        return TicTacToeGrid()


class TicTacToeGrid(GridLayout):
    def __init__(self, *args, **kwargs):
        super(TicTacToeGrid, self).__init__(*args, **kwargs)
        for column in range(3):
            for row in range(3):
                cell = TicTacToeCell(coordinates=(column, row))
                cell.bind(on_release=self.cell_pressed)
                self.add_widget(cell)

    def cell_pressed(self, cell):
        pass

if __name__ == "__main__":
    TicTacToeApp().run()