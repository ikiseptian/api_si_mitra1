from sqlalchemy import Column, Integer, String, Date
from app.db_connection import Base

class CorezDonatur(Base):
    __tablename__ = "corez_donatur"
    id_crm = Column(String, primary_key=True)
    aktif = Column(String)

class CorezTransaksiToday(Base):
    __tablename__ = "corez_transaksi_today"
    id_crm = Column(Integer, primary_key=True, autoincrement=True)  # Tambahkan kolom id sebagai primary key
    # id_crm = Column(String)
    id_donatur = Column(Integer)
    tgl_donasi = Column(Integer)

# Tambahkan model lainnya seperti CorezTransaksiThisMonth, CorezTransaksiThisYear, dll.
