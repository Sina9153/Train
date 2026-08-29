import sys

from PySide6.QtWidgets import QWidget, QApplication, QPushButton, QVBoxLayout, QLabel

app = QApplication(sys.argv)

widget = QWidget()
layout = QVBoxLayout()

L_1=QLabel()

def a():
    pass

b_1 = QPushButton("Click 1")
b_2 = QPushButton("Click 2")
b_3 = QPushButton("Click 3")

b_1.clicked.connect(a)

layout.addWidget(b_1)
layout.addWidget(b_2)
layout.addWidget(b_3)

widget.setLayout(layout)

widget.show()
app.exec()