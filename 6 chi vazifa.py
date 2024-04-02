from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QPalette, QColor

app = QApplication([])


class Color(QWidget):
    def __init__(self, color):
        super().__init__()
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.bosh = QHBoxLayout()
        self.widget = QWidget()

        self.h1 = QHBoxLayout()
        self.w1 = QWidget()
        self.r1 = Color("red")
        self.r2 = Color("cyan")
        self.h1.addWidget(self.r1)
        self.h1.addWidget(self.r2)
        self.w1.setLayout(self.h1)
        self.bosh.addWidget(self.w1)

        self.v1 = QVBoxLayout()
        self.w2 = QWidget()
        self.r3 = Color("black")
        self.r4 = Color("green")
        self.r5 = Color("orange")
        self.v1.addWidget(self.r3)
        self.v1.addWidget(self.r4)
        self.v1.addWidget(self.r5)
        self.w2.setLayout(self.v1)
        self.bosh.addWidget(self.w2)

        self.widget.setLayout(self.bosh)
        self.setCentralWidget(self.widget)


window = Window()
window.show()
app.exec()
