from PyQt5 import QtWidgets, QtGui

from model import Model

from drawing import *
from .main_window_ui import Ui_MainWindow

path_to_icon = './imgs/app_icon.png'


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)

        self.model = Model(-1)
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon(path_to_icon))

        init_gl_widget(self.gl_widget, self.model)

        self.pushButtonStartDrawing.clicked.connect(self.start_drawing_fractal)

    def start_drawing_fractal(self):
        self.pushButtonStartDrawing.setDisabled(True)
        self.textEditIterNum.setDisabled(True)

        iter_num_str = self.textEditIterNum.toPlainText()
        if iter_num_str:
            self.model.iter_num = int(iter_num_str)

        self.gl_widget.update()

        self.pushButtonStartDrawing.setDisabled(False)
        self.textEditIterNum.setDisabled(False)