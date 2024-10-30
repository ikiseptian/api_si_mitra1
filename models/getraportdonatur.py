from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class CorezDonatur(Base):
    __tablename__ = "corez_donatur"

    id_crm = Column(Integer, primary_key=True, index=True)
    # id_crm = Column(String)
    aktif = Column(String)

class CorezTransaksiToday(Base):
    __tablename__ = "corez_transaksi_today"

    id_crm = Column(Integer, primary_key=True, index=True)
    # id_crm = Column(String)
    id_donatur = Column(String)
    tgl_donasi = Column(DateTime)