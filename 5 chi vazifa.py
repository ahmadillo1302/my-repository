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
        self.bosh = QVBoxLayout()

        self.h1 = QHBoxLayout()
        self.w1 = QWidget()
        self.r1 = Color("red")
        self.r2 = Color("cyan")
        self.r3 = Color("yellow")
        self.r4 = Color("pink")
        self.h1.addWidget(self.r1)
        self.h1.addWidget(self.r2)
        self.h1.addWidget(self.r3)
        self.h1.addWidget(self.r4)
        self.w1.setLayout(self.h1)
        self.w1.setAutoFillBackground(True)
        p1 = self.w1.palette()
        p1.setColor(self.w1.backgroundRole(), QColor("green"))
        self.w1.setPalette(p1)
        self.bosh.addWidget(self.w1)

        self.r5 = Color("magenta")
        self.bosh.addWidget(self.r5)

        self.h2 = QHBoxLayout()
        self.w2 = QWidget()
        self.r6 = Color("grey")
        self.r7 = Color("yellow")
        self.h2.addWidget(self.r6)
        self.h2.addWidget(self.r7)
        self.w2.setLayout(self.h2)
        self.bosh.addWidget(self.w2)

        self.widget.setLayout(self.bosh)
        self.setCentralWidget(self.widget)


window = Window()
window.show()
app.exec()
