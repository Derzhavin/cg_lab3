# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 600)
        MainWindow.setMinimumSize(QtCore.QSize(600, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gl_widget = QtWidgets.QOpenGLWidget(self.centralwidget)
        self.gl_widget.setGeometry(QtCore.QRect(10, 50, 580, 540))
        self.gl_widget.setStyleSheet("color: rgb(152, 152, 152);")
        self.gl_widget.setObjectName("gl_widget")
        self.textEditIterNum = QtWidgets.QTextEdit(self.centralwidget)
        self.textEditIterNum.setGeometry(QtCore.QRect(120, 10, 60, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEditIterNum.sizePolicy().hasHeightForWidth())
        self.textEditIterNum.setSizePolicy(sizePolicy)
        self.textEditIterNum.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.textEditIterNum.setStyleSheet("font: 10pt \"Verdana\";")
        self.textEditIterNum.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEditIterNum.setObjectName("textEditIterNum")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 90, 30))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButtonStartDrawing = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonStartDrawing.setGeometry(QtCore.QRect(190, 10, 70, 30))
        self.pushButtonStartDrawing.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonStartDrawing.setObjectName("pushButtonStartDrawing")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Лаборотарная работа №3: дракон Леви"))
        self.label.setText(_translate("MainWindow", "Кол-во итераций:"))
        self.pushButtonStartDrawing.setText(_translate("MainWindow", "Построить"))
