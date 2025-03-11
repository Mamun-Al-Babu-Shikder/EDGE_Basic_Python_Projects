import sys

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QGridLayout


class Calculator(QWidget):
    def __init__(self):
        super().__init__()

        self.display = None
        self.setWindowTitle("Calculator")
        self.setFixedSize(300, 400)  # Disable window resizing

        self.create_ui()

    def create_ui(self):
        layout = QVBoxLayout()

        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setStyleSheet("font-size: 20px; padding: 10px;")
        layout.addWidget(self.display)

        grid_layout = QGridLayout()
        buttons = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
            ('0', 3, 0), ('C', 3, 1), ('=', 3, 2), ('+', 3, 3),
        ]

        for btn_text, row, col in buttons:
            button = QPushButton(btn_text)
            button.setStyleSheet("font-size: 18px; padding: 15px;")
            button.clicked.connect(lambda checked, text=btn_text: self.on_button_click(text))
            grid_layout.addWidget(button, row, col)

        layout.addLayout(grid_layout)
        self.setLayout(layout)

    def on_button_click(self, text):
        if text == "C":
            self.display.clear()
        elif text == "=":
            try:
                result = eval(self.display.text())
                self.display.setText(str(result))
            except Exception:
                self.display.setText("Error")
        else:
            self.display.setText(self.display.text() + text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec_())
