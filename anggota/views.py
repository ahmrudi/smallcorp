import sys
from PySide import QtCore, QtGui
from data import Anggota
from models import AnggotaTableModel
import UQDialog
import UQWidget_Main



class FormAnggota(QtGui.QDialog, UQDialog.Ui_Dialog):
    __modified = False
    def __init__(self, mode = True, parent=None):
        super(FormAnggota, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Form Anggota")
        self.kodeLineEdit.returnPressed.connect(self.cariData)
        self.deletePushButton.clicked.connect(self.cmdDelete)
        self.disconnect(self.buttonBox, QtCore.SIGNAL("returnPressed()"), self.accept)
        self.setMode(mode)
    
    def setIsi(self, data):
        self.kodeLineEdit.setText(data.kode)
        self.namaLineEdit.setText(data.nama)
        self.tempatLahirLineEdit.setText(data.tempat_lahir)
        if data.tanggal_lahir is not None:
            self.tanggalLahirDateEdit.setDate(QtCore.QDate(data.tanggal_lahir.year, data.tanggal_lahir.month, data.tanggal_lahir.day))
        self.jenisKelaminComboBox.setCurrentIndex(data.indexKelamin())
        self.handphoneLineEdit.setText(data.telepon)
        self.alamatTextEdit.setText(data.alamat)
        self.statusCheckBox.setChecked(data.status)
        self.__data = data
    
    def setMode(self, create=True):
        try:
            self.buttonBox.accepted.disconnect(self.accept)
        except RuntimeError:
            try:
                self.buttonBox.accepted.disconnect(self.cmdCreate)
                self.buttonBox.accepted.disconnect(self.cmdUpdate)
            except RuntimeError:
                pass
        finally:
            if create:
                self.buttonBox.accepted.connect(self.cmdCreate)
            else:
                self.buttonBox.accepted.connect(self.cmdUpdate)
    
    def data(self):
        kode = self.kodeLineEdit.text()
        data = Anggota()
        new_data = data.queryGet(kode)
        if new_data is None:
            new_data = Anggota()
            new_data.kode = self.kodeLineEdit.text()
        new_data.tempat_lahir = self.tempatLahirLineEdit.text()
        new_data.tanggal_lahir = self.tanggalLahirDateEdit.date().toPython()
        new_data.alamat = self.alamatTextEdit.toPlainText()
        new_data.jenis_kelamin = self.jenisKelaminComboBox.currentText()
        new_data.telepon = self.handphoneLineEdit.text()
        new_data.nama = self.namaLineEdit.text()
        new_data.status = self.statusCheckBox.isChecked()
        return new_data

    def isValid(self):
        if len(self.kodeLineEdit.text()) > 4:
            return True
        return False
    
    def cmdCreate(self):
        if self.isValid():
            data = self.data()
            data.queryCreate()
            self.setMode(False)
            self.setStatusAction("Data berhasil ditambahkan.")
            self.__modified = True
    
    def isModified(self):
        return self.__modified
    
    def cmdUpdate(self):
        if self.isValid():
            data = self.data()
            if data.isModified():
                if data.queryUpdate():
                    self.setStatusAction("Data berhasil diubah.")
    
    def setStatusAction(self, text):
        self.statusAction.setText("<html><p style='color:red;'>*Data berhasil diubah.</span>")
        QtCore.QTimer.singleShot(1000, self.statusReset)
    
    def statusReset(self):
        self.statusAction.setText("")
            
    
    def cmdDelete(self):
        tanya = QtGui.QMessageBox.question(self, self.windowTitle(),
            "Data yang sudah dihapus tidak bisa dikembalikan.\nAnda yakin akan menghapus data %s?"%self.kodeLineEdit.text(),
            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.No)
        if tanya == QtGui.QMessageBox.Yes:
            data = self.data()
            data.queryDelete()
            self.reject()
    
    def cariData(self):
        anggota = Anggota()
        kode = self.kodeLineEdit.text()
        data = anggota.cariData(kode)
        if data is not None:
            self.setIsi(data)
            self.setMode(False)
        else:
            tanya = QtGui.QMessageBox.question(self, self.windowTitle(), "Data tidak ditemukan, buat baru?", \
                QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.No)
            if tanya == QtGui.QMessageBox.Yes:
                self.setMode(True)
                self.setIsi(anggota)
                self.kodeLineEdit.setText(kode)
            else:
                self.kodeLineEdit.undo()
                self.kodeLineEdit.undo()
            


class DataAnggotaWidget(UQWidget_Main.Ui_Form, QtGui.QWidget):
    
    def __init__(self, parent=None):
        super(DataAnggotaWidget, self).__init__(parent)
        self.setupUi(self)
        self.setData()
        self.dataTableView.horizontalHeader().setStretchLastSection(True)
        self.connect(self.dataTableView, QtCore.SIGNAL("doubleClicked(QModelIndex)"), self.cmdUpdateData)
    
    def setData(self):
        self.__model = AnggotaTableModel(self)
        self.__proxyModel = QtGui.QSortFilterProxyModel(self)
        self.__proxyModel.setSourceModel(self.__model)
        self.__proxyModel.setDynamicSortFilter(True)
        self.__proxyModel.setFilterKeyColumn(0)
        self.dataTableView.setModel(self.__proxyModel)
        self.connect(self.cariLineEdit, QtCore.SIGNAL("textChanged(QString)"), self.__proxyModel.setFilterRegExp)
        
    def cmdUpdateData(self, model):
        form = FormAnggota(mode=False)
        form.setIsi(model.data(self.__model.modelRole))
        if form.exec_() == form.Rejected:
            if form.isModified():
                self.setData()


class FormCariAnggota(QtGui.QDialog):
    def __init__(self, parent=None):
        super(FormCariAnggota, self).__init__(parent)
        self.vBoxLayout = QtGui.QVBoxLayout(self)
        self.setWindowTitle("Cari Anggota")
        
        self.data = DataAnggotaWidget(self)
        self.buttonBox = QtGui.QDialogButtonBox(QtGui.QDialogButtonBox.Ok | QtGui.QDialogButtonBox.Cancel, QtCore.Qt.Horizontal, self)
        
        self.data.dataTableView.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        for i in range(2, 7):
            self.data.dataTableView.setColumnHidden(i, True)
        
        self.vBoxLayout.addWidget(self.data)
        self.vBoxLayout.addWidget(self.buttonBox)
        
        self.buttonBox.accepted.connect(self.cmdAccept)
        self.buttonBox.rejected.connect(self.reject)
    
    def dataModel(self):
        return self.data.dataTableView.currentIndex()
    
    def cmdAccept(self):
        if self.dataModel().data(AnggotaTableModel.modelRole) is not None:
            self.accept()
        else:
            QtGui.QMessageBox.warning(self, self.windowTitle(), "Anda belum menentukan pilihan.")


class MainAnggota(QtGui.QMainWindow):
    
    def __init__(self, parent=None):
        super(MainAnggota, self).__init__(parent)
        self.setWindowTitle("Data Anggota")
        self.data = DataAnggotaWidget()
        self.setCentralWidget(self.data)



if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    app.setStyle("oxygen")
    main = FormCariAnggota()
    if main.exec_() == main.Accepted:
        print main.dataModel().data(AnggotaTableModel.modelRole).kode
    #form = FormAnggota()
    #form.exec_()
    sys.exit(app.exec_())