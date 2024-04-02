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
        self.boshV = QVBoxLayout()

        self.h1 = QHBoxLayout()
        self.w1 = QWidget()
        self.r1 = Color("green")
        self.r2 = Color("yellow")
        self.r3 = Color("brown")
        self.r4 = Color("cyan")
        self.h1.addWidget(self.r1)
        self.h1.addWidget(self.r2)
        self.h1.addWidget(self.r3)
        self.h1.addWidget(self.r4)
        self.w1.setLayout(self.h1)
        self.boshV.addWidget(self.w1)

        self.h2 = QHBoxLayout()
        self.w2 = QWidget()
        self.r5 = Color("red")
        self.r6 = Color("pink")
        self.h2.addWidget(self.r5)
        self.h2.addWidget(self.r6)
        self.w2.setLayout(self.h2)
        self.boshV.addWidget(self.w2)

        self.h3 = QHBoxLayout()
        self.w3 = QWidget()
        self.r7 = Color("green")
        self.r8 = Color("orange")
        self.r9 = Color("yellow")
        self.h3.addWidget(self.r7)
        self.h3.addWidget(self.r8)
        self.h3.addWidget(self.r9)
        self.w3.setLayout(self.h3)
        self.boshV.addWidget(self.w3)

        self.widget.setLayout(self.boshV)
        self.setCentralWidget(self.widget)


window = Window()
window.show()
app.exec()
