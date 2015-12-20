from PySide import QtCore
from anggota.data import Anggota

class AnggotaTableModel(QtCore.QAbstractTableModel):
    modelRole = QtCore.Qt.UserRole
    def __init__(self, parent=None):
        super(AnggotaTableModel, self).__init__(parent)
        self.model = Anggota
        self.query = self.model.q
        self.__root = self.query.all()
    
    def rowCount(self, parent=QtCore.QModelIndex):
        return len(self.__root)
    
    def columnCount(self, parent=QtCore.QModelIndex):
        return 8
    
    def headerData(self, section, orientation, role):
        if role == QtCore.Qt.DisplayRole:
            if orientation == QtCore.Qt.Horizontal:
                if section == 0:
                    return "Kode"
                if section == 1:
                    return "Nama"
                if section == 2:
                    return "Jenis Kelamin"
                if section == 3:
                    return "Tempat Lahir"
                if section == 4:
                    return "Tanggal Lahir"
                if section == 5:
                    return "Telepon"
                if section == 6:
                    return "Alamat"
                if section == 7:
                    return "Status"
            else:
                return section + 1
    
    def data(self, index, role=QtCore.Qt.DisplayRole):
        if index.isValid():
            if role == QtCore.Qt.DisplayRole:
                data = self.__root[index.row()]
                if index.column() == 0:
                    return data.kode
                if index.column() == 1:
                    return data.nama
                if index.column() == 2:
                    return data.jenis_kelamin
                if index.column() == 3:
                    return data.tempat_lahir
                if index.column() == 4:
                    return str(data.tanggal_lahir)
                if index.column() == 5:
                    return data.telepon
                if index.column() == 6:
                    return data.alamat
                if index.column() == 7:
                    if data.status:
                        return "Aktif"
                    else:
                        return "Tidak Aktif"
            elif role == self.modelRole:
                return self.__root[index.row()]
    
    def resetData(self):
        self.reset()
        self.__root = self.query.all()