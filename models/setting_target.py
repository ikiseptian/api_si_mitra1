from sqlalchemy import Column, Integer, String, Date, Float
from config.db_connection import Base

# Definisikan model CorezTransaksiToday
class CorezTransaksiToday(Base):
    __tablename__ = 'corez_transaksi_today'
    
    # Kolom tabel
    id = Column(Integer, primary_key=True, index=True)
    approved_transaksi = Column(String)
    id_crm = Column(Integer)
    transaksi = Column(Float)
    tgl_donasi = Column(Date)

# Definisikan model CorezTransaksiThisMonth
class CorezTransaksiThisMonth(Base):
    __tablename__ = 'corez_transaksi_thismonth'
    
    # Kolom tabel
    id = Column(Integer, primary_key=True, index=True)
    approved_transaksi = Column(String)
    id_crm = Column(Integer)
    transaksi = Column(Float)
    tgl_donasi = Column(Date)

# Definisikan model SettingTarget
class SettingTarget(Base):
    __tablename__ = 'setting_target'
    
    # Kolom tabel
    id = Column(Integer, primary_key=True, index=True)
    jenis = Column(String)
    id_jenis = Column(Integer)
    target = Column(Float)
    tgl_target = Column(Date)
