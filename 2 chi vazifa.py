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
        self.widget = QWidget()
        self.boshH = QHBoxLayout()

        self.V1 = QVBoxLayout()
        self.w1 = QWidget()
        self.v11 = Color("red")
        self.V1.addWidget(self.v11)
        self.V1H1 = QHBoxLayout()
        self.v1h1 = Color("green")
        self.v1h2 = Color("yellow")
        self.V1H1.addWidget(self.v1h1)
        self.V1H1.addWidget(self.v1h2)
        self.w1.setLayout(self.V1H1)
        self.V1.addWidget(self.w1)
        self.v12 = Color("pink")
        self.V1.addWidget(self.v12)
        self.boshH.addLayout(self.V1)

        self.V2 = QVBoxLayout()
        self.w2 = QWidget()
        self.w21 = QWidget()
        self.h = QHBoxLayout()
        self.h1 = Color("green")
        self.h2 = Color("yellow")
        self.h3 = Color("brown")
        self.h4 = Color("cyan")
        self.h.addWidget(self.h1)
        self.h.addWidget(self.h2)
        self.h.addWidget(self.h3)
        self.h.addWidget(self.h4)
        self.w21.setLayout(self.h)
        self.V2.addWidget(self.w21)
        self.h5 = Color("magenta")
        self.V2.addWidget(self.h5)
        self.w2.setLayout(self.V2)
        self.boshH.addWidget(self.w2)

        self.widget.setLayout(self.boshH)
        self.setCentralWidget(self.widget)


window = Window()
window.show()
app.exec()
