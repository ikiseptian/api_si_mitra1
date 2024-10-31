from sqlalchemy import Column, DateTime, Integer, String, Float, MetaData
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = MetaData()

class CorezTransaksi(Base):
    __tablename__ = 'corez_transaksi'
    __table_args__ = {'schema': 'zains_rz'}

    id_transaksi = Column(String, primary_key=True)
    id_donatur = Column(String)
    id_via_bayar = Column(Integer)
    id_program = Column(String)
    quantity = Column(Integer)
    transaksi = Column(Float)
    tgl_transaksi = Column(DateTime)
    id_kantor_transaksi = Column(Integer)
    id_penghimpunan = Column(Integer)
    id_via_himpun = Column(String)
    id_cara_bayar = Column(String)
    id_crm = Column(String)
    id_claim = Column(String)
    id_position_claim = Column(String)
    approved_transaksi = Column(String)
    keterangan = Column(String)
    user_insert = Column(String)
    tgl_donasi = Column(DateTime)


class CorezTransaksi(Base):
    __tablename__ = 'setting_donatrur'
    __table_args__ = {'schema': 'zains_rz'}

    
