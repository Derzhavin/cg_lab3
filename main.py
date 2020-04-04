import sys

from PyQt5 import QtWidgets
from view import MainWindow

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()