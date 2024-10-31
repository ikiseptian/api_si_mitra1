# Di file models/getInfoDonatur.py
from sqlalchemy import Column, Integer, String
from ..config.db_connection import Base

class CorezDonatur5(Base):
    __tablename__ = "corez_donatur"
    __table_args__ = {'extend_existing': True}
    
    id_crm = Column(String, primary_key=True)
    aktif = Column(String)

class CorezTransaksiThisMonth2(Base):
    __tablename__ = "corez_transaksi_thismonth"
    __table_args__ = {'extend_existing': True}
    
    id_transaksi = Column(Integer, primary_key=True)
    id_crm = Column(String)
    id_donatur = Column(String)

class CorezDafThismonth(Base):
    __tablename__ = "corez_daf_thismonth"
    __table_args__ = {'extend_existing': True}
    
    id_daf = Column(Integer, primary_key=True)
    id_muzakki = Column(String)
    nia_zisco = Column(String)