import sys

from PyQt5.QtWidgets import QApplication

from tic_tac_toe.game_window import TicTacToeWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TicTacToeWindow()
    window.show()
    app.exec_()
