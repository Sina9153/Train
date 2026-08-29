import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel ,QVBoxLayout, QHBoxLayout

app = QApplication(sys.argv)

a = QMainWindow()
a.setWindowTitle("A")
a.resize(300,400)

b = QPushButton("1",a)
b.resize(40,40)
b.move(50,25)

c=QLabel("Hello",a)
c.resize(40,40)
c.move(75,90)

a.show()

app.exec()