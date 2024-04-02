from PyQt5.QtWidgets import (QApplication, QWidget, QMainWindow, QVBoxLayout,
                             QHBoxLayout, QLabel, QLineEdit, QPushButton)

app = QApplication([])


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sign Up Form")
        self.bosh = QVBoxLayout()
        self.widget = QWidget()

        text = ["Name:", "Email:", "Password:", "Confirm Password:", "Phone:"]
        self.label = [QLabel(i) for i in text]
        katta_uzunlik = max(yozuv.sizeHint().width() for yozuv in self.label)

        for i in self.label:
            i.setFixedWidth(katta_uzunlik)

        self.h1 = QHBoxLayout()
        self.w1 = QWidget()
        self.i1 = QLineEdit()

        self.h1.addWidget(self.label[0])
        self.h1.addWidget(self.i1)
        self.w1.setLayout(self.h1)
        self.bosh.addWidget(self.w1)

        self.h2 = QHBoxLayout()
        self.w2 = QWidget()
        self.i2 = QLineEdit()

        self.h2.addWidget(self.label[1])
        self.h2.addWidget(self.i2)
        self.w2.setLayout(self.h2)
        self.bosh.addWidget(self.w2)

        self.h3 = QHBoxLayout()
        self.w3 = QWidget()
        self.i3 = QLineEdit()

        self.h3.addWidget(self.label[2])
        self.h3.addWidget(self.i3)
        self.w3.setLayout(self.h3)
        self.bosh.addWidget(self.w3)

        self.h4 = QHBoxLayout()
        self.w4 = QWidget()
        self.i4 = QLineEdit()

        self.h4.addWidget(self.label[3])
        self.h4.addWidget(self.i4)
        self.w4.setLayout(self.h4)
        self.bosh.addWidget(self.w4)

        self.h5 = QHBoxLayout()
        self.w5 = QWidget()
        self.i5 = QLineEdit()

        self.h5.addWidget(self.label[4])
        self.h5.addWidget(self.i5)
        self.w5.setLayout(self.h5)
        self.bosh.addWidget(self.w5)

        self.btn = QPushButton("Sign Up")
        self.bosh.addWidget(self.btn)

        self.widget.setLayout(self.bosh)
        self.setCentralWidget(self.widget)


window = Window()
window.show()
app.exec()
