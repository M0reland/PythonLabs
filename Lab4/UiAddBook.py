# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UiAddBook.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(459, 347)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.line_auth_id = QtWidgets.QLineEdit(self.centralwidget)
        self.line_auth_id.setObjectName("line_auth_id")
        self.verticalLayout.addWidget(self.line_auth_id)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.line_name = QtWidgets.QLineEdit(self.centralwidget)
        self.line_name.setObjectName("line_name")
        self.verticalLayout.addWidget(self.line_name)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.line_pages = QtWidgets.QLineEdit(self.centralwidget)
        self.line_pages.setObjectName("line_pages")
        self.verticalLayout.addWidget(self.line_pages)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.line_publisher = QtWidgets.QLineEdit(self.centralwidget)
        self.line_publisher.setObjectName("line_publisher")
        self.verticalLayout.addWidget(self.line_publisher)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.line_years = QtWidgets.QLineEdit(self.centralwidget)
        self.line_years.setObjectName("line_years")
        self.verticalLayout.addWidget(self.line_years)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.button_add_book = QtWidgets.QPushButton(self.centralwidget)
        self.button_add_book.setMinimumSize(QtCore.QSize(150, 80))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.button_add_book.setFont(font)
        self.button_add_book.setObjectName("button_add_book")
        self.verticalLayout_2.addWidget(self.button_add_book)
        self.button_close = QtWidgets.QPushButton(self.centralwidget)
        self.button_close.setMinimumSize(QtCore.QSize(150, 80))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.button_close.setFont(font)
        self.button_close.setObjectName("button_close")
        self.verticalLayout_2.addWidget(self.button_close)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Добавить книгу"))
        self.label.setText(_translate("MainWindow", "ID автора"))
        self.label_2.setText(_translate("MainWindow", "Название книги"))
        self.label_3.setText(_translate("MainWindow", "Количество страниц"))
        self.label_5.setText(_translate("MainWindow", "Издательство"))
        self.label_4.setText(_translate("MainWindow", "Годы публикации"))
        self.button_add_book.setText(_translate("MainWindow", "Добавить книгу"))
        self.button_close.setText(_translate("MainWindow", "Закрыть окно"))
