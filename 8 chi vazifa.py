from PyQt5.QtWidgets import (QApplication, QWidget, QMainWindow, QVBoxLayout,
                             QHBoxLayout, QLabel, QLineEdit, QPushButton)

app = QApplication([])


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Miles to kilometr")
        self.bosh = QVBoxLayout()
        self.widget = QWidget()
        self.text = ["Distance in miles:", "Distance in kilometr"]
        self.label = [QLabel(i) for i in self.text]
        self.len = max(i.sizeHint().width() for i in self.label)

        for i in self.label:
            i.setFixedWidth(self.len)


        self.h1 = QHBoxLayout()
        self.w1 = QWidget()
        self.i1 = QLineEdit()
        self.h1.addWidget(self.label[0])
        self.h1.addWidget(self.i1)
        self.w1.setLayout(self.h1)
        self.bosh.addWidget(self.w1)

        self.btn = QPushButton("Convert")
        self.bosh.addWidget(self.btn)

        self.h2 = QHBoxLayout()
        self.w2 = QWidget()
        self.i2 = QLineEdit()
        self.h2.addWidget(self.label[1])
        self.h2.addWidget(self.i2)
        self.w2.setLayout(self.h2)
        self.bosh.addWidget(self.w2)

        self.widget.setLayout(self.bosh)
        self.setCentralWidget(self.widget)


window = Window()
window.show()
app.exec()
