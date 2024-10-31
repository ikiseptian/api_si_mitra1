from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from ..config.db_connection import Base

class CorezTransaksiThisMonth1(Base):
    __tablename__ = 'corez_transaksi_thismonth'
    __table_args__ = {'extend_existing': True}
    
    # Mengubah foreign key untuk merujuk ke id_crm
    id_transaksi = Column(Integer, ForeignKey('corez_transaksi.id_crm'), primary_key=True)
    
    # Memperbaiki relationship dengan foreign keys yang benar
    transaksi = relationship(
        "CorezTransaksi1",
        primaryjoin="CorezTransaksiThisMonth1.id_transaksi==CorezTransaksi1.id_crm",
        back_populates="this_month",
        uselist=False
    )

class CorezTransaksi1(Base):
    __tablename__ = 'corez_transaksi'
    __table_args__ = {'extend_existing': True}
    
    id_crm = Column(Integer, primary_key=True)
    id_donatur = Column(String, ForeignKey('corez_donatur.id_crm'))
    approved_transaksi = Column(String)
    tgl_donasi = Column(Date)
    id_program = Column(Integer, ForeignKey('setting_program.id_program'))
    
    # Memperbaiki relationship
    this_month = relationship(
        "CorezTransaksiThisMonth1",
        primaryjoin="CorezTransaksi1.id_crm==CorezTransaksiThisMonth1.id_transaksi",
        back_populates="transaksi",
        uselist=False
    )
    donatur = relationship("CorezDonatur", back_populates="transaksi")
    program = relationship("SettingProgram", back_populates="transaksi")

class CorezDonatur(Base):
    __tablename__ = 'corez_donatur'
    __table_args__ = {'extend_existing': True}
    
    id_crm = Column(String, primary_key=True)
    aktif = Column(String)
    
    transaksi = relationship("CorezTransaksi1", back_populates="donatur")

class SettingProgram(Base):
    __tablename__ = 'setting_program'
    __table_args__ = {'extend_existing': True}
    
    id_program = Column(Integer, primary_key=True)
    program = Column(String)
    
    transaksi = relationship("CorezTransaksi1", back_populates="program")