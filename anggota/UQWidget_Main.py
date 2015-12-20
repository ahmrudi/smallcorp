# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uis/UQWidget_Main.ui'
#
# Created: Sun Dec 20 14:19:38 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.cariLineEdit = QtGui.QLineEdit(Form)
        self.cariLineEdit.setObjectName("cariLineEdit")
        self.verticalLayout.addWidget(self.cariLineEdit)
        self.dataTableView = QtGui.QTableView(Form)
        self.dataTableView.setObjectName("dataTableView")
        self.verticalLayout.addWidget(self.dataTableView)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.cariLineEdit.setPlaceholderText(QtGui.QApplication.translate("Form", "Cari...", None, QtGui.QApplication.UnicodeUTF8))

