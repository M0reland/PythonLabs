# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UiMainWin.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(590, 544)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.line_auth = QtWidgets.QLineEdit(self.centralwidget)
        self.line_auth.setMinimumSize(QtCore.QSize(200, 30))
        self.line_auth.setObjectName("line_auth")
        self.verticalLayout_2.addWidget(self.line_auth)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.button_findauthor = QtWidgets.QPushButton(self.centralwidget)
        self.button_findauthor.setMinimumSize(QtCore.QSize(120, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button_findauthor.setFont(font)
        self.button_findauthor.setObjectName("button_findauthor")
        self.horizontalLayout.addWidget(self.button_findauthor)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setMinimumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.line_book = QtWidgets.QLineEdit(self.centralwidget)
        self.line_book.setMinimumSize(QtCore.QSize(200, 30))
        self.line_book.setObjectName("line_book")
        self.verticalLayout.addWidget(self.line_book)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.button_findbook = QtWidgets.QPushButton(self.centralwidget)
        self.button_findbook.setMinimumSize(QtCore.QSize(120, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button_findbook.setFont(font)
        self.button_findbook.setObjectName("button_findbook")
        self.horizontalLayout_2.addWidget(self.button_findbook)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.button_addbook = QtWidgets.QPushButton(self.centralwidget)
        self.button_addbook.setMinimumSize(QtCore.QSize(400, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.button_addbook.setFont(font)
        self.button_addbook.setObjectName("button_addbook")
        self.verticalLayout_4.addWidget(self.button_addbook)
        self.button_addauthor = QtWidgets.QPushButton(self.centralwidget)
        self.button_addauthor.setMinimumSize(QtCore.QSize(400, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.button_addauthor.setFont(font)
        self.button_addauthor.setObjectName("button_addauthor")
        self.verticalLayout_4.addWidget(self.button_addauthor)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "ID автора"))
        self.button_findauthor.setText(_translate("MainWindow", "Найти автора"))
        self.label_2.setText(_translate("MainWindow", "Название книги"))
        self.button_findbook.setText(_translate("MainWindow", "Найти книгу"))
        self.button_addbook.setText(_translate("MainWindow", "Добавить книгу"))
        self.button_addauthor.setText(_translate("MainWindow", "Добавить автора"))
