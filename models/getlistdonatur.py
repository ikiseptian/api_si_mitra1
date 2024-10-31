from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from config.db_connection import Base

class CorezTransaksiThisMonth1(Base):
    __tablename__ = 'corez_transaksi_thismonth'
    __table_args__ = {'extend_existing': True}

    id_crm = Column(String(255), primary_key=True)
    nilai_transaksi = Column(String(255))
    tgl_donasi = Column(Date)
    approved_transaksi = Column(String(255))
    id_program = Column(Integer, ForeignKey('setting_program.id_program'))

    # Mengubah definisi relationship
    program = relationship("SettingProgram", back_populates="transaksi_list")

class CorezDonatur(Base):
    __tablename__ = 'corez_donatur'
    __table_args__ = {'extend_existing': True}

    id_donatur = Column(Integer, primary_key=True)
    donatur = Column(String(255))
    aktif = Column(String(1))

class SettingProgram(Base):
    __tablename__ = 'setting_program'
    __table_args__ = {'extend_existing': True}

    id_program = Column(Integer, primary_key=True)
    program = Column(String(255))
    
    # Menambahkan relationship di sisi SettingProgram
    transaksi_list = relationship("CorezTransaksiThisMonth1", back_populates="program")