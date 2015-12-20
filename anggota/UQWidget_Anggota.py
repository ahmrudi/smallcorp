# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uis/UQWidget_Anggota.ui'
#
# Created: Sun Dec 20 09:06:15 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.formLayout = QtGui.QFormLayout(Form)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.kodeLabel = QtGui.QLabel(Form)
        self.kodeLabel.setObjectName("kodeLabel")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.kodeLabel)
        self.kodeLineEdit = QtGui.QLineEdit(Form)
        self.kodeLineEdit.setObjectName("kodeLineEdit")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.kodeLineEdit)
        self.namaLabel = QtGui.QLabel(Form)
        self.namaLabel.setObjectName("namaLabel")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.namaLabel)
        self.namaLineEdit = QtGui.QLineEdit(Form)
        self.namaLineEdit.setObjectName("namaLineEdit")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.namaLineEdit)
        self.tempatLahirLabel = QtGui.QLabel(Form)
        self.tempatLahirLabel.setObjectName("tempatLahirLabel")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.tempatLahirLabel)
        self.tempatLahirLineEdit = QtGui.QLineEdit(Form)
        self.tempatLahirLineEdit.setObjectName("tempatLahirLineEdit")
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.tempatLahirLineEdit)
        self.tanggalLahirLabel = QtGui.QLabel(Form)
        self.tanggalLahirLabel.setObjectName("tanggalLahirLabel")
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.tanggalLahirLabel)
        self.tanggalLahirDateEdit = QtGui.QDateEdit(Form)
        self.tanggalLahirDateEdit.setObjectName("tanggalLahirDateEdit")
        self.tanggalLahirDateEdit.setCalendarPopup(True)
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.tanggalLahirDateEdit)
        self.alamatLabel = QtGui.QLabel(Form)
        self.alamatLabel.setObjectName("alamatLabel")
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.alamatLabel)
        self.alamatTextEdit = QtGui.QTextEdit(Form)
        self.alamatTextEdit.setObjectName("alamatTextEdit")
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.alamatTextEdit)
        self.kodeLabel.setBuddy(self.kodeLineEdit)
        self.namaLabel.setBuddy(self.namaLineEdit)
        self.tempatLahirLabel.setBuddy(self.tempatLahirLineEdit)
        self.tanggalLahirLabel.setBuddy(self.tanggalLahirDateEdit)
        self.alamatLabel.setBuddy(self.alamatTextEdit)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Anggota Form", None, QtGui.QApplication.UnicodeUTF8))
        self.kodeLabel.setText(QtGui.QApplication.translate("Form", "Kode", None, QtGui.QApplication.UnicodeUTF8))
        self.namaLabel.setText(QtGui.QApplication.translate("Form", "Nama", None, QtGui.QApplication.UnicodeUTF8))
        self.tempatLahirLabel.setText(QtGui.QApplication.translate("Form", "Tempat Lahir", None, QtGui.QApplication.UnicodeUTF8))
        self.tanggalLahirLabel.setText(QtGui.QApplication.translate("Form", "Tanggal Lahir", None, QtGui.QApplication.UnicodeUTF8))
        self.alamatLabel.setText(QtGui.QApplication.translate("Form", "Alamat", None, QtGui.QApplication.UnicodeUTF8))

