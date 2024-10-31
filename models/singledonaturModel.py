from sqlalchemy import Column, Date, Enum, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = MetaData()

class SingleDonatur(Base):
    __tablename__ = 'corez_donatur'

    id_donatur = Column(String(20), primary_key=True, index=True)
    donatur = Column(String(50))
    hp = Column(String(30))
    email = Column(String(100))
    aktif = Column(Enum('y', 'n', 'p', 'u'))
    id_kantor = Column(String(4))
    id_jenis = Column(String(1))
    tgl_lahir = Column(Date)
    status = Column(Enum('Donatur', 'Mitra', 'UPZ', 'Kotak'))
    last_transaction = Column(Date)
    id_profiling = Column(String(1))
    whatsapp = Column(String(30))
