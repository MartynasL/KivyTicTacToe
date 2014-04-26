from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.properties import ListProperty, NumericProperty


class TicTacToeCell(Button):
    coordinates = ListProperty([0, 0])


class TicTacToeApp(App):
    def build(self):
        return TicTacToeGrid()


class TicTacToeGrid(GridLayout):
    pressed_cells = ListProperty([0, 0, 0,
                                  0, 0, 0,
                                  0, 0, 0])
    active_player = NumericProperty(1)
    best_cpu_move = None

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
            cell.text = 'X'
            cell.background_color = (1, 0, 1, 0)
            self.cpu_move(self.pressed_cells)
            self.pressed_cells[self.best_cpu_move] = -1
            self.children[self.best_cpu_move].text = 'O'
            self.children[self.best_cpu_move].background_color = (0, 1, 1, 0)


    def win(self, board):
        sums = [sum(board[0:3]),  # Rows
                sum(board[3:6]),
                sum(board[6:9]),
                sum(board[0::3]),  # Columns
                sum(board[1::3]),
                sum(board[2::3]),
                sum(board[::4]),  # Diagonals
                sum(board[2:-2:2])]

        if 3 in sums:
            return 10
        elif -3 in sums:
            return -10
        elif 0 not in board:
            return 0

    def on_pressed_cells(self, instance, new_value):
        pressed_cells = new_value

        if self.win(pressed_cells) == 10:
            popup = Popup(title='End of the game',
                          content=Label(text='You win'),
                          size_hint=(0.5, 0.75))
            popup.bind(on_dismiss=self.reset)
            popup.open()

    def reset(self, *args):
        self.pressed_cells = [0, 0, 0,
                              0, 0, 0,
                              0, 0, 0]

        for cell in self.children:
            cell.text = ''
            cell.background_color = (1, 1, 1, 1)

    def cpu_move(self, board):
        if 0 not in board:
            return self.win(board)
        scores = []
        moves = []

        for cell in board:
            if cell == 0:
                new_board = board
                list_index = board.index(cell)
                new_board[list_index] = self.active_player
                scores.append(self.cpu_move(new_board))
                moves.append(list_index)

        if self.active_player == -1:
            max_score_index = scores.index(max(scores))
            self.best_cpu_move = moves[max_score_index]
            return scores[max_score_index]
        else:
            min_score_index = scores.index(min(scores))
            self.best_cpu_move = [min_score_index]
            return scores[min_score_index]


if __name__ == "__main__":
    TicTacToeApp().run()