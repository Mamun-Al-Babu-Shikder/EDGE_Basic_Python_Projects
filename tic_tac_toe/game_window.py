from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QVBoxLayout, QLabel, QMessageBox


class TicTacToeWindow(QWidget):
    player_x = "X"
    player_o = "O"

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("TicTacToe")

        self.current_player = self.player_x
        self.current_player_label = QLabel("Turn for player: " + self.current_player)
        self.buttons = [[QPushButton(" ") for _ in range(3)] for _ in range(3)]

        self.gird_layout = QGridLayout()
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].setFixedSize(100, 100)
                self.buttons[i][j].clicked.connect(lambda _, row=i, col=j: self.make_move(row, col))
                self.gird_layout.addWidget(self.buttons[i][j], i, j)

        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.current_player_label)
        self.main_layout.addLayout(self.gird_layout)
        self.setLayout(self.main_layout)

    def make_move(self, row, col):
        button = self.buttons[row][col]
        if button.text().strip() == "":
            button.setText(self.current_player)
            if self.is_current_player_win():
                QMessageBox.information(self, "Game Over", "Player '" + self.current_player + "' wins!")
                self.reset_board()
            elif self.is_draw():
                QMessageBox.warning(self, "Game Over", "Match is Draw!")
                self.reset_board()
            else:
                self.toggle_player()

    def is_current_player_win(self):
        board = [[self.buttons[i][j].text().strip() for j in range(3)] for i in range(3)]

        for row in board:
            if row[0] == row[1] == row[2] == self.current_player:
                return True

        for j in range(3):
            if board[0][j] == board[1][j] == board[2][j] == self.current_player:
                return True

        if board[0][0] == board[1][1] == board[2][2] == self.current_player:
            return True

        if board[0][2] == board[1][1] == board[2][0] == self.current_player:
            return True

    def is_draw(self):
        return all(self.buttons[i][j].text().strip() != "" for i in range(3) for j in range(3))

    def toggle_player(self):
        if self.current_player == self.player_x:
            self.current_player = self.player_o
        else:
            self.current_player = self.player_x
        self.current_player_label.setText("Turn for player: " + self.current_player)

    def reset_board(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].setText(" ")
        self.toggle_player()
