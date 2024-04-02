from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QVBoxLayout
from PyQt5.QtGui import QPalette, QColor

a = QApplication([])


class Color(QWidget):
    def __init__(self, color):
        super().__init__()
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)


class window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.vertikal = QVBoxLayout()
        self.widget = QWidget()
        self.widget.setLayout(self.vertikal)
        self.rang1 = Color("grey")
        self.rang2 = Color("orange")
        self.rang3 = Color("red")
        self.vertikal.addWidget(self.rang1)
        self.vertikal.addWidget(self.rang2)
        self.vertikal.addWidget(self.rang3)
        self.setCentralWidget(self.widget)


oyna = window()
oyna.show()
a.exec()
