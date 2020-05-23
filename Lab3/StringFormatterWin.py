# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'StringFormatter.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.line_Input = QtWidgets.QLineEdit(Form)
        self.line_Input.setObjectName("line_Input")
        self.horizontalLayout_3.addWidget(self.line_Input)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.checkBox_Delete = QtWidgets.QCheckBox(Form)
        self.checkBox_Delete.setObjectName("checkBox_Delete")
        self.horizontalLayout.addWidget(self.checkBox_Delete)
        self.spinBox_HowMuch = QtWidgets.QSpinBox(Form)
        self.spinBox_HowMuch.setProperty("value", 5)
        self.spinBox_HowMuch.setObjectName("spinBox_HowMuch")
        self.horizontalLayout.addWidget(self.spinBox_HowMuch)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.checkBox_Ast = QtWidgets.QCheckBox(Form)
        self.checkBox_Ast.setObjectName("checkBox_Ast")
        self.verticalLayout.addWidget(self.checkBox_Ast)
        self.checkBox_Spaces = QtWidgets.QCheckBox(Form)
        self.checkBox_Spaces.setObjectName("checkBox_Spaces")
        self.verticalLayout.addWidget(self.checkBox_Spaces)
        self.checkBox_Sort = QtWidgets.QCheckBox(Form)
        self.checkBox_Sort.setObjectName("checkBox_Sort")
        self.verticalLayout.addWidget(self.checkBox_Sort)
        self.radioButton_BySize = QtWidgets.QRadioButton(Form)
        self.radioButton_BySize.setObjectName("radioButton_BySize")
        self.verticalLayout.addWidget(self.radioButton_BySize)
        self.radioButton_byLexic = QtWidgets.QRadioButton(Form)
        self.radioButton_byLexic.setObjectName("radioButton_byLexic")
        self.verticalLayout.addWidget(self.radioButton_byLexic)
        self.button_format = QtWidgets.QPushButton(Form)
        self.button_format.setObjectName("button_format")
        self.verticalLayout.addWidget(self.button_format)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.line_Result = QtWidgets.QLineEdit(Form)
        self.line_Result.setObjectName("line_Result")
        self.horizontalLayout_2.addWidget(self.line_Result)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "StringFormatter"))
        self.label.setText(_translate("Form", "Строка:"))
        self.checkBox_Delete.setText(_translate("Form", "Удалить все слова размером меньше"))
        self.label_3.setText(_translate("Form", "букв"))
        self.checkBox_Ast.setText(_translate("Form", "Заменить все цифры на *"))
        self.checkBox_Spaces.setText(_translate("Form", "Вставить по пробелу между символами"))
        self.checkBox_Sort.setText(_translate("Form", "Сортировать слова в строке"))
        self.radioButton_BySize.setText(_translate("Form", "По размеру"))
        self.radioButton_byLexic.setText(_translate("Form", "Лексикографически"))
        self.button_format.setText(_translate("Form", "Форматировать"))
        self.label_2.setText(_translate("Form", "Результат:"))
