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
        self.setupUI()

    def setupUI(self):
        self.boshH = QHBoxLayout()

        self.V1 = QVBoxLayout()
        self.w1 = QWidget()
        self.v1 = Color("grey")
        self.v2 = Color("orange")
        self.v3 = Color("blue")
        self.V1.addWidget(self.v1)
        self.V1.addWidget(self.v2)
        self.V1.addWidget(self.v3)
        self.w1.setLayout(self.V1)
        self.boshH.addWidget(self.w1)

        self.V2 = QVBoxLayout()
        self.w2 = QWidget()
        self.w2.setLayout(self.V2)
        self.wh1 = QWidget()
        self.h = QHBoxLayout()
        self.h1 = Color("green")
        self.h2 = Color("yellow")
        self.h3 = Color("brown")
        self.h4 = Color("cyan")
        self.h.addWidget(self.h1)
        self.h.addWidget(self.h2)
        self.h.addWidget(self.h3)
        self.h.addWidget(self.h4)
        self.wh1.setLayout(self.h)
        self.V2.addWidget(self.wh1)

        self.w3 = QWidget()
        self.h_2 = QHBoxLayout()
        self.h5 = Color("magenta")
        self.h6 = Color("pink")
        self.h_2.addWidget(self.h5)
        self.h_2.addWidget(self.h6)
        self.w3.setLayout(self.h_2)
        self.V2.addWidget(self.w3)

        self.w4 = QWidget()
        self.h_3 = QHBoxLayout()
        self.h7 = Color("green")
        self.h8 = Color("orange")
        self.h9 = Color("yellow")
        self.h_3.addWidget(self.h7)
        self.h_3.addWidget(self.h8)
        self.h_3.addWidget(self.h9)
        self.w4.setLayout(self.h_3)
        self.V2.addWidget(self.w4)
        self.boshH.addWidget(self.w2)

        self.widget.setLayout(self.boshH)
        self.setCentralWidget(self.widget)


window = Window()
window.show()
app.exec()
