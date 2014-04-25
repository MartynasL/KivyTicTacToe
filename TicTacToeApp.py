from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.properties import ListProperty


class TicTacToeCell(Button):
    coordinates = ListProperty([0, 0])


class TicTacToeApp(App):
    def build(self):
        return TicTacToeGrid()


class TicTacToeGrid(GridLayout):
    pressed_cells = ListProperty([0, 0, 0,
                                 0, 0, 0,
                                 0, 0, 0])

    def __init__(self, *args, **kwargs):
        super(TicTacToeGrid, self).__init__(*args, **kwargs)
        for column in range(3):
            for row in range(3):
                cell = TicTacToeCell(coordinates=(column, row))
                cell.bind(on_release=self.cell_pressed)
                self.add_widget(cell)

    def cell_pressed(self, cell):
        row, column = cell.coordinates
        list_index = 3 * row + column
        already_pressed = self.pressed_cells[list_index]

        if not already_pressed:
            self.pressed_cells[list_index] = 1
            cell.text = '[color=0000ff]X[/color]'

    def on_pressed_cells(self, instance, new_value):
        pressed_cells = new_value

        sums = [sum(pressed_cells[0:3]),  # Rows
                sum(pressed_cells[3:6]),
                sum(pressed_cells[6:9]),
                sum(pressed_cells[0::3]),  # Columns
                sum(pressed_cells[1::3]),
                sum(pressed_cells[2::3]),
                sum(pressed_cells[::4]),  # Diagonals
                sum(pressed_cells[2:-2:2])]

        win = None
        if 3 in sums:
            win = 'You win'
        elif -3 in sums:
            win = 'You lose'
        elif 0 not in pressed_cells:
            win = 'It''s a draw'

        if win:
            popup = Popup(title='End of the game',
                          content=Label(text=win),
                          size_hint=(0.5, 0.75))
            popup.bind(on_dismiss=self.reset)
            popup.open()

    def reset(self):
        self.pressed_cells = [0, 0, 0,
                              0, 0, 0,
                              0, 0, 0]

        for cell in self.children:
            cell.text = ''


if __name__ == "__main__":
    TicTacToeApp().run()