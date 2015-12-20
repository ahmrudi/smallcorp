import sqlalchemy
from datetime import date
from sqlalchemy.exc import IntegrityError
from settings import Entity, session


class Anggota(Entity):
    __tablename__ = "anggota"
    __table_args__ = {'extend_existing':True}
    kode = sqlalchemy.Column(sqlalchemy.String(15), primary_key=True, unique=True)
    nama = sqlalchemy.Column(sqlalchemy.String(55))
    jenis_kelamin = sqlalchemy.Column(sqlalchemy.String(10))
    tempat_lahir = sqlalchemy.Column(sqlalchemy.String(55))
    tanggal_lahir = sqlalchemy.Column(sqlalchemy.Date, default=date.today())
    alamat = sqlalchemy.Column(sqlalchemy.String(100))
    telepon = sqlalchemy.Column(sqlalchemy.String(15))
    status = sqlalchemy.Column(sqlalchemy.Boolean, default=True)
    q = session.query_property()
    s = session()
    
    def indexKelamin(self):
        data = ["Laki-Laki", "Perempuan"]
        try:
            return data.index(self.jenis_kelamin)
        except ValueError:
            return 0
    
    def queryCreate(self):
        try:
            self.s.add(self)
            self.s.commit()
        except IntegrityError:
            self.s.rollback()
    
    def isModified(self):
        return self.s.is_modified(self)
    
    def queryUpdate(self):
        try:
            if self.isModified():
                self.s.commit()
                return True
            return False
        except Exception:
            self.s.rollback()
            return False
           
    def queryGet(self, kode):
        return self.q.get(kode)
       
    def queryDelete(self):
        try:
            self.s.delete(self)
        except:
            self.s.rollback()
    
    def queryDetail(self, kode = None):
        if kode is None:
            return self.q.get(self.kode)
        else:
            return self.q.get(kode)
        
    def cariData(self, kode):
        data = self.queryDetail(kode)
        return data